from pen import C, s

TITLE = "Three overlapping circles, each holding a symbol of learning: a book, a light and a pencil"


def shapes():
    return [
        s('circle cx="320" cy="175" r="120" fill-opacity="0.6"', C["teal"]),
        s('circle cx="480" cy="175" r="120" fill-opacity="0.6"', C["yellow"]),
        s('circle cx="400" cy="300" r="120" fill-opacity="0.6"', C["coral"]),
        # book
        s('path d="M268 138 C253 131 233 131 223 136 V173 C233 168 253 168 268 175 Z"', C["white"]),
        s('path d="M268 138 C283 131 303 131 313 136 V173 C303 168 283 168 268 175 Z"', C["white"]),
        # light (LED)
        s('path d="M518 168 V146 A16 16 0 0 1 550 146 V168 Z"', C["white"]),
        s('path d="M527 168 V196 M541 168 V188 M534 104 V92 M562 118 l9 -9 M506 118 l-9 -9"'),
        # pencil
        s('path d="M350 352 H428 L452 362 L428 372 H350 Z"', C["amber"]),
        s('rect x="334" y="352" width="16" height="20"', C["white"]),
        s('circle cx="400" cy="216" r="9"', C["black"], flat=True),
    ]
