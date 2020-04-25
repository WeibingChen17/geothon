import math 
import numpy 
import random
from collections import defaultdict

geoObjects = defaultdict(dict)

def show():
    for objectType, objectDict in geoObjects.items():
        for objectName, instance in objectDict.items():
            instance.consolidate()
    for objectType, objectDict in geoObjects.items():
        for objectName, instance in objectDict.items():
            print(instance)


def getAFloat():
    return random.random()

def getAPoint():
    # This is the point generator.
    return random.random(), random.random()

def point(name):
    points = geoObjects['points']
    if name in points:
        return points[name]
    else:
        new_point = Point(name)
        return new_point

def allPoints():
    return geoObjects['points'].values()

def segment(begin, end):
    segments = geoObjects['segments']
    name = ''.join(sorted([str(begin), str(end)]))
    if name in segments:
        seg = segments[name]
        seg.setBegin(point(begin)).setEnd(point(end))
        return seg
    else:
        new_segment = Segment(str(begin), str(end))
        return new_segment

def allSegments():
    return geoObjects['segments'].values()

def triangle(p1, p2, p3):
    triangles = geoObjects['triangles']
    name = ''.join(sorted([p1, p2, p3]))
    if name in triangles:
        return triangles[name]
    else:
        new_triangle = Triangle(p1, p2, p3)
        return new_triangle

def allTriangles():
    return geoObjects['triangles'].values()

def circle(name):
    circles = geoObjects['circles']
    if name in circles:
        return circles[name]
    else:
        new_circle = Circle(name)
        return new_circle

def allCircles():
    return geoObjects['circles'].values()

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

    def consolidate(self):
        pass

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
        geoObjects['points'][name] = self

    def __repr__(self):
        return '{}({}, {})'.format(self.name, self.x, self.y)

    def setX(self, x):
        self.x = x
        for d in self._dependent:
            d.update()
        return self

    def setY(self, y):
        self.y = y
        for d in self._dependent:
            d.update()
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
        geoObjects['segments'][''.join(sorted([begin, end]))] = self

    def __repr__(self):
        return '{}({} -> {})'.format(self.name, self.begin, self.end)

    def __contains__(self, p):
        pass

    def setBegin(self, p):
        self.begin = p
        for d in self._dependent:
            d.update()
        return self

    def setEnd(self, p):
        self.end = p
        for d in self._dependent:
            d.update()
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


class Triangle(GeoObject):
    def __init__(self, p1, p2, p3):
        super().__init__()
        self.name = OrderedString(p1 + p2 + p3)
        self.points = [point(p1), point(p2), point(p3)]
        self.sides = [segment(p1, p2), segment(p2, p3), segment(p3, p1)]
        geoObjects['triangles'][p1 + p2 + p3] = self

    def __repr__(self):
        return '{}({}, {}, {})'.format(self.name, *self.points)

    def consolidate(self):
        if self._consolidate:
            return
        self._consolidate = True
        if self.isIndependent():
            for p in self.points:
                p.consolidate()
        else:
            # (todo) better update triangle here
            self.points, self.sides = self._supporter[0](*(self._supporter[1:]))
        for d in self._dependent:
            d.update()

    def getArea(self):
        lengths = [s.getLength().getValue() for s in self.sides]
        semip = sum(lengths) * 0.5
        return math.sqrt(semip * numpy.prod([semip - l for l in lengths]))


class Circle(GeoObject):
    def __init__(self, name):
        super().__init__()
        self.name = OrderedString(name)
        self.center = point(name)
        self.radius = None
        geoObjects['circles'][name] = self

    def __contains__(self, p):
        self.consolidate()
        p.consolidate()
        return p.distanceTo(self.center) == self.radius

    def __repr__(self):
        return '{}({}, r({}))'.format(self.name, self.center, self.radius)
    
    def getCenter(self):
        self.consolidate()
        return self.center

    def setCenter(self, center):
        self.center = center
        self.update()
        return self

    def getRadius(self):
        self.consolidate()
        return self.radius

    def setRadisu(self, radius):
        self.radius = radius
        self.update()
        return self

    def consolidate(self):
        if self._consolidate:
            return
        self._consolidate = True
        if self.isIndependent():
            self.center.consolidate()
            self.radius = getAFloat()
        else:
            x, y, r = self._supporter[0](*(self._supporter[1:]))
            if x == None:
                # throw exception here
                return 
            self.center.setX(x).setY(y)
            self.radius = r
        for d in self._dependent:
            d.update()

    def fromThreePoints(self, p1, p2, p3):
        def getACirleFromThreePoint(p1, p2, p3):
            p1.consolidate()
            p2.consolidate()
            p3.consolidate()
            x1, y1, x2, y2, x3, y3 = p1.x, p1.y, p2.x, p2.y, p3.x, p3.y
            A = x1*(y2-y3)-y1*(x2-x3)+x2*y3-x3*y2
            if abs(A) < 1e-6:
                return None, None, None
            B = (x1*x1+y1*y1)*(y3-y2)+(x2*x2+y2*y2)*(y1-y3)+(x3*x3+y3*y3)*(y2-y1)
            C = (x1*x1+y1*y1)*(x2-x3)+(x2*x2+y2*y2)*(x3-x1)+(x3*x3+y3*y3)*(x1-x2)
            D = (x1*x1+y1*y1)*(x3*y2-x2*y3)+(x2*x2+y2*y2)*(x1*y3-x3*y1)+(x3*x3+y3*y3)*(x2*y1-x1*y2)
            x = -B/2/A
            y = -C/2/A
            r = math.sqrt(B*B+C*C-4*A*D)/abs(2*A)
            return x, y, r
        self.setSupporter([getACirleFromThreePoint, p1, p2, p3])
        self._consolidate = False
        p1.addDependent(self)
        p2.addDependent(self)
        p3.addDependent(self)
        return self

class Distance:
    eps = 1e-6
    def __init__(self, value):
        self.value = value

    def __eq__(self, dis):
        if isinstance(dis, (int, float)):
            return abs(self.value - dis) < self.eps
        elif isinstance(dis, Distance):
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

