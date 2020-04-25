from Geothon import *

a = point('a')
assert(a.name == 'a')
assert(a in allPoints())

b = point('a')
assert(b is a )

assert(a.isConsolidate() == False)
assert(a.x == None)
assert(a.y == None)
a.consolidate()
assert(a.x != None)
assert(a.y != None)

c = point('c')
assert(c.distanceTo(a) > 0)
