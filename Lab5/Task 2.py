import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Segment:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def length(self):
        return math.sqrt((self.point2.x - self.point1.x) ** 2 + (self.point2.y - self.point1.y) ** 2)

class Triangle:
    def __init__(self, point1, point2, point3):
        self.side1 = Segment(point1, point2)
        self.side2 = Segment(point2, point3)
        self.side3 = Segment(point3, point1)

    def perimeter(self):
        return self.side1.length() + self.side2.length() + self.side3.length()
            
p1 = Point(0, 0)
p2 = Point(3, 0)
p3 = Point(0, 4)

segment = Segment(p1, p2)
print("Довжина відрізка:", segment.length())

triangle = Triangle(p1, p2, p3)
print("Периметр трикутника:", triangle.perimeter())