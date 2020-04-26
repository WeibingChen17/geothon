from Geothon import *

def concyclic(*args):
    if len(args) <= 3:
        return True
    for p in args:
        p.consolidate()
    c = circle('tmp').setVisible(False).fromThreePoints(args[0], args[1], args[2])
    return all([(p in c) for p in args[3:]])
