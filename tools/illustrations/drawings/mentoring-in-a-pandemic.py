from pen import C, s

TITLE = "A laptop showing a video call with four people, beside a wifi signal and a life ring"


def shapes():
    sh = [
        s('rect x="170" y="58" width="460" height="292" rx="14"', C["dark"]),
        s('path d="M130 350 H670 L700 390 H100 Z"', C["gray"]),
    ]
    for (tx, ty), col in zip(((193, 82), (412, 82), (193, 218), (412, 218)), (C["teal"], C["yellow"], C["coral"], C["blue"])):
        sh += [
            s(f'rect x="{tx}" y="{ty}" width="195" height="112" rx="6"', col),
            s(f'circle cx="{tx+97}" cy="{ty+44}" r="20"', C["white"]),
            s(f'path d="M{tx+60} {ty+112} Q{tx+97} {ty+62} {tx+134} {ty+112}"', C["white"]),
        ]
    sh += [
        # wifi
        s('path d="M678 104 Q720 64 762 104 M692 120 Q720 94 748 120"'),
        s('circle cx="720" cy="138" r="7"', C["black"], flat=True),
        # life ring: support
        s('circle cx="90" cy="250" r="52"', C["coral"]),
        s('circle cx="90" cy="250" r="24"', C["mint"]),
    ]
    sh.append(s('path d="M107 233 L127 213 M73 233 L53 213 M73 267 L53 287 M107 267 L127 287"'))
    return sh
