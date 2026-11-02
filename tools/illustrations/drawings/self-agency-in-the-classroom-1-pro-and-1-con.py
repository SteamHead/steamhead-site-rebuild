from pen import C, s

TITLE = "A balance scale weighing a key on one side against a tangled ball of string on the other"


def shapes():
    return [
        s('line x1="20" y1="420" x2="780" y2="420"'),
        s('path d="M330 420 L470 420 L430 390 L370 390 Z"', C["amber"]),
        s('rect x="390" y="110" width="20" height="280"', C["amber"]),
        s('path d="M170 134 L630 114 L630 128 L170 148 Z"', C["dark"]),
        s('circle cx="400" cy="130" r="16"', C["yellow"]),
        # pans
        s('path d="M190 140 L130 280 M190 140 L250 280 M610 122 L550 262 M610 122 L670 262"'),
        s('path d="M110 280 L270 280 C260 320 120 320 110 280 Z"', C["gray"]),
        s('path d="M530 262 L690 262 C680 302 540 302 530 262 Z"', C["gray"]),
        # key
        s('circle cx="148" cy="245" r="28"', C["yellow"]),
        s('circle cx="148" cy="245" r="9"', C["white"]),
        s('path d="M176 245 L252 245 M232 245 v18 M248 245 v14"'),
        # tangle
        s('circle cx="610" cy="222" r="40"', C["coral"]),
        s('path d="M575 210 C600 180 650 200 640 235 C630 260 585 250 590 220 C595 195 640 205 625 240 M572 235 C600 250 640 245 650 215"'),
        s('path d="M648 235 C670 250 690 238 712 252"'),
    ]
