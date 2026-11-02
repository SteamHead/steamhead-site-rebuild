from pen import C, s

TITLE = "A tower of wooden building blocks being stacked, next to a magnifying glass and a sprouting seedling"


def shapes():
    blocks = [(260, 340, 120, 70, C["yellow"]), (390, 340, 120, 70, C["teal"]),
              (320, 260, 120, 70, C["coral"]), (330, 180, 70, 70, C["blue"])]
    sh = [s('line x1="20" y1="410" x2="780" y2="410"')]
    for x, y, w, h, col in blocks:
        sh.append(s(f'rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4"', col))
    sh += [
        # block on its way to the top
        s('path d="M430 70 L500 70 L500 140 L430 140 Z" transform="rotate(12 465 105)"', C["amber"]),
        s('path d="M410 150 C400 170 400 175 395 178" stroke-dasharray="8 8"'),
        # magnifying glass
        s('path d="M140 330 L70 400 L86 414 L156 344 Z"', C["dark"]),
        s('circle cx="185" cy="295" r="55"', C["white"]),
        # seedling in a pot
        s('path d="M610 330 L700 330 L688 410 L622 410 Z"', C["coral"]),
        s('path d="M655 330 L655 250"'),
        s('path d="M655 280 C620 280 600 255 605 230 C635 228 655 250 655 280 Z"', C["teal"]),
        s('path d="M655 265 C690 265 712 240 708 212 C678 210 655 235 655 265 Z"', C["teal"]),
    ]
    return sh
