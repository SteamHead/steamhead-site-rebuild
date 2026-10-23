from pen import C, s

TITLE = "A video player showing a student's landscape photo with a review comment beside it, and a camera"


def shapes():
    return [
        # video player with a photo on screen
        s('rect x="90" y="40" width="480" height="320" rx="12"', C["dark"]),
        s('rect x="120" y="66" width="420" height="230"', C["teal"]),
        s('circle cx="470" cy="118" r="28"', C["yellow"]),
        s('path d="M120 296 L230 170 L300 240 L380 140 L540 296 Z"', C["white"]),
        # timeline with the scrubber partway along
        s('rect x="120" y="322" width="420" height="12" rx="6"', C["gray"]),
        s('rect x="120" y="322" width="200" height="12" rx="6"', C["coral"]),
        s('circle cx="320" cy="328" r="12"', C["coral"]),
        # review comment
        s('path d="M610 50 L760 50 Q772 50 772 62 L772 140 Q772 152 760 152 L650 152 L620 178 L628 152 L610 152 Q598 152 598 140 L598 62 Q598 50 610 50 Z"', C["white"]),
        s('path d="M620 80 l120 0 M620 104 l130 0 M620 128 l80 0"'),
        # camera
        s('rect x="630" y="232" width="56" height="26" rx="4"', C["gray"]),
        s('rect x="600" y="252" width="170" height="120" rx="14"', C["blue"]),
        s('circle cx="685" cy="312" r="40"', C["white"]),
        s('circle cx="685" cy="312" r="20"', C["gray"]),
    ]
