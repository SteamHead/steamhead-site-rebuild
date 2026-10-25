from pen import C, s

TITLE = "An open box of free maker resources, a light bulb and tools, carried along a path to a school building"


def shapes():
    return [
        s('line x1="20" y1="390" x2="780" y2="390"'),
        # resource box
        s('path d="M80 280 L270 280 L270 390 L80 390 Z"', C["amber"]),
        s('path d="M80 280 L50 240 M270 280 L300 240"'),
        s('rect x="100" y="205" width="70" height="75" rx="3"', C["blue"]),
        s('path d="M114 205 L114 280 M128 228 l30 0 M128 245 l30 0"'),
        s('rect x="190" y="200" width="20" height="80" rx="5"', C["teal"]),
        s('rect x="175" y="185" width="50" height="22" rx="4"', C["gray"]),
        s('path d="M110 150 l0 -18 M150 140 l8 -16 M70 165 l-14 -10"'),
        # path to the school
        s('path d="M300 370 C380 370 420 330 500 330"', None, 'stroke-dasharray="14 12"'),
        s('path d="M482 312 L504 330 L482 348"'),
        # school
        s('path d="M530 390 L530 220 L640 140 L750 220 L750 390 Z"', C["teal"]),
        s('rect x="615" y="320" width="50" height="70"', C["white"]),
        s('rect x="560" y="245" width="45" height="40"', C["white"]),
        s('rect x="675" y="245" width="45" height="40"', C["white"]),
        s('circle cx="640" cy="200" r="20"', C["yellow"]),
        s('path d="M640 140 L640 90 L680 102 L640 114"', C["coral"]),
    ]
