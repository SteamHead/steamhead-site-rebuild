from pen import C, s

TITLE = "A workbench with adapted maker tools: a big push-button switch wired to a light, and a chunky-grip screwdriver"


def shapes():
    return [
        s('rect x="40" y="300" width="720" height="30" rx="4"', C["amber"]),
        s('path d="M90 330 V440 M710 330 V440"'),
        # big accessible switch wired to a light
        s('rect x="100" y="228" width="170" height="72" rx="12"', C["gray"]),
        s('path d="M135 228 Q185 140 235 228 Z"', C["coral"]),
        s('path d="M270 268 C320 268 330 230 378 230"'),
        s('rect x="378" y="198" width="96" height="64" rx="10"', C["teal"]),
        s('circle cx="426" cy="230" r="14"', C["yellow"]),
        s('path d="M426 168 V182 M386 178 l10 10 M466 178 l-10 10"'),
        # chunky-grip screwdriver
        s('rect x="520" y="252" width="132" height="48" rx="24"', C["blue"]),
        s('path d="M552 258 V294 M578 258 V294 M604 258 V294"'),
        s('rect x="652" y="269" width="80" height="14"', C["gray"]),
        s('path d="M732 269 L748 276 L732 283"'),
    ]
