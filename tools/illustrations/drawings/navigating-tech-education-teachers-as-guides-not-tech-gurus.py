from pen import C, s

TITLE = "A signpost at the start of a winding path that leads past a laptop and a hammer to a flag"


def shapes():
    return [
        s('path d="M30 410 C220 410 240 345 380 345 S 560 280 640 250 S 700 200 720 168"', None, 'stroke-dasharray="14 12"'),
        # signpost: guidance, not answers
        s('path d="M120 238 V252 M120 292 V308 M120 348 V408"'),
        s('path d="M120 252 H212 L234 272 L212 292 H120 Z"', C["yellow"]),
        s('path d="M120 308 H44 L24 328 L44 348 H120 Z"', C["teal"]),
        # laptop
        s('rect x="325" y="238" width="112" height="72" rx="6"', C["blue"]),
        s('path d="M310 310 H452 L464 326 H298 Z"', C["gray"]),
        # hammer
        s('rect x="-8" y="0" width="16" height="84" rx="4" transform="translate(588 168) rotate(32)"', C["amber"]),
        s('rect x="-36" y="-16" width="72" height="28" rx="4" transform="translate(588 168) rotate(32)"', C["dark"]),
        # flag
        s('path d="M720 168 V52"'),
        s('path d="M720 54 L782 74 L720 94 Z"', C["coral"]),
    ]
