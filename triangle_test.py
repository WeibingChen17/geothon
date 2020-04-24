import Geothon as G
triangle = G.Triangle('a', 'b', 'c')
assert(Point('a') in G.getPoints())
assert(Point('b') in G.getPoints())
assert(Point('c') in G.getPoints())
assert(Segment('a', 'b') in G.getSegments())
assert(Segment('b', 'c') in G.getSegments())
assert(Segment('c', 'a') in G.getSegments())
