from Geothon import *
import Relation as R

triangle('a', 'b', 'c')
segment('a', 'b').extendTo(point('d'), segment('a', 'c').getLength())
segment('c', 'b').extendTo(point('e'), segment('a', 'c').getLength())
segment('b', 'a').extendTo(point('f'), segment('c', 'b').getLength())
segment('c', 'a').extendTo(point('g'), segment('c', 'b').getLength())
segment('b', 'c').extendTo(point('h'), segment('a', 'b').getLength())
segment('a', 'c').extendTo(point('i'), segment('a', 'b').getLength())
assert(segment('b', 'd').getLength() == segment('b', 'e').getLength())
assert(segment('a', 'f').getLength() == segment('a', 'g').getLength())
assert(segment('c', 'h').getLength() == segment('c', 'i').getLength())
assert(R.concyclic(point('d'), point('e'), point('f'), point('g'), point('h'), point('i')))
o = circle('o').fromThreePoints(point('d'), point('e'), point('f'))
show()
