from support import REPO, TemporaryHome, tree_state


class SetupTests(TemporaryHome):
    def test_preview_creates_no_links_or_directories(self):
        # Given a fresh target
        before = tree_state(self.target)
        # When
        result = self.setup("pi-core", "pi-ui")
        # Then
        self.assertIn("Preview only", result.stdout)
        self.assertEqual(tree_state(self.target), before)

    def test_apply_links_every_managed_file_without_folding_directories(self):
        # Given a fresh target
        packages = [REPO / "stow/pi-core", REPO / "stow/pi-ui"]
        # When
        self.setup("--apply", "pi-core", "pi-ui")
        # Then
        for package in packages:
            for source in package.rglob("*"):
                destination = self.target / source.relative_to(package)
                with self.subTest(path=destination.relative_to(self.target)):
                    if source.is_file():
                        self.assertTrue(destination.is_symlink())
                        self.assertEqual(destination.resolve(), source.resolve())
                    else:
                        self.assertTrue(destination.is_dir())
                        self.assertFalse(destination.is_symlink())

    def test_repeat_apply_keeps_links_and_runtime_content_unchanged(self):
        # Given an applied target with local credentials and runtime files
        self.setup("--apply", "pi-core", "pi-ui")
        self.write_target(".pi/agent/auth.json", '{"fixture":"not-a-credential"}\n')
        self.write_target(".pi/agent/sessions/local.jsonl", '{"local":true}\n')
        self.write_target(".pi/agent/tasks/backlog.md", "# Private requests\n")
        before = tree_state(self.target)
        # When
        self.setup("--apply", "pi-core", "pi-ui")
        # Then
        self.assertEqual(tree_state(self.target), before)

    def test_remove_unlinks_managed_files_but_preserves_runtime_content(self):
        # Given an applied target with local credentials and runtime files
        self.setup("--apply", "pi-core", "pi-ui")
        runtime = {
            ".pi/agent/auth.json": '{"fixture":"not-a-credential"}\n',
            ".pi/agent/sessions/local.jsonl": '{"local":true}\n',
            ".pi/agent/tasks/backlog.md": "# Private requests\n",
        }
        for path, content in runtime.items():
            self.write_target(path, content)
        # When
        self.setup("--remove", "pi-core", "pi-ui")
        # Then
        for package in (REPO / "stow").iterdir():
            for source in package.rglob("*"):
                if source.is_file():
                    destination = self.target / source.relative_to(package)
                    self.assertFalse(destination.is_symlink(), str(destination))
                    self.assertFalse(destination.exists(), str(destination))
        for path, content in runtime.items():
            destination = self.target / path
            self.assertFalse(destination.is_symlink())
            self.assertEqual(destination.read_text(), content)

    def test_existing_settings_refuse_apply_without_partial_deployment(self):
        # Given a settings file owned by the user
        self.write_target(".pi/agent/settings.json", '{"existing":true}\n')
        before = tree_state(self.target)
        # When
        result = self.setup("--apply", "pi-core", "pi-ui", check=False)
        # Then
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("would cause conflicts", result.stderr)
        self.assertIn("All operations aborted", result.stderr)
        self.assertIn("settings.json", result.stderr)
        self.assertEqual(tree_state(self.target), before)

    def test_existing_custom_agent_refuses_apply_without_partial_deployment(self):
        # Given a custom agent owned by the user
        self.write_target(".pi/agent/agents/planner.md", "Existing planner\n")
        before = tree_state(self.target)
        # When
        result = self.setup("--apply", "pi-core", check=False)
        # Then
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("would cause conflicts", result.stderr)
        self.assertIn("All operations aborted", result.stderr)
        self.assertIn("planner.md", result.stderr)
        self.assertEqual(tree_state(self.target), before)

    def test_removed_calm_package_is_rejected_without_changes(self):
        # Given a fresh target and the retired package
        before = tree_state(self.target)
        # When
        result = self.setup("--apply", "pi-calm", check=False)
        # Then
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Unknown package: pi-calm", result.stderr)
        self.assertFalse((REPO / "stow/pi-calm").exists())
        self.assertEqual(tree_state(self.target), before)

    def test_unknown_package_is_rejected_before_applying_valid_packages(self):
        # Given a valid package followed by an unknown package
        before = tree_state(self.target)
        # When
        result = self.setup("--apply", "pi-core", "unknown", check=False)
        # Then
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Unknown package: unknown", result.stderr)
        self.assertEqual(tree_state(self.target), before)

    def test_missing_target_is_rejected_without_creating_it(self):
        # Given a target that does not exist
        missing = self.root / "missing"
        self.env["DOTFILES_TARGET"] = str(missing)
        # When
        result = self.setup("--apply", "pi-core", check=False)
        # Then
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(f"Target must already exist: {missing}", result.stderr)
        self.assertFalse(missing.exists())
        self.assertEqual(tree_state(self.target), {})

    def test_home_stow_defaults_are_refused_without_reading_their_options(self):
        # Given dangerous hidden Stow defaults in the isolated home
        rc = self.home / ".stowrc"
        rc.write_text("--adopt\n")
        before = tree_state(self.target)
        # When
        result = self.setup("--apply", "pi-core", check=False)
        # Then
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(f"Review existing Stow defaults before using this wrapper: {rc}", result.stderr)
        self.assertEqual(rc.read_text(), "--adopt\n")
        self.assertEqual(tree_state(self.target), before)

    def test_dangling_home_stowrc_is_also_refused_without_changes(self):
        # Given a dangling rc link in the isolated home
        rc = self.home / ".stowrc"
        rc.symlink_to(self.home / "missing-defaults")
        before = tree_state(self.target)
        # When
        result = self.setup("--apply", "pi-core", check=False)
        # Then
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(f"Review existing Stow defaults before using this wrapper: {rc}", result.stderr)
        self.assertTrue(rc.is_symlink())
        self.assertEqual(tree_state(self.target), before)
