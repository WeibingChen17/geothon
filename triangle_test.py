from Geothon import *

t = triangle('a', 'b', 'c')
assert(point('a') in allPoints())
assert(point('b') in allPoints())
assert(point('c') in allPoints())
assert(segment('a', 'b') in allSegments())
assert(segment('b', 'c') in allSegments())
assert(segment('c', 'a') in allSegments())

assert(segment('a', 'b').getLength() + segment('b', 'c').getLength() > segment('c', 'a').getLength())
assert(len(t.sides) == 3)
assert(len(t.points) == 3)

t2 = triangle('a', 'c', 'd')
assert(t2.getArea() > 0)
