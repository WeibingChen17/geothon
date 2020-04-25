from Geothon import *

o = circle('o')
assert(o.name.eq('o'))
assert(o.getRadius() > 0)
assert(o.getCenter() in allPoints())
assert(o in allCircles())
