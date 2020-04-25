import Geothon as G

seg = G.getSegment('a', 'b')
assert(seg.name.eq('ab') and seg.name.eq('ba'))
assert(G.getPoint('a') in G.getPoints())
assert(G.getPoint('b') in G.getPoints())
assert(G.getSegment('a', 'b') in G.getSegments())
assert(G.getSegment('b', 'a') in G.getSegments())
assert(G.Measure.distance(G.getPoint('a'), G.getPoint('b')) == G.getSegment('a', 'b').getLength())

seg2 = G.getSegment('b', 'a')
assert(seg2 is seg)
