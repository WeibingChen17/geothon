from Geothon import *

o = circle('O')
assert(o.name == 'O')
assert(o.getCenter() in allPoints())
# print(o)
assert(o in allCircles())

# print(point('A'))
# print(point('B'))
# print(point('C'))
o.fromThreePoints(point('A'), point('B'), point('C'))
assert(point('A') in o)
assert(point('B') in o)
assert(point('C') in o)
# print(o)
assert(o.getRadius() > 0)
