import numpy as np

class Vector:

    def __init__(self, vector):
        self.vector = vector

    def __str__(self):
        return f'{self.vector}'

    def dot(self, other):
        assert isinstance(other, Vector)
        return np.dot(self.vector, other.vector)

    def magnitude(self):
        return np.linalg.norm(self.vector)

    def normalize(self):
        norm = self.magnitude()
        return Vector(self.vector / norm)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.vector + other.vector)
        else:
            return Vector(self.vector + other)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.vector - other.vector)
        else:
            return Vector(self.vector - other)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(self.vector * other.vector)
        else:
            return Vector(self.vector * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv(self, other):
        if isinstance(other, Vector):
            return Vector(self.vector / other.vector)
        else: 
            return Vector(self.vector / other)


