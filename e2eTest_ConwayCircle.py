from Geothon import *
import Relation as R

triangle('A', 'B', 'C')
segment('A', 'B').extendTo(point('D'), segment('A', 'C').getLength())
segment('C', 'B').extendTo(point('E'), segment('A', 'C').getLength())
segment('B', 'A').extendTo(point('F'), segment('C', 'B').getLength())
segment('C', 'A').extendTo(point('G'), segment('C', 'B').getLength())
segment('B', 'C').extendTo(point('H'), segment('A', 'B').getLength())
segment('A', 'C').extendTo(point('I'), segment('A', 'B').getLength())
circle('O').fromThreePoints(point('D'), point('E'), point('F'))

assert(segment('B', 'D').getLength() == segment('B', 'E').getLength())
assert(segment('A', 'F').getLength() == segment('A', 'G').getLength())
assert(segment('C', 'H').getLength() == segment('C', 'I').getLength())
assert(R.concyclic(point('D'), point('E'), point('F'), point('G'), point('H'), point('I')))

show()
