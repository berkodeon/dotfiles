"""Temporary homes and real commands shared by the deployment checks."""

import os
from pathlib import Path
import subprocess
import tempfile
import unittest


REPO = Path(__file__).resolve().parents[1]


class TemporaryHome(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="dotfiles-test-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.home = self.root / "home"
        self.target = self.root / "target"
        self.home.mkdir()
        self.target.mkdir()
        self.env = {
            **{key: value for key, value in os.environ.items() if not key.startswith("GIT_")},
            "HOME": str(self.home),
            "XDG_CONFIG_HOME": str(self.home / ".config"),
            "DOTFILES_TARGET": str(self.target),
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_CONFIG_GLOBAL": os.devnull,
        }

    def run_command(self, *args, cwd=None, check=True):
        try:
            result = subprocess.run(
                args, cwd=cwd or self.root, env=self.env,
                text=True, capture_output=True, timeout=30,
            )
        except FileNotFoundError:
            self.fail(f"Required command not found: {args[0]}. Install it separately before running the checks.")
        if check:
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        return result

    def setup(self, *args, check=True):
        return self.run_command("bash", str(REPO / "scripts/setup"), *args, check=check)

    def write_target(self, path, content):
        destination = self.target / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content)
        return destination


def tree_state(root):
    """Record directories, link destinations and file bytes without following links."""
    return {
        str(path.relative_to(root)): (
            ("link", os.readlink(path)) if path.is_symlink() else
            ("directory",) if path.is_dir() else ("file", path.read_bytes())
        )
        for path in root.rglob("*")
    }
