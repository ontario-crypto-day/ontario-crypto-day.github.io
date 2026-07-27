# tools

## make-social-image.py

Generates the 1200×630 social media card shown when an event page is shared.
Replaces the Photoshop file this design used to live in.

```sh
python3 tools/make-social-image.py --date "December 9, 2026" --logo waterloo \
    --out images/socialmedia-20261209.png
```

Then set `header.og_image` in the event's page to the new file — that is what
social platforms show when the page is shared. (`og_image` in `_config.yml` is
only the fallback, used by pages with no header image, such as `past.md`.)

Omit `--logo` for a card with no logo; the date is centred instead.

Requires Python 3 with [Pillow](https://pypi.org/project/Pillow/) (`pip3 install Pillow`)
and macOS, for the Helvetica Neue faces the original Photoshop design used.

**Adding a host institution:** drop a PNG in `images/logos/` and pass its name to
`--logo`. Transparent or white background both work; the logo is scaled down to
fit a 420×200 box and is never scaled up, so supply it at least 200px tall or it
will render small. `waterloo.png` and `mcmaster.png` were cropped out of the
social images made for the June 2025 and June 2026 events; `fields.png` was
downscaled from a logo off the Fields Institute site.

The June 2025 and June 2026 cards predate this script and were made by hand, so
regenerating them would shift the logo by a few pixels; leave them as they are.
