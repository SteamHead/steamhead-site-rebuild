from pen import C, s

TITLE = "Two classroom floor plans: desks in rows facing the teacher, and desks pushed into small groups"


def shapes():
    sh = [
        s('rect x="40" y="35" width="320" height="380" rx="14"', C["white"]),
        s('rect x="440" y="35" width="320" height="380" rx="14"', C["white"]),
        s('rect x="80" y="55" width="240" height="14" rx="4"', C["teal"]),
        s('rect x="480" y="55" width="240" height="14" rx="4"', C["teal"]),
        s('rect x="160" y="92" width="80" height="30" rx="4"', C["coral"]),
        s('path d="M378 225 L422 225 M408 211 L422 225 L408 239"'),
    ]
    for ry in (165, 245, 325):  # rows: everyone faces the front
        for dx in (68, 138, 208, 278):
            sh += [s(f'rect x="{dx}" y="{ry}" width="54" height="32" rx="4"', C["yellow"]),
                   s(f'circle cx="{dx+27}" cy="{ry+48}" r="10"', C["gray"])]
    for (cx, cy), col in zip(((540, 190), (680, 190), (610, 320)), (C["yellow"], C["blue"], C["amber"])):
        for ox, oy in ((-50, -32), (0, -32), (-50, 0), (0, 0)):  # pods: four desks face each other
            sh.append(s(f'rect x="{cx+ox}" y="{cy+oy}" width="50" height="32" rx="4"', col))
        for ox, oy in ((-25, -46), (25, -46), (-25, 46), (25, 46)):
            sh.append(s(f'circle cx="{cx+ox}" cy="{cy+oy}" r="10"', C["gray"]))
    sh += [s('path d="M565 105 q10 -16 28 -10 q18 -6 22 10 q2 14 -16 16 l-8 10 l-2 -10 q-22 0 -24 -16 Z"', C["white"])]
    return sh

