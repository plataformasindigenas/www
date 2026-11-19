# Plataforma de Línguas Indígenas: the portal

<https://plataformas.terradoc.org/> in Portuguese, English and Spanish. Built by
[terradoc](https://pypi.org/project/terradoc/) since 2026-11 (meta `domains/plataformas/P7-PLAN.md`),
like the platforms: same look, no data of its own, no grafismo (the project's neutral palette).

```
terradoc.yaml              settings (no data modules; pack: none)
requirements.txt           the terradoc version (bump it like the platforms)
locales/<pt|en|es>.yaml    site title, home sentence, description, hero text per language
data/pages/<locale>/       one Markdown file per page (same name in every language)
    home.md                shown on the home page under the photograph
    plataformas.md equipe.md contato.md privacidade.md
static/images/             photographs and logos (published as WebP by terradoc)
```

How pages work (menu order, pictures with credit, cards, old addresses): terradoc's
`docs/pages.md`. To try a change: `pip install -r requirements.txt`, then
`terradoc build -c terradoc.yaml --out /tmp/portal` and open `/tmp/portal/index.html`, or push
a branch and look at `https://previews.terradoc.org/plataformas/<branch>/`.

Still to do (the team): credits for the photographs (`terradoc check` lists them), a review of
the Spanish interface strings in terradoc.

Going back to the old Vite site: its last version is the tag `archive/portal-vite`. It would
also need a `public/sw.js` that removes terradoc's offline worker from visitors' browsers:
`self.addEventListener('install', () => self.skipWaiting()); self.addEventListener('activate',
e => e.waitUntil(self.registration.unregister()));`
