from pen import C, s

TITLE = "An old website window packed into a cardboard moving box, with an arrow pointing to a fresh new website window"


def shapes():
    return [
        # old window sticking out of a box
        s('rect x="110" y="110" width="200" height="140" rx="8"', C["white"]),
        s('path d="M110 140 L310 140"'),
        s('rect x="110" y="110" width="200" height="30" rx="8"', C["gray"]),
        s('path d="M135 170 l100 0 M135 195 l140 0"'),
        s('path d="M70 230 L350 230 L350 400 L70 400 Z"', C["amber"]),
        s('path d="M70 230 L30 280 M350 230 L390 280"'),
        s('path d="M180 230 l0 45 l60 0 l0 -45"'),
        # arrow
        s('path d="M410 260 L500 260 M478 238 L500 260 L478 282"'),
        # new window
        s('rect x="530" y="120" width="230" height="250" rx="10"', C["white"]),
        s('rect x="530" y="120" width="230" height="34" rx="10"', C["teal"]),
        s('circle cx="552" cy="137" r="5"', C["white"]),
        s('circle cx="572" cy="137" r="5"', C["white"]),
        s('rect x="555" y="175" width="180" height="80" rx="4"', C["yellow"]),
        s('path d="M555 285 l180 0 M555 310 l140 0 M555 335 l160 0"'),
        s('path d="M590 70 l0 -18 M640 60 l10 -16 M690 70 l14 -12"'),
    ]
