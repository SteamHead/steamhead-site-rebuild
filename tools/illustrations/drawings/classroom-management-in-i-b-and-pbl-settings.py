from pen import C, s

TITLE = "A signpost with three arrows pointing different ways beside an open toolbox of project tools"


def shapes():
    return [
        s('line x1="20" y1="420" x2="780" y2="420"'),
        # signpost
        s('rect x="240" y="80" width="22" height="340"', C["amber"]),
        s('path d="M262 100 L420 100 L455 130 L420 160 L262 160 Z"', C["teal"]),
        s('path d="M240 180 L90 180 L55 210 L90 240 L240 240 Z"', C["coral"]),
        s('path d="M262 260 L400 260 L435 290 L400 320 L262 320 Z"', C["yellow"]),
        # toolbox
        s('path d="M520 300 L740 300 L740 410 L520 410 Z"', C["blue"]),
        s('path d="M520 300 L560 270 L780 270 L740 300"', C["blue"]),
        s('path d="M600 300 C600 270 660 270 660 300"'),
        # tools sticking out
        s('path d="M560 300 L545 175 L560 172 L575 300"', C["gray"]),
        s('rect x="525" y="150" width="56" height="28" rx="4"', C["dark"]),
        s('rect x="640" y="160" width="26" height="140" rx="3"', C["yellow"]),
        s('path d="M640 180 h12 M640 200 h8 M640 220 h12 M640 240 h8 M640 260 h12 M640 280 h8"'),
        s('path d="M700 300 L700 200 C700 185 720 185 720 200 L720 300"', C["coral"]),
    ]
