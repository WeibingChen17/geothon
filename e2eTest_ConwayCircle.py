import Geothon as G

triangle('a', 'b', 'c')
segment('a', 'b').extendTo(point('d'), segment('a', 'c').getlength())
segment('c', 'b').extendto(point('e'), segment('a', 'c').getlength())
segment('b', 'a').extendto(point('f'), segment('c', 'b').getlength())
segment('c', 'a').extendto(point('g'), segment('c', 'b').getlength())
segment('b', 'c').extendto(point('h'), segment('a', 'b').getlength())
segment('a', 'c').extendto(point('i'), segment('a', 'b').getLength())
assert(G.Measure.concyclic(Point('d'), Point('e'), Point('f'), Point('g'), Point('h'), Point('i')))
circle('o'). buildFromThreePoints(point('d'), point('e'), point('f'))
G.show()
