from Geothon import *

seg = segment('a', 'b')
assert(seg.name == 'ab' and seg.name == 'ba')
assert(point('a') in allPoints())
assert(point('b') in allPoints())
assert(segment('a', 'b') in allSegments())
assert(segment('b', 'a') in allSegments())
assert(point('a').distanceTo(point('b')) == segment('a', 'b').getLength())

seg2 = segment('b', 'a')
assert(seg2 is seg)

seg.extendTo(point('c'), segment('a', 'b').getLength())
assert(segment('b', 'c') in allSegments())
assert(segment('b', 'c').getLength() == segment('a', 'b').getLength())
