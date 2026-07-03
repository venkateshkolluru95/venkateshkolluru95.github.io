# Updating the site

Almost everything you'd change lives in one file: **`data.json`**. No coding, no build step.

## The easy way (no terminal, works from your phone)
1. Open the repo on GitHub - click **`data.json`**.
2. Click the **pencil (edit) icon** at the top-right.
3. Edit or paste your text (templates below).
4. Scroll down and click **Commit changes**.
5. The live site rebuilds automatically in about 1 minute.

> **Golden rule:** `data.json` is picky about punctuation. Every item in a list needs a comma after it **except the last one**, and all text uses straight quotes `"`. If the site ever goes blank after an edit, a missing comma or a curly quote is almost always why. Paste the file back to Claude and it's a 10-second fix.

---

## Publications - mostly automatic
- **A newly published paper (has a DOI):** do nothing. It appears on its own from Google Scholar / OpenAlex within days.
- **An under-review or preprint paper:** add it to the `publications_featured` list (these are pinned to the top):
  ```json
  {
   "year": 2026,
   "authors": "Kolluru, V., Coauthor, A., & Coauthor, B.",
   "title": "Your paper title here",
   "venue": "Journal name (Under Review)",
   "status": "under review",
   "doi": "https://doi.org/..."
  }
  ```
- **Citation numbers** (they do not auto-update, Google blocks that): edit the `scholar` block with fresh numbers from your Google Scholar profile:
  ```json
  "scholar": { "citations": 950, "hindex": 16, "i10": 19, "user": "7Tji1bMAAAAJ", "updated": "2026-09-01" }
  ```

## Awards - `awards` list
```json
{ "year": "2026", "title": "Award Name", "org": "Awarding Body" }
```
Optional extras:
- `"link": "https://..."` makes the card link to a source.
- `"media": "filename.jpg", "mtype": "photo"` shows an image (drop the file in `assets/awards_web/`). Use `"mtype": "doc"` for certificates/letters, or `"mtype": "video"` with `"poster": "filename_poster.jpg"` for a video.

## Talks & Presentations - `talks` list
```json
{ "title": "Talk title", "venue": "Conference 2026", "year": "2026", "role": "lead", "kind": "oral", "link": "https://..." }
```
- `role`: `"lead"` shows a **PRESENTER** badge; `"co"` shows **CO-AUTHOR**.
- `kind`: `"oral"`, `"upcoming"`, or `""` (blank for a poster/standard).
- `link` is optional.

## News ticker - `news` list (newest first)
```json
{ "date": "Sep'26", "html": "Your update with <b>bold</b> and a <a href=\"https://...\" target=\"_blank\" rel=\"noopener\">link</a>." }
```

---

## Bigger changes
These touch `index.html` or need image/video processing, so they are easiest to hand to Claude:
- Hero headline, About text, project or experience descriptions
- Adding travel photos/videos (need resizing + `assets/travel_web/manifest.json` update)
- New project or AI-card images (need resizing into `assets/proj_web/`)
- Portrait swap (`assets/portrait.jpg`)

## Publishing an edit from your computer (alternative to the web editor)
```bash
cd "path/to/site"
git add -A
git commit -m "Update content"
git push
```
The site rebuilds in about 1 minute at https://venkateshkolluru95.github.io.
