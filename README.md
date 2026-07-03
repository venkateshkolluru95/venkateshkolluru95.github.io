# Venkatesh Kolluru - Portfolio

Personal portfolio at [venkateshkolluru95.github.io](https://venkateshkolluru95.github.io).

Venkatesh Kolluru, Ph.D. - Research Scientist III at NASA MSFC ODSI / University of Alabama in Huntsville. Earth observation, landscape ecology, hydrology, and geospatial foundation models.

A dark-cosmic single page built around an interactive 3D Earth (Three.js). Pure static files, no build step - `index.html` is the whole site. Content lives in `data.json`, so most updates need no code changes.

## Run locally
Any static file server works (opening via `file://` blocks the data fetches). From this folder:

```bash
python3 -m http.server 8000     # then open http://localhost:8000/
```

## Edit content
Most content is in `data.json` - edit it, commit, and the live site updates on the next deploy. No build step.

| Key in `data.json` | What it drives |
| --- | --- |
| `news`      | News ticker (newest first) |
| `talks`     | Talks & Presentations list (role + venue + link) |
| `awards`    | Recognition coverflow (media, org, source link) |
| `scholar`   | Google Scholar metrics shown on the Publications chip (citations, h-index, i10) |
| `publications_featured` | Under-review / preprint papers pinned to the top |
| `publications_fallback` | Curated list used if OpenAlex is unreachable |

Other content:

| Location | What it drives |
| --- | --- |
| `index.html` | Hero, About, AI/Ecology cards, Projects, Experience, Contact copy and links |
| `assets/travel_web/manifest.json` | Ground Truth travel sites (coords, covers, photos, videos) |
| `assets/proj_web/`, `assets/awards_web/` | Project / AI-card media and award media |
| `assets/portrait.jpg` | About-section portrait |
| `llms.txt` | Plain-text profile for AI assistants / crawlers |

**Publications are automatic.** They fetch live from OpenAlex (ORCID `0000-0002-2110-5560`); new papers with a DOI appear on their own. Citation metrics come from Google Scholar and are set manually in `data.json > scholar` (OpenAlex undercounts) - refresh them periodically.

## Media pipeline
Raw camera originals (`assets/travel/`, `assets/awards/`, `assets/project_cards/`) are git-ignored; only web-optimized copies ship (~170 MB). To add media: convert with `sips`/`ffmpeg` into the matching `*_web/` folder, update the relevant manifest/`data.json`, and commit.

## Deploy
Hosted on GitHub Pages from `main` / root. Every push to `main` rebuilds the live site in ~1 minute:

```bash
git add -A && git commit -m "Update content" && git push
```

Responsive (hamburger drawer on mobile/tablet) and respects `prefers-reduced-motion`.
