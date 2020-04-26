from Geothon import *

def concyclic(*args):
    if len(args) <= 3:
        return True
    for p in args:
        p.consolidate()
    x, y, r = getACirleFromThreePoint(args[0], args[1], args[2])
    c = point('').setVisible(False).setX(x).setY(y).setConsolidate()
    return all([p.distanceTo(c) == r for p in args[3:]])
