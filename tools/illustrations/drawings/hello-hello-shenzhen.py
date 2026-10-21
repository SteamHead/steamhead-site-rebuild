from pen import C, s

TITLE = "A plane flying a dashed route between two city skylines, with a suitcase waiting at the arrival city"


def shapes():
    sh = [s('line x1="20" y1="380" x2="780" y2="380"')]
    # left skyline
    for x, w, h, col in ((50, 50, 120, C["gray"]), (105, 60, 180, C["teal"]), (170, 45, 100, C["gray"])):
        sh.append(s(f'rect x="{x}" y="{380-h}" width="{w}" height="{h}"', col))
    # right skyline
    for x, w, h, col in ((560, 50, 150, C["gray"]), (615, 40, 230, C["blue"]), (660, 70, 120, C["gray"]), (735, 40, 170, C["teal"])):
        sh.append(s(f'rect x="{x}" y="{380-h}" width="{w}" height="{h}"', col))
    sh += [
        s('path d="M150 180 C250 40 500 40 610 130"', None, 'stroke-dasharray="14 12"'),
        # plane
        s('path d="M360 92 L440 82 L460 72 L470 78 L456 92 L470 112 L460 116 L436 100 L370 104 Z"', C["white"]),
        s('path d="M400 90 L380 60 L395 58 L425 88 M405 103 L392 124 L404 125 L428 101"', C["white"]),
        # suitcase
        s('rect x="460" y="300" width="70" height="80" rx="8"', C["coral"]),
        s('path d="M480 300 L480 284 L510 284 L510 300 M460 330 L530 330"'),
    ]
    return sh
