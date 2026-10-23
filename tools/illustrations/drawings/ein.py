from pen import C, s

TITLE = "Teachers seen from behind watching a presentation, with two speech bubbles for a two-language meetup"


def shapes():
    sh = [
        s('rect x="230" y="50" width="340" height="200" rx="8"', C["white"]),
        s('path d="M270 210 L270 150 M320 210 L320 120 M370 210 L370 170 M420 210 L420 100"'),
        s('rect x="460" y="90" width="80" height="60" rx="4"', C["yellow"]),
        s('path d="M400 250 L400 280"'),
        # speech bubbles
        s('path d="M60 70 h110 a16 16 0 0 1 16 16 v44 a16 16 0 0 1 -16 16 h-60 l-22 22 l0 -22 h-28 a16 16 0 0 1 -16 -16 v-44 a16 16 0 0 1 16 -16 Z"', C["teal"]),
        s('path d="M80 100 l70 0 M80 120 l45 0"'),
        s('path d="M630 110 h110 a16 16 0 0 1 16 16 v44 a16 16 0 0 1 -16 16 h-28 l0 22 l-22 -22 h-60 a16 16 0 0 1 -16 -16 v-44 a16 16 0 0 1 16 -16 Z"', C["coral"]),
        s('path d="M650 140 l70 0 M650 160 l45 0"'),
    ]
    for x, col in ((150, C["blue"]), (290, C["amber"]), (430, C["teal"]), (570, C["coral"]), (700, C["yellow"])):
        sh += [s(f'path d="M{x-55} 450 C{x-55} 380 {x+55} 380 {x+55} 450"', col),
               s(f'circle cx="{x}" cy="340" r="36"', C["dark"])]
    return sh
