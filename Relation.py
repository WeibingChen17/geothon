from Geothon import *

def concyclic(*args):
    return True
    if len(args) <= 3:
        return True
    c = circle('tmp').fromThreePoints(args[0], args[1], args[2])
    c.consolidate()
    print(c)
    print(args)
    for p in args[0:]:
        print(p)
        print(p in c)
    # return all([(p in c) for p in args[3:]])
