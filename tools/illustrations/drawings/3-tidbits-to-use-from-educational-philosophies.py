from pen import C, s

TITLE = "A fruit tree, a pair of pruning shears and a basket holding three picked fruits"


def shapes():
    sh = [
        # tree
        s('path d="M180 420 L195 250 L220 250 L238 420 Z"', C["amber"]),
        s('circle cx="205" cy="170" r="120"', C["teal"]),
        s('path d="M205 250 L160 200 M210 240 L255 195"'),
    ]
    for x, y, col in ((140, 130, C["coral"]), (250, 110, C["yellow"]), (190, 205, C["coral"]),
                      (275, 200, C["yellow"]), (120, 210, C["yellow"])):
        sh.append(s(f'circle cx="{x}" cy="{y}" r="16"', col))
    sh += [
        s('line x1="20" y1="420" x2="780" y2="420"'),
        # basket with three fruits
        s('circle cx="520" cy="320" r="26"', C["coral"]),
        s('circle cx="575" cy="312" r="26"', C["yellow"]),
        s('circle cx="630" cy="320" r="26"', C["coral"]),
        s('path d="M470 330 L680 330 L655 415 L495 415 Z"', C["amber"]),
        s('path d="M490 360 L665 360 M500 390 L660 390 M535 330 L540 415 M575 330 L575 415 M615 330 L610 415"'),
        s('path d="M490 330 C490 230 660 230 660 330" '),
        # pruning shears
        # pruning shears: curved blades meeting at a pivot, red handles below
        s('path d="M655 190 C630 160 615 120 618 70 C640 100 660 140 668 180 Z"', C["gray"]),
        s('path d="M655 190 C680 160 700 125 705 85 C680 110 660 150 645 182 Z"', C["gray"]),
        s('path d="M648 200 C630 230 610 255 598 285 C592 300 608 306 616 294 C632 268 650 240 662 205 Z"', C["coral"]),
        s('path d="M662 200 C682 228 700 252 714 282 C720 298 704 304 696 292 C680 266 664 238 650 205 Z"', C["coral"]),
        s('circle cx="655" cy="194" r="8"', C["white"]),
    ]
    return sh
