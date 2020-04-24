import Geothon as G

a = G.Point('a')
assert(a.name.eq('a'))
assert(a in G.getPoints())

