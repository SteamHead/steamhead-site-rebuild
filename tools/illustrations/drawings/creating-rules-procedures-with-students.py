from pen import C, s

TITLE = "A chart-paper list of class rules on an easel, with students' raised hands and a marker adding to it"


def shapes():
    sh = [
        # easel legs and board
        s('path d="M296 450 L306 380 M504 450 L494 380 M400 450 L400 380"'),
        s('rect x="270" y="60" width="260" height="320" rx="6"', C["white"]),
        s('rect x="290" y="45" width="220" height="22" rx="6"', C["gray"]),
    ]
    for i, y in enumerate((110, 170, 230, 290)):
        sh += [s(f'rect x="300" y="{y}" width="30" height="30" rx="4"', C["white"]),
               s(f'line x1="350" y1="{y+15}" x2="{500 - (i % 2) * 40}" y2="{y+15}"')]
    sh += [s(f'path d="M306 {y+15} l8 9 l14 -18"') for y in (110, 170, 230)]
    # marker writing the last rule
    sh += [s('path d="M455 320 L540 230 L560 250 L475 340 Z"', C["coral"]),
           s('path d="M455 320 L445 350 L475 340"', C["white"])]
    # raised hands either side
    for cx, col in ((140, C["yellow"]), (650, C["blue"])):
        sh += [s(f'path d="M{cx-30} 450 L{cx-30} 230 L{cx+30} 230 L{cx+30} 450"', col),
               s(f'path d="M{cx-34} 240 C{cx-40} 180 {cx-38} 140 {cx-30} 110 C{cx-26} 98 {cx-14} 100 {cx-14} 115 L{cx-12} 80 '
                 f'C{cx-10} 66 {cx+4} 66 {cx+5} 80 L{cx+6} 75 C{cx+8} 62 {cx+22} 62 {cx+22} 78 L{cx+24} 95 '
                 f'C{cx+26} 84 {cx+40} 84 {cx+40} 98 L{cx+38} 180 C{cx+38} 210 {cx+34} 230 {cx+34} 240 Z"', C["white"])]
    return sh
