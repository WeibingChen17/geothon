import Geothon as G

G.Triangle('a', 'b', 'c')
G.Transform.extend(Segment('a', 'b')).to(Point('d')).withLength(Segment('a', 'c').getLength())
G.Transform.extend(Segment('c', 'b')).to(Point('e')).withLength(Segment('a', 'c').getLength())
G.Transform.extend(Segment('b', 'a')).to(Point('f')).withLength(Segment('c', 'b').getLength())
G.Transform.extend(Segment('c', 'a')).to(Point('g')).withLength(Segment('c', 'b').getLength())
G.Transform.extend(Segment('b', 'c')).to(Point('h')).withLength(Segment('a', 'b').getLength())
G.Transform.extend(Segment('a', 'c')).to(Point('i')).withLength(Segment('a', 'b').getLength())
G.Circle('d', 'e', 'f')
assert(G.Measure.concyclic(Point('d'), Point('e'), Point('f'), Point('g'), Point('h'), Point('i')))
G.show()
