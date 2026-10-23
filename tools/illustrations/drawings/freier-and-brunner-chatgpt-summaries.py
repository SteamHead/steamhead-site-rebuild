from pen import C, s

TITLE = "A thick open book with an arrow leading to a short speech bubble of summary lines"


def shapes():
    sh = [
        s('path d="M60 160 L60 365 C100 350 170 352 210 368 C250 352 320 350 360 365 L360 160 Z"', C["teal"]),
        s('path d="M210 150 C170 130 100 130 70 145 L70 345 C100 330 170 330 210 350 Z"', C["white"]),
        s('path d="M210 150 C250 130 320 130 350 145 L350 345 C320 330 250 330 210 350 Z"', C["white"]),
    ]
    for y in range(180, 330, 22):
        sh.append(s(f'path d="M92 {y} L188 {y} M232 {y} L328 {y}"'))
    sh += [
        s('path d="M392 250 L468 250 M452 234 L468 250 L452 266"'),
        s('path d="M524 140 H716 Q740 140 740 164 V266 Q740 290 716 290 H600 L548 338 L562 290 H524 Q500 290 500 266 V164 Q500 140 524 140 Z"', C["yellow"]),
        s('path d="M535 180 H705 M535 215 H680 M535 250 H640"'),
        s('path d="M752 96 l14 0 M759 89 l0 14 M470 120 l12 0 M476 114 l0 12"'),
    ]
    return sh
