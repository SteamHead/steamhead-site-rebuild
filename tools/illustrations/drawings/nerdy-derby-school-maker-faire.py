import math

from pen import C, s

TITLE = "Two homemade derby cars racing down a long wooden track towards a chequered flag"


def shapes():
    k = (330 - 110) / (700 - 30)
    ang = math.degrees(math.atan(k))
    def y_at(x): return 110 + (x - 30) * k
    sh = [
        s('line x1="20" y1="420" x2="790" y2="420"'),
        *[s(f'line x1="{x}" y1="{y_at(x)+30:.0f}" x2="{x}" y2="420"') for x in (140, 330, 520)],
        s('path d="M30 110 L700 330 L790 330 L790 360 L700 360 L30 140 Z"', C["gray"]),
        # finish flag
        s('line x1="716" y1="330" x2="716" y2="196"'),
        s('rect x="716" y="196" width="72" height="54"', C["white"]),
        *[s(f'rect x="{716+c*18}" y="{196+r*18}" width="18" height="18"', "#000", flat=True)
          for r in range(3) for c in range(4) if (r + c) % 2 == 0],
        s('rect x="716" y="196" width="72" height="54"'),
    ]

    def car(x, body, deco):
        t = f'translate({x} {y_at(x):.1f}) rotate({ang:.2f})'
        return [
            s(f'path transform="{t}" d="M-50 -14 L-50 -38 L-10 -38 L5 -52 L35 -52 L50 -38 L50 -14 Z"', body),
            s(f'path transform="{t}" d="{deco}"'),
            s(f'circle transform="{t}" cx="-30" cy="-13" r="13"', C["white"]),
            s(f'circle transform="{t}" cx="30" cy="-13" r="13"', C["white"]),
            s(f'path transform="{t}" d="M-75 -40 l-40 0 M-70 -26 l-55 0"'),
        ]
    sh += car(250, C["yellow"], "M-30 -32 L-12 -32 L-22 -22 L-4 -22")
    sh += car(480, C["coral"], "M10 -46 L30 -46 M-40 -30 L-5 -30")
    return sh

