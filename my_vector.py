import math

class Vector:
    """A Three element vector"""
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def dot(self, new):
        return self.x * new.x + self.y * new.y + self.z * new.z

    def magnitude(self):
        return math.sqrt(self.dot(self))

    def normalize(self):
        return self / self.magnitude()

    def __truediv__(self, other):
        assert not isinstance(other,Vector)
        return Vector(self.x / other, self.y / other, self.z /other)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        assert not isinstance(other,Vector)
        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return self.__mul__(other)