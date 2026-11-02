from pen import C, s

TITLE = "Three maker badges with ribbons, showing a lightning bolt, a light bulb and a hammer"


def badge(cx, col, icon):
    return [
        s(f'path d="M{cx-35} 250 L{cx-55} 380 L{cx-25} 360 L{cx-10} 395 L{cx+5} 260 Z"', C["coral"]),
        s(f'path d="M{cx+35} 250 L{cx+55} 380 L{cx+25} 360 L{cx+10} 395 L{cx-5} 260 Z"', C["coral"]),
        s(f'circle cx="{cx}" cy="190" r="95"', col),
        s(f'circle cx="{cx}" cy="190" r="72"', C["white"]),
    ] + icon


def shapes():
    bolt = [s('path d="M158 130 L128 200 L156 200 L140 252 L190 175 L160 175 L178 130 Z"', C["yellow"])]
    bulb = [s('path d="M380 205 a38 38 0 1 1 40 0 q-6 8 -6 20 l-28 0 q0 -12 -6 -20 Z"', C["yellow"]),
            s('rect x="386" y="227" width="28" height="16" rx="4"', C["gray"])]
    hammer = [s('rect x="605" y="140" width="80" height="32" rx="5"', C["gray"]),
              s('rect x="634" y="172" width="20" height="80" rx="6"', C["amber"])]
    return badge(160, C["teal"], bolt) + badge(400, C["yellow"], bulb) + badge(640, C["blue"], hammer)
