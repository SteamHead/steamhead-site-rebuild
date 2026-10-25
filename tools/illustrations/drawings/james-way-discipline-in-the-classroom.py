import math

from pen import C, s

TITLE = "A dial with low, medium and high zones and its needle turned towards the low end"


def shapes():
    cx, cy, R, r = 400, 360, 260, 150

    def arc(a0, a1, col):
        p = lambda rad, a: (cx + rad * math.cos(math.radians(a)), cy - rad * math.sin(math.radians(a)))
        (x0, y0), (x1, y1), (x2, y2), (x3, y3) = p(R, a0), p(R, a1), p(r, a1), p(r, a0)
        return s(f'path d="M{x0:.0f} {y0:.0f} A{R} {R} 0 0 0 {x1:.0f} {y1:.0f} L{x2:.0f} {y2:.0f} A{r} {r} 0 0 1 {x3:.0f} {y3:.0f} Z"', col)

    a = math.radians(140)
    nx, ny = cx + 220 * math.cos(a), cy - 220 * math.sin(a)
    return [
        s('rect x="110" y="70" width="580" height="320" rx="24"', C["white"]),
        arc(120, 180, C["teal"]),   # low: students share the process
        arc(60, 120, C["yellow"]),
        arc(0, 60, C["coral"]),     # high: traditional adult/child roles
        s(f'path d="M{cx + 12 * math.sin(a):.0f} {cy + 12 * math.cos(a):.0f} L{nx:.0f} {ny:.0f} '
          f'L{cx - 12 * math.sin(a):.0f} {cy - 12 * math.cos(a):.0f} Z"', C["dark"]),
        s(f'circle cx="{cx}" cy="{cy}" r="22"', C["dark"]),
    ]
