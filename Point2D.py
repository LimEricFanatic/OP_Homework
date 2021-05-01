import math


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point2D (%f, %f)' % (self.x, self.y)

    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point2D(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Point2D(self.x / other.x, self.y / other.y)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalization(self):
        mod = math.sqrt(self.x ** 2 + self.y ** 2)
        self.x = self.x / mod
        self.y = self.y / mod
