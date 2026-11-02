from pen import C, s

TITLE = "A cardboard box hung above a stage, its trapdoor swung open by a servo, letting paper snow fall"


def shapes():
    sh = [
        # stage floor and curtains
        s('rect x="-10" y="390" width="820" height="70"', C["gray"]),
        s('path d="M-10 -10 L130 -10 Q95 200 150 395 L-10 395 Z"', C["coral"]),
        s('path d="M810 -10 L670 -10 Q705 200 650 395 L810 395 Z"', C["coral"]),
        # hanging strings and the box
        s('path d="M310 0 L310 70 M490 0 L490 70"'),
        s('rect x="270" y="70" width="260" height="90" rx="4"', C["amber"]),
        s('path d="M300 100 l40 0 M460 130 l40 0"'),
        # trapdoor hinged at the left, swung open at an angle
        s('path d="M270 160 L282 158 L380 232 L370 242 Z"', C["amber"]),
        s('circle cx="274" cy="160" r="5"', C["dark"]),
        # servo on the side, wire running off to the controller
        s('rect x="530" y="92" width="44" height="34" rx="4"', C["blue"]),
        s('path d="M574 109 Q620 109 640 60 Q650 30 670 20"'),
    ]
    flakes = [(430, 200), (470, 245), (410, 285), (500, 300), (450, 340), (390, 360),
              (520, 360), (480, 200), (360, 320), (540, 250)]
    for i, (x, y) in enumerate(flakes):
        if i % 3 == 0:
            sh.append(s(f'path d="M{x-11} {y} l22 0 M{x-6} {y-10} l12 20 M{x+6} {y-10} l-12 20"'))
        else:
            sh.append(s(f'circle cx="{x}" cy="{y}" r="{9 + i % 2 * 3}"', C["white"]))
    return sh
