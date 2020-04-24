import Geothon as G

seg = G.Segment('a', 'b')
assert(seg.name.eq('ab') and seg.name.eq('ba'))
assert(G.Point('a') in G.getPoints())
assert(G.Point('b') in G.getPoints())
assert(G.Segment('a', 'b') in G.getSegments())
assert(G.Segment('b', 'a') in G.getSegments())
assert(G.Measure.distance(G.Point('a'), G.Point('b')) 
        == G.Measure.length(G.Segment('a', 'b')))
