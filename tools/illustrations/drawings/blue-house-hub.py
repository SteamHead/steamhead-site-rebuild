from pen import C, s

TITLE = "A small blue house with a big workshop door, alone in a wide desert with mountains and a setting sun"


def shapes():
    return [
        s('circle cx="560" cy="105" r="50"', C["yellow"]),
        s('path d="M420 270 L520 180 L600 240 L680 170 L800 270 Z"', C["amber"]),
        s('path d="M0 270 L800 270"'),
        # house
        s('path d="M150 330 L150 220 L240 160 L330 220 L330 330 Z"', C["blue"]),
        s('rect x="180" y="250" width="80" height="80"', C["white"]),
        s('path d="M180 270 L260 270 M180 290 L260 290 M180 310 L260 310"'),
        s('rect x="280" y="240" width="30" height="30"', C["yellow"]),
        s('path d="M120 330 L360 330"'),
        # cacti and space
        s('path d="M470 330 L470 270 Q470 258 482 258 Q494 258 494 270 L494 330 Z"', C["teal"]),
        s('path d="M470 300 L455 300 L455 282"'),
        s('path d="M60 390 l50 0 M200 410 l70 0 M420 395 l60 0 M600 410 l80 0"'),
        s('path d="M90 80 l12 0 M96 74 l0 12 M380 60 l12 0 M386 54 l0 12"'),
    ]
