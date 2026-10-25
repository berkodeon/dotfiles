# Berk's dotfiles

My Pi configuration, managed as plain files with GNU Stow.
See [components and references](REFERENCES.md) for what each piece does and why it is here.

## Managed configuration

| Package | Contents |
| --- | --- |
| `pi-core` | Preferences, tab spinner, Claude bridge, agent routing, skills and request tracking |
| `pi-ui` | Rosé Pine Moon theme |
| `Brewfile` | GNU Stow and current Homebrew Node |

## Setup

Install Homebrew and Git first, then:

```sh
git clone git@github.com:berkodeon/dotfiles.git ~/Dev/Personal/dotfiles
cd ~/Dev/Personal/dotfiles
brew bundle install --file=Brewfile
node --version
bash scripts/setup pi-core
```

Install and authenticate Pi and the required agent CLIs separately. Resolve any
Homebrew link conflicts before continuing. Run the test suite after runtime upgrades.

### Configuration links

`scripts/setup` validates packages and the target, rejects `.stowrc` overrides,
and previews Stow operations before applying them.

| Command | Result |
| --- | --- |
| `bash scripts/setup pi-core` | Preview only; nothing is linked |
| `bash scripts/setup --apply pi-core` | Preview, then create individual file links |
| `bash scripts/setup --remove pi-core` | Preview, then unlink managed files |
| `bash scripts/setup --apply pi-ui` | Preview, then link the appearance files |

Set `DOTFILES_TARGET` to an existing directory's absolute path; the default is your home.
Directories are never folded into links. Credentials, sessions and downloads stay local.

### Existing settings

Close Pi first. Back up conflicting files outside this repo, preserving their
permissions. Merge the portable preferences, then move only the reviewed conflicts
to that backup. Preview again before applying. Never use `--adopt` or force links.

After applying `pi-core`, install its declared extensions:

```sh
pi update --extensions
```

Settings may also resolve packages on Pi startup. Restart Pi with a new session,
check `/model`, `/subagents-models` and `/subagents-doctor`, and authenticate each
provider. Codex uses Pi's native `openai-codex` provider; Claude uses `claude-bridge`.
Claude is configured for the Pro plan with Extra Usage and AskClaude disabled.

After applying `pi-ui`, use `/reload` and select `rose-pine-moon` in `/settings`.
Pi can write through its linked settings file, so review the resulting Git diff.

## Pi workflow

| Piece | Purpose |
| --- | --- |
| Model routing | Codex parent; Luna scout; Sol workers/reviewer; Claude planner, oracle and independent reviewer |
| `quality-cycle` | Evidence, meaningful tests and separate reviews for substantial work; tiny edits skip ceremony |
| Ponytail | Minimal complete changes; reviewers use its review skill |
| tasks-axi | Private request ledger at `~/.pi/agent/tasks/backlog.md`, outside Git |
| `/requests` | Optional read-only shortcut for request status; ordinary questions work too |
| `pi-tab-spinner` | Packaged tab animation while Pi works; disappears when the run settles; no naming-model calls |

Project settings can override routing. Child execution uses native missions;
requests track the user's asks. Only delivered messages can be captured, and queued
items do not authorize execution. There is no automatic cross-provider fallback.
For a status view without model tokens, run this directly in your terminal:

```sh
tasks-axi list --file "$HOME/.pi/agent/tasks/backlog.md" --state queued --fields held,hold_reason
```

## Planned work

Configuration and installation candidates from the **2026-10-04** inventory.

| Area | Next step | Status |
| --- | --- | --- |
| Agent installation | Document install/update routes for Pi, Claude, Codex and tasks-axi | Pending |
| Package versions | Pin the four existing unversioned Pi declarations listed in the references | Pending |

<details>
<summary>Later: app configuration and installation candidates</summary>

| Area | Next step | Status |
| --- | --- | --- |
| Zsh | Review `.zshrc`, `.zprofile`, `.zshenv`, `.profile`, `.zsh/` and `.zfunc/`; keep only portable aliases, completions and PATH settings | Later |
| Shell plugins | Record Oh My Zsh, autosuggestions, syntax highlighting and Powerlevel10k installation; track `.p10k.zsh`, not downloaded repos | Later |
| Shell secrets | Keep the conditional local secrets hook; never import `.zshrc.secrets` | Later |
| Herdr and iTerm | Record installation; export portable settings, profiles and keybindings, not sessions or private plists | Later |
| Git and GitHub CLI | Review aliases, ignores and preferences; separate identity, URL rewrites, machine paths and authentication | Later |
| Neovim | Choose between `nvim/` and `nvim-config/`; track selected Lua/lockfile or pin the external repo, without nested `.git` directories | Decision needed |
| VS Code and Cursor | Review settings, snippets, keybindings and MCP secrets; record 43/34 observed extension IDs; confirm Cursor is still used | Later |
| IntelliJ and Sublime | Export selected settings and IdeaVim; decide IDE sync; exclude Sublime's user CA bundle | Later |
| Window management | Review AeroSpace rules and generated launch agent; decide whether Amethyst is also wanted | Later |
| Font | Declare JetBrains Mono Nerd Font if keeping it | Later |
| Shared AI instructions | Review `~/AGENTS.md`, shared skills and skill lockfile; do not import workspace-specific policy blindly | Later |
| Claude Code and Codex | Review portable settings, rules and skills; record plugins, not caches, credentials or project trust history | Later |
| Pi skills | Record the desired `find-skills` source and install method | Later |
| OpenCode and other agents | Review OpenCode settings/package declarations; confirm Treehouse and other tools are still used before adding them | Later |
| Global JavaScript tools | Review Codex, Corepack, Neovim provider, Prettier, ts-node, TypeScript, Yarn and legacy PhantomJS before declaring them | Later |
| Python | Choose pyenv/pipx/uv strategy and required versions; record applications such as Ruff and VisiData, not virtual environments | Decision needed |
| Rust and Go | Record installation routes and wanted toolchains | Later |
| R and RStudio | Choose R/Rig declarations; review Makevars and editor preferences, not `.Renviron` or history | Later |
| Data tools | Review VisiData, vdpm, Gobang and Harlequin settings/plugins without database secrets | Later |
| Other shell tools | Check whether Fish, Tele and Yarn preferences are still wanted | Later |
| SSH and private services | Use reviewed templates or local includes for SSH, AWS, Kubernetes, Google Cloud and CircleCI; keep keys and credentials local | Later |
| Database clients and VPN | Export only safe UI preferences; keep connections and VPN profiles local | Later |

### Installation candidates

These came from the same inventory. Review active use and installation channels
before adding declarations; do not uninstall duplicates just because they appear here.

| Group | Candidates |
| --- | --- |
| Everyday CLI | Git, gh, ripgrep, fd, fzf, jq, tree, wget, watch, ncdu, lazygit |
| Editors and build tools | Neovim, Vim, CMake, GCC, Make, pkg-config/pkgconf, LuaRocks, tree-sitter; Perl only if needed |
| Python quality tools | pyenv, pipx, Ruff, isort, py-spy |
| Cloud and CI | AWS CLI, AWS IAM Authenticator, CircleCI, kubectl, Helm, Kustomize; choose between the observed Google Cloud casks |
| Data and diagnostics | PostgreSQL 15, golang-migrate, parquet-cli, usql, Gobang, vdpm, k6, Graphviz, Ghostscript, VHS, Tele, OpenCode |
| Desktop utilities | AeroSpace, Amethyst, Jumpcut, OrbStack, JetBrains Mono Nerd Font; review portable OrbStack preferences separately from VM/container data |
| Development apps | iTerm, VS Code, IntelliJ IDEA, Sublime Text, Bruno, DBeaver, FileZilla, Xcode |
| Daily apps | 1Password, Vivaldi, Slack, Telegram, Amphetamine |
| Machine-specific apps | OpenVPN Connect, Brother iPrint&Scan, OnyX |
| R | R, R.app and Rig; choose the intended combination |

</details>

## Checks and everyday changes

```sh
python3 -m unittest discover -s tests -v
```

| Check | What it proves |
| --- | --- |
| Setup | Preview, repeated apply, individual links, conflict refusal, runtime preservation and unlinking in temporary directories |

Tests require Python 3, Bash and GNU Stow. They use the Python standard library
and temporary homes and targets. No Pi installation, downloaded extensions or
model requests are needed.

Review `git status`, `git diff` and staged files before committing. On another machine,
close Pi, pull into a clean working tree with `git pull --ff-only`, review changes,
then preview/apply affected packages and reconcile extensions. Linked files change
as soon as Git updates them. Unlinking does not uninstall packages or sign out accounts;
restore backed-up settings before reopening Pi if rolling back.

Never track tokens, authentication stores, private keys, cloud/VPN credentials,
sessions, histories, logs, sockets, caches, downloaded packages, virtual environments,
browser profiles, VM/container data or backups. Ignore rules are not a secret scanner.
See [AGENTS.md](AGENTS.md) for editing rules.
