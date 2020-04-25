points = {}
segments = {}
triangles = {}
circles = {}

def show():
    pass

def point(name):
    if name in points:
        return points[name]
    else:
        new_point = Point(name)
        return new_point

def allPoints():
    return points.values()

def segment(begin, end):
    name = ''.join(sorted([begin, end]))
    if name in segments:
        seg = segments[name]
        seg.setDirection(begin, end)
        return seg
    else:
        new_segment = Segment(begin, end)
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

class Name:
    def __init__(self, name):
        self.name = sorted(list(name)) 

    def eq(self, other_name):
        return self.name == sorted(list(other_name))

class Point:
    def __init__(self, name):
        self.name = Name(name)
        points[name] = self
        self.x = getRandom()
        self.y = getRandom()

    def distanceTo(self, p): 
        return Distance(1.0)

class Segment:
    def __init__(self, begin, end):
        self.name = Name(begin + end)
        self.begin = point(begin)
        self.end = point(end)
        segments[''.join(sorted([begin, end]))] = self
        self.direction = (self.begin, self.end)
        self.length = None

    def __contains__(self, p):
        pass

    def getLength(self):
        if self.length:
            return self.length
        self.length = self.begin.distanceTo(self.end)
        return self.length

    def setDirection(self, begin, end):
        self.direction = (point(begin), point(end))

    def extendTo(self, p, length):
        pass


class Triangle:
    def __init__(self, p1, p2, p3):
        self.name = Name(p1 + p2 + p3)
        self.points = [point(p1), point(p2), point(p3)]
        self.sides = [segment(p1, p2), segment(p2, p3), segment(p3, p1)]
        triangles[p1 + p2 + p3] = self

class Circle:
    def __init__(self, name):
        self.name = Name(name)
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
    def __init__(self, d):
        self.d = d

    def __eq__(self, d):
        if isinstance(d, Distance):
            return abs(self.d - d.d) < 1e-6
        elif isinstance(d, float):
            return abs(self.d - d) < 1e-6
    
    def __add__(self, d):
        return Distance(self.d + d.d)

    def __gt__(self, d):
        return self.d - d.d > 1e-6

    def __lt__(self, d):
        return d.d - self.d > 1e-6

def getRandom():
    return 1.0
