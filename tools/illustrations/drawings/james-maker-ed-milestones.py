from pen import C, s

TITLE = "A winding path with four milestones: a speech bubble, a battery, an envelope and a glowing light bulb"


def shapes():
    return [
        s('path d="M40 380 C180 380 160 230 300 230 C440 230 400 330 540 330 C640 330 680 230 740 230"', None, 'stroke-dasharray="14 12"'),
        # 1: speech bubble (English class)
        s('circle cx="110" cy="368" r="14"', C["white"]),
        s('path d="M60 200 h120 a18 18 0 0 1 18 18 v50 a18 18 0 0 1 -18 18 h-70 l-25 25 l0 -25 h-25 a18 18 0 0 1 -18 -18 v-50 a18 18 0 0 1 18 -18 Z"', C["teal"]),
        s('path d="M80 235 l80 0 M80 260 l55 0"'),
        # 2: 9-volt battery (weekend maker project)
        s('circle cx="300" cy="230" r="14"', C["white"]),
        s('rect x="265" y="80" width="70" height="105" rx="8"', C["coral"]),
        s('rect x="275" y="62" width="18" height="18"', C["gray"]),
        s('rect x="307" y="62" width="18" height="18"', C["gray"]),
        s('path d="M280 120 l40 0 M300 110 l0 20"'),
        # 3: envelope (email)
        s('circle cx="540" cy="330" r="14"', C["white"]),
        s('rect x="480" y="200" width="120" height="80" rx="6"', C["white"]),
        s('path d="M480 206 L540 248 L600 206"'),
        # 4: light bulb, shining outwards (open maker ed)
        s('circle cx="740" cy="230" r="14"', C["white"]),
        s('path d="M705 130 a45 45 0 1 1 70 0 q-10 12 -10 30 l-50 0 q0 -18 -10 -30 Z"', C["yellow"]),
        s('rect x="717" y="162" width="46" height="24" rx="5"', C["gray"]),
        s('path d="M740 22 l0 -14 M685 45 l-14 -12 M790 45 l8 -8 M662 95 l-18 0"'),
    ]
