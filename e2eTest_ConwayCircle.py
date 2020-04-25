from Geothon import *
import Relation as R

triangle('a', 'b', 'c')
segment('a', 'b').extendTo(point('d'), segment('a', 'c').getLength())
segment('c', 'b').extendTo(point('e'), segment('a', 'c').getLength())
segment('b', 'a').extendTo(point('f'), segment('c', 'b').getLength())
segment('c', 'a').extendTo(point('g'), segment('c', 'b').getLength())
segment('b', 'c').extendTo(point('h'), segment('a', 'b').getLength())
segment('a', 'c').extendTo(point('i'), segment('a', 'b').getLength())
(R.concyclic(point('d'), point('e'), point('f'), point('g'), point('h'), point('i')))
circle('o').fromThreePoints(point('d'), point('e'), point('f'))
show()
