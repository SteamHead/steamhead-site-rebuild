from pen import C, s

TITLE = "A light-up dress on a dress form at the end of a runway under two spotlights, with a video play button"


def shapes():
    sh = [
        # spotlight beams
        s('path d="M150 0 L210 0 L340 150 L300 175 Z"', C["white"], 'stroke-dasharray="10 10"'),
        s('path d="M650 0 L590 0 L460 150 L500 175 Z"', C["white"], 'stroke-dasharray="10 10"'),
        # runway
        s('path d="M250 400 L550 400 L640 450 L160 450 Z"', C["gray"]),
        # dress form: stand, bodice, skirt
        s('path d="M400 346 L400 400 M370 400 L430 400"'),
        s('circle cx="400" cy="92" r="10"', C["dark"]),
        s('path d="M355 112 Q400 98 445 112 L436 196 Q400 208 364 196 Z"', C["teal"]),
        s('path d="M364 200 Q400 212 436 200 L500 330 Q400 350 300 330 Z"', C["blue"]),
        # play button
        s('circle cx="660" cy="300" r="56"', C["coral"]),
        s('path d="M642 270 L690 300 L642 330 Z"', C["white"]),
    ]
    for x, y in ((380, 232), (420, 236), (360, 270), (400, 274), (440, 272), (338, 308), (378, 314), (424, 314), (464, 306)):
        sh.append(s(f'circle cx="{x}" cy="{y}" r="7"', C["yellow"]))
    return sh
