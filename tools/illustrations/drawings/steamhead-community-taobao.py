from pen import C, s

TITLE = "A student-made light-up project leaving a cardboard shipping box, beside a phone showing it listed in an online shop"


def glow(cx, cy, r):
    rays = " ".join(f"M{cx + dx * (r + 10)} {cy + dy * (r + 10)} l{dx * 18} {dy * 18}"
                    for dx, dy in ((1, 0), (-1, 0), (0, -1), (0.7, -0.7), (-0.7, -0.7)))
    return [s(f'circle cx="{cx}" cy="{cy}" r="{r}"', C["yellow"]),
            s(f'circle cx="{cx}" cy="{cy}" r="{r // 3}"', C["white"]),
            s(f'path d="{rays}"')]


def shapes():
    return [
        # open box with the project rising out of it
        *glow(230, 158, 42),
        s('path d="M110 240 L170 240 L130 204 L70 204 Z"', C["amber"]),
        s('path d="M290 240 L350 240 L410 204 L350 204 Z"', C["amber"]),
        s('rect x="110" y="240" width="240" height="150"', C["amber"]),
        s('rect x="140" y="300" width="80" height="50" rx="4"', C["white"]),
        s('path d="M152 318 l56 0 M152 334 l36 0"'),
        # arrow to the phone
        s('path d="M372 310 Q430 310 462 262 M446 266 L462 262 L466 279"'),
        # phone with a product listing
        s('rect x="490" y="30" width="200" height="390" rx="26"', C["gray"]),
        s('rect x="508" y="70" width="164" height="310" rx="6"', C["white"]),
        s('rect x="522" y="84" width="136" height="120" rx="4"', C["teal"]),
        *glow(590, 144, 28),
        s('path d="M524 228 l120 0 M524 252 l90 0 M524 276 l104 0"'),
        s('rect x="524" y="318" width="132" height="40" rx="20"', C["coral"]),
    ]
