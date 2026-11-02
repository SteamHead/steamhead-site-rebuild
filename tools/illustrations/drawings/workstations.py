from pen import C, s

TITLE = "A classroom seen from above, with four work stations for brainstorming, storyboarding, building and presenting, linked by arrows in a loop"


def table(cx, cy, colour):
    return s(f'rect x="{cx-80}" y="{cy-45}" width="160" height="90" rx="8"', colour)


def shapes():
    sh = [
        s('rect x="30" y="20" width="740" height="410" rx="16"', C["white"]),
        table(190, 120, C["yellow"]), table(610, 120, C["teal"]),
        table(610, 330, C["coral"]), table(190, 330, C["blue"]),
        # brainstorm: sticky notes
        s('rect x="140" y="95" width="32" height="32" transform="rotate(-8 156 111)"', C["white"]),
        s('rect x="180" y="90" width="32" height="32" transform="rotate(6 196 106)"', C["white"]),
        s('rect x="210" y="118" width="32" height="32" transform="rotate(-4 226 134)"', C["white"]),
        # storyboard: three frames
        *[s(f'rect x="{x}" y="104" width="38" height="30" rx="2"', C["white"]) for x in (548, 591, 634)],
        s('path d="M560 124 l8 -10 l8 10 M603 126 a6 6 0 1 0 12 0 M646 116 l14 0"'),
        # build: a stacked cardboard prototype
        s('rect x="570" y="340" width="80" height="26" rx="2"', C["white"]),
        s('rect x="584" y="314" width="52" height="26" rx="2"', C["white"]),
        s('path d="M584 314 L610 292 L636 314"', C["white"]),
        # present: screen on a stand
        s('rect x="140" y="300" width="100" height="58" rx="4"', C["white"]),
        s('path d="M160 340 l18 -18 l14 12 l22 -20"'),
        # loop arrows between stations
        s('path d="M285 100 Q400 60 515 100 M500 88 L515 100 L499 110"'),
        s('path d="M700 175 Q730 225 700 275 M688 262 L700 275 L712 262"'),
        s('path d="M515 350 Q400 390 285 350 M300 362 L285 350 L301 340"'),
        s('path d="M100 275 Q70 225 100 175 M88 188 L100 175 L112 188"'),
    ]
    return sh
