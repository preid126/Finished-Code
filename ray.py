from my_vector import Vector

class Ray:
    """half line with an origin and a normlaized direction"""
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalize()

    def dot(self, new):
        return self.x * new.x + self.y * new.y + self.z * new.z