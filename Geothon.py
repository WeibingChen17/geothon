points = {}
segments = {}
triangles = {}
circles = {}

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
        self.x = None
        self.y = None

class Segment:
    def __init__(self, begin, end):
        self.name = Name(begin + end)
        self.begin = point(begin)
        self.end = point(end)
        segments[''.join(sorted([begin, end]))] = self
        self.direction = (self.begin, self.end)
        self.length = None

    def getLength(self):
        if self.length:
            return self.length
        self.length = Measure.distance(self.begin, self.end)
        return self.length

    def setDirection(self, begin, end):
        self.direction = (point(begin), point(end))

class Triangle:
    def __init__(self, p1, p2, p3):
        self.name = Name(p1 + p2 + p3)
        self.points = [point(p1), point(p2), point(p3)]
        self.sides = [segment(p1, p2), segment(p2, p3), segment(p3, p1)]
        triangles[p1 + p2 + p3] = self

class Circe:
    def __init__(self, name):
        self.name = Name(name)
        self.center = None
        self.radius = None
    
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

class Measure:
    def __init__(self):
        pass

    @staticmethod
    def distance(p1, p2):
        return 1.0

class Transform:
    def __init__(self):
        pass

    @staticmethod
    def extend(seg):
        pass
