from Geothon import *

seg = segment('a', 'b')
assert(seg.name.eq('ab') and seg.name.eq('ba'))
assert(point('a') in allPoints())
assert(point('b') in allPoints())
assert(segment('a', 'b') in allSegments())
assert(segment('b', 'a') in allSegments())
assert(Measure.distance(point('a'), point('b')) == segment('a', 'b').getLength())

seg2 = segment('b', 'a')
assert(seg2 is seg)
