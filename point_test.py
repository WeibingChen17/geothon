import Geothon as G

a = G.getPoint('a')
assert(a.name.eq('a'))
assert(a in G.getPoints())

c = G.getPoint('a')
assert(c is a )

