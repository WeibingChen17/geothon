from Geothon import *

seg = segment('A', 'B')
assert(seg.name == 'AB' and seg.name == 'BA')
assert(point('A') in allPoints())
assert(point('B') in allPoints())
assert(segment('A', 'B') in allSegments())
assert(segment('B', 'A') in allSegments())
assert(point('A').distanceTo(point('B')) == segment('A', 'B').getLength())

seg2 = segment('B', 'A')
assert(seg2 is seg)

seg.extendTo(point('C'), segment('A', 'B').getLength())
assert(segment('B', 'C') in allSegments())
assert(segment('B', 'C').getLength() == segment('A', 'B').getLength())
