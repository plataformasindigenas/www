# www: two small sites

| Folder | Site | Built with |
|---|---|---|
| [`portal/`](portal/) | <https://plataformas.terradoc.org/>, the Plataformas Indígenas portal (pt/en/es) | Vite + Tailwind (`cd portal && npm ci && npm run build`) |
| [`landing/`](landing/) | <https://terradoc.org/>, the terradoc software page | nothing: plain HTML, served as is |

Every push is built by `.github/workflows/publish.yml` and published as the git refs
`refs/portal/<branch>` and `refs/landing/<branch>`; the web server picks them up within about two
minutes (terradoc's `sitepull`, see `plataformasindigenas/terradoc/server/README.md`). `master` is
production. Any other branch is a preview at `https://previews.terradoc.org/plataformas/<branch>/`
and `https://previews.terradoc.org/terradoc/<branch>/`; the portal's links are root-relative, so a
portal preview shows each page but its menu leads to the live site's paths.

If a build fails, the live sites keep their last good version and an issue
"Publicação falhou: <branch>" is opened.
