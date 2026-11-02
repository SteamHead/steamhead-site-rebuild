from pen import C, s

TITLE = "A lottery drum of coloured balls sending one ball down a chute towards a school"


def shapes():
    sh = [
        s('path d="M170 312 L140 410 M290 312 L320 410 M110 410 H350"'),
        s('circle cx="230" cy="200" r="120"', C["white"]),
        s('path d="M350 200 H392 V244"'),
    ]
    for (x, y), col in zip(((180, 230), (230, 260), (280, 228), (205, 180), (262, 170), (160, 270), (232, 120)),
                           (C["yellow"], C["coral"], C["teal"], C["blue"], C["yellow"], C["teal"], C["coral"])):
        sh.append(s(f'circle cx="{x}" cy="{y}" r="22"', col))
    sh += [
        s('path d="M300 300 L560 395 M312 276 L560 367"'),
        s('circle cx="430" cy="324" r="20"', C["coral"]),
        s('rect x="560" y="232" width="200" height="178"', C["teal"]),
        s('path d="M540 237 L660 152 L780 237 Z"', C["yellow"]),
        s('rect x="640" y="340" width="40" height="70"', C["white"]),
        s('rect x="590" y="262" width="40" height="36"', C["white"]),
        s('rect x="690" y="262" width="40" height="36"', C["white"]),
    ]
    return sh
