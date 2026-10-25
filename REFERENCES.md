# Components and references

Managed components, versions and licenses. Homebrew follows current formulae;
Pi package versions are specified in `settings.json`.

## Installed components and declarations

| App | Component | Why it is here | Version or reference | License |
| --- | --- | --- | --- | --- |
| Setup | [GNU Stow](https://www.gnu.org/software/stow/manual/stow.html) | Link individual configuration files without copying home directories | `Brewfile`: current formula | GPL-3.0-or-later |
| Pi runtime | [Node.js](https://nodejs.org/) | Run Pi and its JavaScript extensions | `Brewfile`: current `node` formula | MIT and bundled dependency licenses |
| Testing | [Python](https://docs.python.org/3/library/unittest.html) | Run behavioral checks with standard-library unittest, tempfile, pathlib and subprocess; no test dependencies | Python 3; installed separately | PSF-2.0 |
| Pi | [Pi coding agent](https://github.com/badlogic/pi-mono) | The agent these settings configure | Checked with 1.0.1; installed separately | MIT |
| Pi | [Tab spinner](https://github.com/ymy88/pi-tab-spinner) | Show activity in the terminal tab title | `pi-tab-spinner@0.1.0` | MIT |
| Pi | [Claude bridge](https://github.com/elidickinson/pi-claude-bridge) | Use Claude through its Agent SDK with account billing safeguards | `pi-claude-bridge@0.9.1` | MIT |
| Pi | [FFF](https://github.com/dmtrKovalenko/fff/tree/main/packages/pi-fff) | File/content search tools | `@ff-labs/pi-fff`, unpinned; local 0.11.0 | MIT |
| Pi | [Subagents](https://github.com/nicobailon/pi-subagents) | Planning, delegated work and independent reviews | `pi-subagents@0.79.2` | MIT |
| Pi | [Web access](https://github.com/nicobailon/pi-web-access) | Search, fetch and source checking for research | `pi-web-access@0.43.0` | MIT |
| Pi | [Ponytail](https://github.com/DietrichGebert/ponytail) | Small complete changes and focused review skills | `@dietrichgebert/ponytail@5.3.2` | MIT |
| Pi | [Supi Context](https://github.com/mrclrchtr/supi/tree/main/packages/supi-context) | Context-management support | `@mrclrchtr/supi-context`, unpinned; local 11.0.0 | MIT |
| Pi | [Intercom](https://www.npmjs.com/package/pi-intercom) | Coordinate existing local Pi sessions | `pi-intercom`, unpinned; local 0.18.0 | MIT |
| Pi | [BTW](https://github.com/dbachelder/pi-btw) | Side conversations without interrupting the main task | `pi-btw`, unpinned; local 0.8.0 | MIT |
| Pi requests | [tasks-axi](https://github.com/kunchenguid/tasks-axi) | Maintain the private request ledger | CLI 0.2.6; installed separately | MIT |

“Local” versions identify installed releases of unpinned declarations.
Codex uses Pi's native `openai-codex` provider.

## Managed files

| App | Files | Why | Reference and license |
| --- | --- | --- | --- |
| Pi appearance | `pi-ui` theme | Rosé Pine Moon colors | Unchanged theme from [kunchenguid/dotfiles](https://github.com/kunchenguid/dotfiles/tree/9a4a6387d0dd6f4bf9b8a5a732b406916bbbf95d/home/.pi/agent), commit `9a4a6387d0dd6f4bf9b8a5a732b406916bbbf95d`; [MIT-0](https://github.com/kunchenguid/dotfiles/blob/9a4a6387d0dd6f4bf9b8a5a732b406916bbbf95d/LICENSE) |
| Pi preferences | `pi-core` settings | Portable UI preferences and explicit model routing | General UI preferences adapted from the same MIT-0 reference; routing/custom agents configured locally |
| Pi requests | `skills/tasks-axi/` | Make the request CLI discoverable as a skill | Copied unchanged from installed tasks-axi 0.2.6, `skills/tasks-axi/SKILL.md`; MIT license retained beside it |
| Pi workflow | `quality-cycle`, `/requests`, parent policy and custom agents | Evidence-led work, request status and bounded delegation | Repository-maintained workflow instructions |

## Further reading

| Reference | What it informed |
| --- | --- |
| [Homebrew Bundle](https://docs.brew.sh/Brew-Bundle-and-Brewfile) | Prerequisite installation |
| [Wesley Schwengle: GNU Stow](https://medium.com/@waterkip/managing-my-dotfiles-with-gnu-stow-262d2540a866) | App-sized Stow packages |
| [Alex Cloudstar: dotfiles](https://medium.com/@alexcloudstar/dotfiles-the-secret-weapon-for-effortless-configuration-management-c8354f02fbe1) | Small modules and an explicit Git workflow |
| [vdpm tests](https://github.com/berkodeon/vdpm/tree/cc7f7a947d30b536d148b3f6e4f275f667cd6c7e/tests) | Behavior-named Given/When/Then scenarios, temporary environments and real CLI checks |
