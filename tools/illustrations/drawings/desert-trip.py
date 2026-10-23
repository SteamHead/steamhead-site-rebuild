from pen import C, s

TITLE = "A small van loaded with a box of electronics driving along a desert road under a big sun"


def shapes():
    return [
        s('circle cx="640" cy="105" r="55"', C["yellow"]),
        s('path d="M0 300 L100 210 L200 300 Z"', C["amber"]),
        s('path d="M500 300 L590 200 L680 300 Z"', C["amber"]),
        s('line x1="0" y1="300" x2="800" y2="300"'),
        s('path d="M0 380 L800 380"'),
        s('path d="M40 340 l60 0 M130 340 l50 0 M540 340 l60 0 M700 340 l60 0"'),
        # cactus
        s('path d="M690 300 L690 200 Q690 185 705 185 Q720 185 720 200 L720 300 Z"', C["teal"]),
        s('path d="M690 250 L668 250 Q660 250 660 240 L660 222"'),
        s('path d="M720 235 L742 235 Q750 235 750 225 L750 208"'),
        # van
        s('path d="M250 345 L250 255 L440 255 L480 295 L480 345 Z"', C["coral"]),
        s('path d="M440 262 L440 295 L472 295"', C["white"]),
        s('circle cx="300" cy="350" r="22"', C["white"]),
        s('circle cx="430" cy="350" r="22"', C["white"]),
        # box of electronics on roof, with a circuit board poking out
        s('rect x="280" y="200" width="130" height="55"', C["amber"]),
        s('rect x="300" y="168" width="70" height="32"', C["teal"]),
        s('path d="M315 184 l15 0 l0 -8 M345 184 l12 0"'),
        s('circle cx="384" cy="160" r="9"', C["yellow"]),
        s('path d="M384 169 l0 20"'),
        s('path d="M230 275 l-60 0 M225 318 l-80 0"'),
    ]
