import math

from pen import C, s

TITLE = "Two meshing gears beside a new website in a browser window, with a gear at its centre"


def gear(cx, cy, r_out, r_in, teeth, phase=0.0):
    pts = []
    step = 2 * math.pi / teeth
    for i in range(teeth):
        a = i * step + phase
        for frac, r in ((0.0, r_in), (0.12, r_out), (0.45, r_out), (0.57, r_in)):
            ang = a + frac * step
            pts.append(f"{cx + r * math.cos(ang):.1f} {cy + r * math.sin(ang):.1f}")
    return "M" + " L".join(pts) + " Z"


def shapes():
    return [
        # two gears meshing
        s(f'path d="{gear(165, 270, 92, 74, 11)}"', C["teal"]),
        s('circle cx="165" cy="270" r="24"', C["white"]),
        s(f'path d="{gear(242, 167, 52, 38, 7, 0.35)}"', C["coral"]),
        s('circle cx="242" cy="167" r="14"', C["white"]),
        # browser window with the new site
        s('rect x="350" y="50" width="410" height="330" rx="14"', C["white"]),
        s('path d="M350 100 L760 100"'),
        *[s(f'circle cx="{x}" cy="75" r="8"', C["gray"]) for x in (378, 404, 430)],
        s('rect x="456" y="64" width="280" height="22" rx="11"', C["gray"]),
        s(f'path d="{gear(555, 240, 100, 82, 12)}"', C["yellow"]),
        s('circle cx="555" cy="240" r="30"', C["white"]),
    ]
