from pen import C, s

TITLE = "A young plant growing out of a stack of books, reaching towards the sun"


def shapes():
    return [
        s('line x1="20" y1="420" x2="780" y2="420"'),
        # books
        s('rect x="250" y="370" width="300" height="50" rx="6"', C["blue"]),
        s('rect x="275" y="320" width="260" height="50" rx="6"', C["coral"]),
        s('rect x="240" y="270" width="280" height="50" rx="6"', C["yellow"]),
        s('path d="M270 385 h240 M300 335 h200 M265 285 h220"'),
        # plant
        s('path d="M400 270 C400 220 390 170 410 110"'),
        s('path d="M398 220 C350 225 320 195 318 165 C360 160 395 185 398 220 Z"', C["teal"]),
        s('path d="M403 170 C450 172 478 140 476 110 C436 106 405 135 403 170 Z"', C["teal"]),
        s('path d="M410 110 C395 85 400 65 415 50 C430 70 428 90 410 110 Z"', C["teal"]),
        # sun
        s('circle cx="660" cy="100" r="45"', C["amber"]),
        s('path d="M660 30 v-15 M660 170 v15 M590 100 h-15 M730 100 h15 M610 50 l-10 -10 M710 150 l10 10 M710 50 l10 -10 M610 150 l-10 10"'),
    ]
