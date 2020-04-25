from Geothon import *

triangle('a', 'b', 'c')
assert(point('a') in allPoints())
assert(point('b') in allPoints())
assert(point('c') in allPoints())
assert(segment('a', 'b') in allSegments())
assert(segment('b', 'c') in allSegments())
assert(segment('c', 'a') in allSegments())

assert(segment('a', 'b').getLength() + segment('b', 'c').getLength() > segment('c', 'a').getLength())
