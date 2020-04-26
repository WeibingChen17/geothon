from Geothon import *

t = triangle('A', 'B', 'C')
assert(point('A') in allPoints())
assert(point('B') in allPoints())
assert(point('C') in allPoints())
assert(segment('A', 'B') in allSegments())
assert(segment('B', 'C') in allSegments())
assert(segment('C', 'A') in allSegments())

assert(segment('A', 'B').getLength() + segment('B', 'C').getLength() > segment('C', 'A').getLength())
assert(len(t.sides) == 3)
assert(len(t.points) == 3)

t2 = triangle('A', 'C', 'D')
assert(t2.getArea() > 0)
