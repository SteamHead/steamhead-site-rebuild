from pen import C, s

TITLE = "A student wearing a cardboard VR viewer beside a laptop showing a 3D model of a house"


def shapes():
    sh = [
        # floating virtual building the student "sees"
        s('path d="M360 120 L430 70 L500 120 L500 190 L360 190 Z"', C["yellow"], 'stroke-dasharray="10 9"'),
        s('rect x="415" y="145" width="30" height="45"', None, 'stroke-dasharray="6 6"'),
        s('path d="M330 60 l12 0 M336 54 l0 12 M520 80 l12 0 M526 74 l0 12"'),
        # laptop
        s('rect x="70" y="190" width="250" height="160" rx="10"', C["teal"]),
        s('path d="M45 350 L345 350 L370 385 L20 385 Z"', C["gray"]),
        s('path d="M150 300 L150 255 L195 222 L240 255 L240 300 Z M150 255 L240 255 M110 330 L280 330 M195 222 L195 300"', C["white"]),
        # student: shoulders, head, hair, cardboard viewer, strap, hands, smile
        s('path d="M470 450 C480 360 520 330 600 330 C680 330 720 360 730 450"', C["blue"]),
        s('circle cx="600" cy="230" r="78"', C["white"]),
        s('path d="M524 215 C520 150 560 140 600 140 C650 140 685 160 678 215 C660 180 620 175 600 172 C575 176 545 185 524 215 Z"', C["dark"]),
        s('rect x="515" y="200" width="170" height="64" rx="10"', C["amber"]),
        s('path d="M525 214 L675 214 M560 240 l0 10 M640 240 l0 10"'),
        s('path d="M528 264 q-4 22 16 24 q18 0 14 -24"', C["white"]),
        s('path d="M672 264 q4 22 -16 24 q-18 0 -14 -24"', C["white"]),
        s('path d="M575 285 Q600 302 625 285"'),
    ]
    return sh

