from pen import C, s

TITLE = "Two differently shaped school buildings with arrows passing back and forth between them"


def shapes():
    sh = [
        s('path d="M20 380 H780"'),
        # school one: pitched roof
        s('rect x="60" y="205" width="230" height="175"', C["teal"]),
        s('path d="M42 210 L175 122 L308 210 Z"', C["coral"]),
        s('circle cx="175" cy="172" r="18"', C["white"]),
        s('rect x="85" y="235" width="45" height="40"', C["white"]),
        s('rect x="220" y="235" width="45" height="40"', C["white"]),
        s('rect x="150" y="305" width="50" height="75"', C["white"]),
        # school two: flat roof, taller
        s('rect x="510" y="152" width="240" height="228"', C["yellow"]),
        s('rect x="496" y="134" width="268" height="20"', C["gray"]),
    ]
    for x in (535, 607, 679):
        for y in (180, 248):
            sh.append(s(f'rect x="{x}" y="{y}" width="46" height="44"', C["white"]))
    sh += [
        s('rect x="605" y="318" width="50" height="62"', C["white"]),
        s('path d="M332 232 H468 M452 216 L468 232 L452 248"'),
        s('path d="M468 300 H332 M348 284 L332 300 L348 316"'),
    ]
    return sh
