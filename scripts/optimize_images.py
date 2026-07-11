#!/usr/bin/env python3
"""One-time image optimization pass over public/images.

Rules (see PR description / TODO discussion):
- Everything: EXIF orientation baked in, longest side capped at 2000px.
- JPEGs: re-encoded at quality 82; kept only if >=10% smaller.
- PNGs WITH transparency: stay PNG (resized/re-encoded only if smaller).
- PNGs WITHOUT transparency: photographic ones (many unique colors) are
  converted to JPEG — filename changes .png -> .jpg, and every reference
  under src/ is rewritten; flat graphics are palette-quantized, staying PNG.
- HEIC: converted to JPEG (browsers can't display HEIC).
- GIF/MP4/SVG: untouched.

Rerunning is safe: already-optimized files won't shrink another 10%, so
they're left alone.
"""
import io, json, sys
from pathlib import Path
from PIL import Image, ImageOps
import pillow_heif
pillow_heif.register_heif_opener()

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / 'public/images'
MAX_SIDE = 2000
JPEG_Q = 82
MIN_WIN = 0.10          # replace only if >=10% smaller
PHOTO_COLORS = 4096     # unique-color threshold: above this a PNG is a photo

renames = {}            # old repo path -> new repo path
saved = kept = converted = 0
before_total = after_total = 0

def encode_jpeg(im):
    buf = io.BytesIO()
    im.convert('RGB').save(buf, 'JPEG', quality=JPEG_Q, optimize=True, progressive=True)
    return buf

def encode_png(im, quantize):
    buf = io.BytesIO()
    if quantize:
        im = im.quantize(256, method=Image.Quantize.FASTOCTREE)
    im.save(buf, 'PNG', optimize=True)
    return buf

for p in sorted(IMAGES.rglob('*')):
    if not p.is_file():
        continue
    ext = p.suffix.lower()
    if ext not in ('.jpg', '.jpeg', '.png', '.heic'):
        continue
    orig_size = p.stat().st_size
    before_total += orig_size
    try:
        im = Image.open(p)
        im.load()
        im = ImageOps.exif_transpose(im)
    except Exception as e:
        print(f'  !! unreadable, skipped: {p} ({e})', file=sys.stderr)
        after_total += orig_size
        continue

    if max(im.size) > MAX_SIDE:
        scale = MAX_SIDE / max(im.size)
        im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)

    new_path, buf = p, None
    if ext in ('.jpg', '.jpeg'):
        buf = encode_jpeg(im)
    elif ext == '.heic':
        buf = encode_jpeg(im)
        new_path = p.with_suffix('.jpg')
    else:  # png
        # alpha counts only if a meaningful share of pixels use it — many
        # WordPress-exported photos carry a vestigial alpha channel with a
        # handful of stray transparent pixels
        has_alpha = False
        if im.mode in ('RGBA', 'LA', 'PA'):
            hist = im.convert('RGBA').getchannel('A').histogram()
            has_alpha = sum(hist[:250]) / (im.width * im.height) > 0.01
        if has_alpha:
            buf = encode_png(im, quantize=False)
        else:
            thumb = im.convert('RGB')
            thumb.thumbnail((256, 256))
            ncolors = len(set(thumb.getdata()))
            if ncolors > PHOTO_COLORS:
                buf = encode_jpeg(im)
                new_path = p.with_suffix('.jpg')
            else:
                buf = encode_png(im.convert('RGB'), quantize=True)

    win = 1 - buf.tell() / orig_size
    must_rename = new_path != p
    if win >= MIN_WIN or must_rename:
        new_path.write_bytes(buf.getvalue())
        if must_rename:
            p.unlink()
            renames['/' + str(p.relative_to(ROOT / 'public'))] = '/' + str(new_path.relative_to(ROOT / 'public'))
            converted += 1
        saved += 1
        after_total += buf.tell()
    else:
        kept += 1
        after_total += orig_size

# rewrite references to renamed files everywhere under src/
touched = set()
if renames:
    for f in list(ROOT.glob('src/**/*.md')) + list(ROOT.glob('src/**/*.astro')):
        text = f.read_text()
        out = text
        for old, new in renames.items():
            out = out.replace(old, new)
        if out != text:
            f.write_text(out)
            touched.add(str(f.relative_to(ROOT)))

(ROOT / 'scripts/image-optimization-report.json').write_text(json.dumps({
    'before_mb': round(before_total / 1e6, 1),
    'after_mb': round(after_total / 1e6, 1),
    'files_optimized': saved,
    'files_unchanged': kept,
    'files_converted_to_jpeg': converted,
    'renames': renames,
    'content_files_rewritten': sorted(touched),
}, indent=2) + '\n')

print(f'{before_total/1e6:.0f} MB -> {after_total/1e6:.0f} MB '
      f'({(1-after_total/before_total)*100:.0f}% smaller); '
      f'{saved} optimized, {kept} unchanged, {converted} converted to JPEG, '
      f'{len(touched)} content files rewritten')
