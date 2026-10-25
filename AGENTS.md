# Working on these dotfiles

- Keep changes small and readable. Use short tables for completed and remaining work.
- Document the current setup, not conversations, decision history or retired implementations.
- Start with Pi; add other apps only when requested.
- Use `stow/` packages with an explicit target and `--no-folding`. Preview first; never adopt, override or force links.
- Resolve conflicts with a reviewed merge and a backup outside this repository.
- Keep secrets and runtime data outside Git. Never bulk-copy agent or home directories.
- Pin third-party Pi packages; record references, copied-file origins and licenses in `REFERENCES.md`.
- Never silently enable billing, Extra Usage, priority processing or delegation tools.
- Test deployment only against a temporary `DOTFILES_TARGET`, never the real home.
- Review the diff; do not commit or push unless asked.
