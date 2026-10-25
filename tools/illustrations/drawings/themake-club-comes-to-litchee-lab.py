from pen import C, s

TITLE = "A makerspace workbench with a pegboard of tools, a small cardboard robot, and a class flyer pinned to the wall"


def shapes():
    sh = [s('rect x="50" y="36" width="400" height="160" rx="6"', C["gray"])]
    sh += [s(f'circle cx="{x}" cy="{y}" r="3"', C["dark"], flat=True)
           for x in range(80, 440, 40) for y in (60, 172)]
    sh += [
        # hammer, screwdriver, ruler on the pegboard
        s('rect x="96" y="80" width="70" height="26" rx="4"', C["dark"]),
        s('rect x="122" y="106" width="18" height="70" rx="4"', C["amber"]),
        s('rect x="214" y="70" width="22" height="50" rx="6"', C["coral"]),
        s('path d="M225 120 L225 176"'),
        s('rect x="290" y="80" width="130" height="34" rx="2"', C["yellow"]),
        s('path d="M310 80 l0 12 M330 80 l0 18 M350 80 l0 12 M370 80 l0 18 M390 80 l0 12"'),
        # robot on the bench
        s('path d="M245 214 L245 196 M245 196 m-8 -8 a8 8 0 1 0 0.1 0"'),
        s('rect x="210" y="214" width="70" height="44" rx="6"', C["teal"]),
        s('circle cx="231" cy="236" r="6"', C["black"], flat=True),
        s('circle cx="259" cy="236" r="6"', C["black"], flat=True),
        s('rect x="196" y="262" width="98" height="64" rx="6"', C["teal"]),
        s('path d="M196 286 L168 304 M294 286 L322 304"'),
        # workbench
        s('rect x="40" y="326" width="520" height="24" rx="4"', C["amber"]),
        s('path d="M70 350 L70 440 M530 350 L530 440"'),
        # flyer with a light bulb
        s('rect x="590" y="56" width="170" height="240" rx="4"', C["white"]),
        s('rect x="650" y="44" width="50" height="20" rx="2"', C["amber"]),
        s('circle cx="675" cy="136" r="38"', C["yellow"]),
        s('rect x="658" y="172" width="34" height="22" rx="3"', C["gray"]),
        s('path d="M612 226 l126 0 M612 250 l100 0 M612 274 l116 0"'),
    ]
    return sh
