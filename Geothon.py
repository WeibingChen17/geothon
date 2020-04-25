points = {}
segments = {}

def getPoint(name):
    if name in points:
        return points[name]
    else:
        new_point = Point(name)
        return new_point

def getPoints():
    return points.values()

def getSegment(begin, end):
    if begin + end in segments:
        return segments[begin + end]
    else:
        new_segment = Segment(begin, end)
        return new_segment

def getSegments():
    return segments.values()

class Point:
    def __init__(self, name):
        self.name = Name(name)
        points[name] = self
        self.x = None
        self.y = None

class Segment:
    def __init__(self, begin, end):
        self.name = Name(begin + end)
        self.begin = Point(begin)
        self.end = Point(end)
        segments[begin + end] = self
        segments[end + begin] = self

    def getLength(self):
        if 'length' in self.__dict__:
            return self.__dict__['length']
        self.length = Measure.distance(self.begin, self.end)
        return self.length

class Name:
    def __init__(self, name):
        self.name = name

    def eq(self, other_name):
        return sorted(list(self.name)) == sorted(list(other_name))

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
