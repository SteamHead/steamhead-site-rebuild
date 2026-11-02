"""House style for blog header illustrations: black pen over flat brand colour.

Every shape is drawn twice: a flat fill nudged off-register (like a quick
marker fill), then a black pen outline on top. Canvas is 800x450 (16:9, the
homepage card ratio). Colours are the :root tokens in src/styles/global.css.
"""

C = dict(
    yellow="#F4CD15", amber="#EDA83E", teal="#5EB1BF", coral="#EF7B44",
    blue="#409FCD", gray="#D7D7D7", dark="#474747", mint="#E4EDEA",
    white="#ffffff", black="#000000",
)
OFF = "translate(7 6)"
PEN = 'stroke="#000" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"'


def s(el, fill=None, extra="", flat=False):
    """One shape. el is an SVG element minus fill/stroke, e.g. 'circle cx="1" cy="2" r="3"'.
    fill: brand colour or None (outline only). extra: outline-only attributes such as
    stroke-dasharray. flat=True: solid ink with no offset fill and no outline (chequers, pupils)."""
    return (el, fill, extra, flat)


def sketch(title, shapes, bg=C["mint"]):
    fills, lines = [], []
    for el, fill, extra, flat in shapes:
        if flat:
            lines.append(f'<{el} fill="{fill}"/>')
            continue
        if fill:
            fills.append(f'<{el} fill="{fill}"/>')
        lines.append(f'<{el} fill="none" {PEN} {extra}/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" role="img">\n'
            f'<title>{title}</title>\n<rect width="800" height="450" fill="{bg}"/>\n'
            f'<g transform="{OFF}">\n' + "\n".join(fills) + '\n</g>\n<g>\n'
            + "\n".join(lines) + '\n</g>\n</svg>\n')
