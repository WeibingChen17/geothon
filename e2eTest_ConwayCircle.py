import Geothon as G

G.Triangle('a', 'b', 'c')
G.Transform.extend(Segment('a', 'b')).to(Point('d')).withLength(G.Measure.length(Segment('a', 'c')))
G.Transform.extend(Segment('c', 'b')).to(Point('e')).withLength(G.Measure.length(Segment('a', 'c')))
G.Transform.extend(Segment('b', 'a')).to(Point('f')).withLength(G.Measure.length(Segment('c', 'b')))
G.Transform.extend(Segment('c', 'a')).to(Point('g')).withLength(G.Measure.length(Segment('c', 'b')))
G.Transform.extend(Segment('b', 'c')).to(Point('h')).withLength(G.Measure.length(Segment('a', 'b')))
G.Transform.extend(Segment('a', 'c')).to(Point('i')).withLength(G.Measure.length(Segment('a', 'b')))
G.Circle('d', 'e', 'f')
assert(G.Measure.concyclic(Point('d'), Point('e'), Point('f'), Point('g'), Point('h'), Point('i')))
G.show()
