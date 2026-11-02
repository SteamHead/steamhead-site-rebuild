from pen import C, s

TITLE = "A small guest room with a made bed, a desk lamp, a window and a suitcase ready for a visiting maker"


def shapes():
    return [
        s('line x1="20" y1="390" x2="780" y2="390"'),
        # window
        s('rect x="330" y="60" width="160" height="130" rx="6"', C["blue"]),
        s('path d="M410 60 L410 190 M330 125 L490 125"'),
        # bed
        s('rect x="60" y="270" width="280" height="70" rx="8"', C["coral"]),
        s('rect x="60" y="210" width="20" height="180"', C["amber"]),
        s('rect x="90" y="235" width="80" height="35" rx="12"', C["white"]),
        s('path d="M80 340 L80 390 M330 340 L330 390"'),
        # desk + lamp
        s('rect x="520" y="250" width="200" height="22"', C["amber"]),
        s('path d="M540 272 L540 390 M700 272 L700 390"'),
        s('path d="M600 250 L600 180 L640 150"'),
        s('path d="M620 160 L670 125 L690 160 Z"', C["yellow"]),
        s('rect x="560" y="236" width="40" height="14"', C["white"]),
        # suitcase
        s('rect x="400" y="300" width="90" height="90" rx="8"', C["teal"]),
        s('path d="M425 300 L425 282 L465 282 L465 300"'),
        s('path d="M420 330 L470 330"'),
    ]
