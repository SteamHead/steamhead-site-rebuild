from pen import C, s

TITLE = "A video camera on a tripod recording two chairs set up for a conversation, with speech bubbles above"


def shapes():
    return [
        # camera and tripod
        s('path d="M145 240 V282 M145 282 L95 412 M145 282 L195 412 M145 282 V412"'),
        s('rect x="70" y="150" width="150" height="90" rx="10"', C["dark"]),
        s('rect x="220" y="170" width="48" height="50" rx="4"', C["gray"]),
        s('circle cx="96" cy="172" r="9"', C["coral"]),
        s('path d="M278 178 L398 128 M278 212 L398 292"', None, 'stroke-dasharray="10 10"'),
        # two chairs facing each other
        s('rect x="420" y="190" width="18" height="112"', C["yellow"]),
        s('rect x="420" y="300" width="92" height="18"', C["yellow"]),
        s('path d="M428 318 V412 M502 318 V412"'),
        s('rect x="680" y="190" width="18" height="112"', C["yellow"]),
        s('rect x="606" y="300" width="92" height="18"', C["yellow"]),
        s('path d="M616 318 V412 M690 318 V412"'),
        # the conversation
        s('path d="M470 82 Q470 52 520 52 Q570 52 570 82 Q570 112 520 112 L498 132 L502 110 Q470 104 470 82 Z"', C["white"]),
        s('path d="M600 112 Q600 82 650 82 Q700 82 700 112 Q700 142 650 142 L628 162 L632 140 Q600 134 600 112 Z"', C["teal"]),
        s('path d="M376 412 H740"'),
    ]
