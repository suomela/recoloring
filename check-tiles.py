#!/usr/bin/env python3

import itertools

colours = [1, 2, 3, 4]


def good_tile(x):
    a,b,c,\
    d,e,f,\
    g,h,i = x
    return a != b != c and \
           d != e != f and \
           g != h != i and \
           a != d != g and \
           b != e != h and \
           c != f != i

def parts(x):
    a,b,c,\
    d,e,f,\
    g,h,i = x
    return [
        (a,b,
         d,e),
        (b,c,
         e,f),
        (d,e,
         g,h),
        (e,f,
         h,i)
    ]

def type(x):
    if x in [
        (1,3,3,2),
        (2,3,3,1),
    ]:
        return "A"
    elif x in [
        (1,3,4,2),
        (2,1,1,4),
        (2,1,3,4),
        (2,3,1,4),
        (2,3,3,4),
        (2,3,4,1),
        (3,1,1,4),
        (3,2,1,4),
        (4,1,1,2),
        (4,1,1,3),
        (4,1,3,2),
        (4,2,1,3),
        (4,3,1,2),
        (4,3,3,2),
    ]:
        return "B"
    else:
        return "-"

def main():
    tiles = 0
    pairs = 0
    for x in itertools.product(colours, repeat=9):
        if not good_tile(x):
            continue
        tiles += 1
        a,b,c,\
        d,e,f,\
        g,h,i = x
        for E in colours:
            y = a,b,c,\
                d,E,f,\
                g,h,i
            if x >= y:
                continue
            if not good_tile(y):
                continue
            pairs += 1

            tx = [ type(p) for p in parts(x) ]
            ty = [ type(p) for p in parts(y) ]

            p = """
{a} {b} {c}    {a} {b} {c}  |  {x1} {x2}    {y1} {y2}
{d} {e} {f} -> {d} {E} {f}  |  {sp} {sp} -> {sp} {sp}
{g} {h} {i}    {g} {h} {i}  |  {x3} {x4}    {y3} {y4}"""

            print(p.format(
                sp=" ",
                a=a, b=b, c=c, d=d, e=e, E=E, f=f, g=g, h=h, i=i,
                x1=tx[0], x2=tx[1], x3=tx[2], x4=tx[3],
                y1=ty[0], y2=ty[1], y3=ty[2], y4=ty[3],
            ))

            xa = len([t for t in tx if t == 'A'])
            xb = len([t for t in tx if t == 'B'])
            ya = len([t for t in ty if t == 'A'])
            yb = len([t for t in ty if t == 'B'])
            da = ya - xa
            db = yb - xb
            ea = da % 2 == 0
            eb = db % 2 == 0
            assert ea == eb

    print("\nChecked {} tiles, {} pairs.\n".format(tiles, pairs))

main()

