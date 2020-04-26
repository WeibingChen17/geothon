from Geothon import *

a = point('A')
assert(a.name == 'A')
assert(a in allPoints())

b = point('A')
assert(b is a )

assert(a.isConsolidate() == False)
assert(a.x == None)
assert(a.y == None)
a.consolidate()
assert(a.x != None)
assert(a.y != None)

c = point('C')
assert(c.distanceTo(a) > 0)
