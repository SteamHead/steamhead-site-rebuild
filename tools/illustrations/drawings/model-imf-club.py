from pen import C, s

TITLE = "A globe on a stand between two stacks of coins, with speech bubbles for a debate"


def coins(x, n, colour):
    return [s(f'rect x="{x}" y="{360 - 22 * (i + 1)}" width="110" height="22" rx="8"', colour) for i in range(n)]


def bubble(x, y, tail):
    return s(f'path d="M{x} {y} h120 q14 0 14 14 v52 q0 14 -14 14 h-{60 - tail} l-18 22 l2 -22 h-{42 + tail} q-14 0 -14 -14 v-52 q0 -14 14 -14 Z"', C["white"])


def shapes():
    return [
        *coins(110, 5, C["yellow"]), *coins(580, 3, C["amber"]),
        s('line x1="60" y1="360" x2="740" y2="360"'),
        # globe on a stand
        s('path d="M400 330 L400 352"'),
        s('rect x="345" y="352" width="110" height="14" rx="4"', C["dark"]),
        s('circle cx="400" cy="200" r="120"', C["teal"]),
        s('ellipse cx="400" cy="200" rx="55" ry="120"'),
        s('path d="M400 80 L400 320 M280 200 L520 200 M296 140 L504 140 M296 260 L504 260"'),
        # speech bubbles above the coin stacks
        bubble(110, 90, 0), bubble(590, 160, 0),
        s('path d="M130 120 l90 0 M130 142 l60 0 M610 190 l90 0 M610 212 l70 0"'),
    ]
