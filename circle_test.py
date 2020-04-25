from Geothon import *

o = circle('o')
assert(o.name == 'o')
assert(o.getCenter() in allPoints())
# print(o)
assert(o in allCircles())

# print(point('a'))
# print(point('b'))
# print(point('c'))
o.fromThreePoints(point('a'), point('b'), point('c'))
assert(point('a') in o)
assert(point('b') in o)
assert(point('c') in o)
# print(o)
assert(o.getRadius() > 0)
