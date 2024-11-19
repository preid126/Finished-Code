from vector import Vector
import numpy as np

#not done
#need to do inersections

class Sphere:
    
    def __init__(self, center, center_velocity, radius, material):
        self.center = center
        self.center_velocity = center_velocity
        self.radius = radius
        self.material = material

    def volume(self):
        return np.pi * (4/3) * (self.radius ** 3)


class Plane:

    def __init__(self, width, height, origin, material):
        self.width = widht
        self.height = height
        self.origin = origin
        self.material = material

    def area(self):
        return self.width * self.height


class LightSource:

    def __init__(self, position, velocity, colour):
        self.position = position
        self.colour = colour
        self.velocity = velocity

    def motion(self, position, velocity, t_step):
        self.position += velocity * t_step


class Point(Vector):
    pass

class Ray:

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalize()

