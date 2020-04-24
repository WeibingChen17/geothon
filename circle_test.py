import Geothon as G

circle = G.Circle('c')
assert(a.name.eq('c'))
assert(a.radius > 0)
assert(a.center in G.getPoints())
assert(circle in G.getCircles())
