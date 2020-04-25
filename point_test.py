from Geothon import *

a = point('a')
assert(a.name.eq('a'))
assert(a in allPoints())

c = point('a')
assert(c is a )

