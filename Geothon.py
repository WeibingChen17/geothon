import math 
import random

points = {}
segments = {}
triangles = {}
circles = {}

def show():
    pass

def getAPoint():
    # This is the point generator.
    return random.random(), random.random()

def point(name):
    if name in points:
        return points[name]
    else:
        new_point = Point(name)
        return new_point

def allPoints():
    return points.values()

def segment(begin, end):
    name = ''.join(sorted([str(begin), str(end)]))
    if name in segments:
        seg = segments[name]
        seg.setBegin(point(begin)).setEnd(point(end))
        return seg
    else:
        new_segment = Segment(str(begin), str(end))
        return new_segment

def allSegments():
    return segments.values()

def triangle(p1, p2, p3):
    name = ''.join(sorted([p1, p2, p3]))
    if name in triangles:
        return triangles[name]
    else:
        new_triangle = Triangle(p1, p2, p3)
        return new_triangle

def allTriangles():
    return triangles.values()

def circle(name):
    if name in circles:
        return circles[name]
    else:
        new_circle = Circle(name)
        return new_circle

def allCircles():
    return circles.values()

class OrderedString:
    def __init__(self, string):
        self.string = ''.join(sorted(list(string)))

    def __eq__(self, other):
        if isinstance(other, str):
            return self.string == ''.join(sorted(list(other)))
        elif isinstance(other, OrderedString):
            return self.string == other.string
        else:
            return False

    def __repr__(self):
        return self.string

class GeoObject:
    def __init__(self):
        self._consolidate = False
        self._supporter = {}
        self._dependent = []

    def isConsolidate(self):
        return self._consolidate

    def isIndependent(self):
        return not self._supporter

    def setSupporter(self, supporter):
        self._supporter = supporter[:]

    def addDependent(self, dependent):
        self._dependent.append(dependent)

    def update(self):
        if self._consolidate:
            self._consolidate = False
            self.consolidate()


class Point(GeoObject):
    def __init__(self, name):
        super().__init__()
        self.name = OrderedString(name)
        self.x = None
        self.y = None
        points[name] = self

    def __repr__(self):
        return '{}({}, {})'.format(self.name, self.x, self.y)

    def setX(self, x):
        self.x = x
        self.update()
        return self

    def setY(self, y):
        self.y = y
        self.update()
        return self

    def consolidate(self):
        if self._consolidate:
            return
        self._consolidate = True
        if self.isIndependent():
            self.x, self.y = getAPoint()
        else:
            self.x, self.y = self._supporter[0](*(self._supporter[1:]))
        for d in self._dependent:
            d.update()
    
    def distanceTo(self, p): 
        self.consolidate()
        p.consolidate()
        return Distance(math.sqrt((self.x - p.x) * (self.x - p.x) 
            + (self.y - p.y) * (self.y - p.y)))

class Segment(GeoObject):
    def __init__(self, begin, end):
        super().__init__()
        self.name = OrderedString(begin + end)
        self.begin = point(begin)
        self.end = point(end)
        self.length = None
        segments[''.join(sorted([begin, end]))] = self

    def __repr__(self):
        return '{}({} -> {})'.format(self.name, self.begin, self.end)

    def __contains__(self, p):
        pass

    def setBegin(self, p):
        self.begin = p
        self.update()
        return self

    def setEnd(self, p):
        self.end = p
        self.update()
        return self

    def consolidate(self):
        if self._consolidate:
            return
        self._consolidate = True
        if self.isIndependent():
            self.begin.consolidate()
            self.end.consolidate()
        else:
            self.begin, self.end = self._supporter[0](*(self._supporter[1:]))
        for d in self._dependent:
            d.update()

    def extendTo(self, p, length):
        def _extendTo(p1, p2, l):
            p1.consolidate()
            p2.consolidate()
            s = p1.distanceTo(p2).getValue()
            if isinstance(length, Distance):
                l = l.getValue()
            return (p2.x - p1.x) * (1 +  l/s) + p1.x, \
                    (p2.y - p1.y) * (1 + l/s) + p1.y
        p.setSupporter([_extendTo, self.begin, self.end, length])
        segment(self.end.name, p.name)
        self.addDependent(p)

    def getLength(self):
        self.consolidate()
        if self.length:
            return self.length
        self.length = self.begin.distanceTo(self.end)
        return self.length

    def parrelleTo(self, other):
        self.consolidate()
        other.consolidate()
        # TODO (add more relation function)
        return True

    def perpendicularTo(self, other):
        pass


class Triangle:
    def __init__(self, p1, p2, p3):
        self.name = OrderedString(p1 + p2 + p3)
        self.points = [point(p1), point(p2), point(p3)]
        self.sides = [segment(p1, p2), segment(p2, p3), segment(p3, p1)]
        triangles[p1 + p2 + p3] = self

class Circle:
    def __init__(self, name):
        self.name = OrderedString(name)
        self.center = point(name)
        self.radius = getRandom()
        circles[name] = self

    def __contains__(self, p):
        return p.distanceTo(self.center) == self.radius
    
    def getCenter(self):
        return self.center

    def setCenter(self, center):
        self.center = center

    def getRadius(self):
        return self.radius

    def setRadisu(self, radius):
        self.radius = radius

    def buildFromThreePoints(self, p1, p2, p3):
        pass

class Distance:
    eps = 1e-6
    def __init__(self, value):
        self.value = value

    def __eq__(self, dis):
        if isinstance(dis, Distance):
            return abs(self.value - dis.value) < self.eps
        elif isinstance(dis, float):
            return abs(self.value - dis.value) < self.eps
        else:
            return False
    
    def __add__(self, dis):
        if isinstance(dis, (int, float)):
            return Distance(self.value + dis)
        elif isinstance(dis, Distance):
            return Distance(self.value + dis.value)

    def __sub__(self, dis):
        if isinstance(dis, (int, float)):
            return Distance(self.value - dis)
        elif isinstance(dis, Distance):
            return Distance(self.value - dis.value)

    def __mul__(self, dis):
        if isinstance(dis, (int, float)):
            return Distance(self.value * dis)
        elif isinstance(dis, Distance):
            return Distance(self.value * dis.value)

    def __gt__(self, dis):
        if isinstance(dis, (int, float)):
            return self.value - dis > self.eps
        elif isinstance(dis, Distance):
            return self.value - dis.value > self.eps
        # throw exception else

    def __lt__(self, dis):
        if isinstance(dis, (int, float)):
            return dis - self.value > self.eps
        elif isinstance(dis, Distance):
            return dis.value - self.value > self.eps

    def __repr__(self):
        return str(self.value)

    def getValue(self):
        return self.value

