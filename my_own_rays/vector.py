import numpy as np

# done

class Vector:

    def __init__(self, vector):
        self.vector = np.array(vector)

    def __str__(self):
        return f'{self.vector}'

    def dot(self, other):
        assert isinstance(other, Vector)
        return np.dot(self.vector, other.vector)

    def cross(self, other):
        assert isinstance(other, Vector)
        return Vector(np.cross(self.vector, other.vector))

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
            return Vector([a - b for a, b in zip(self.vector, other.vector)])
        else:
            return Vector(self.vector - other)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.vector * other)
        elif isinstance(other, Vector):
            return np.dot(self.vector, other.vector)
        else:
            raise TypeError("Invalid Multiplication")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Vector):
            return Vector(self.vector / other.vector)
        else: 
            return Vector(self.vector / other)


