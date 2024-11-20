from vector import Vector
import numpy as np
from colour import Colour

#think this is done

class Sphere:
    
    def __init__(self, center, material, center_velocity = Vector(np.array([0,0,0])) , radius = 1.0):
        self.center = Vector(center) if not isinstance(center, Vector) else center
        self.center_velocity = center_velocity
        self.radius = radius
        self.material = material

    def volume(self):
        return np.pi * (4/3) * (self.radius ** 3)

    def intersection(self, ray):
        sphere_to_ray = ray.origin - self.center
        b = 2 * ray.direction.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - self.radius ** 2
        disc = b * b - 4 * c

        if disc >= 0:
            dist = (-b - np.sqrt(disc)) / 2
            if dist > 0:
                return dist
        return None

    def normal(self, surface_point):
        return (surface_point - self.center).normalize()


class Plane:

    def __init__(self, origin, u, v, material, finite = True):

        self.origin = Vector(origin) if not isinstance(origin, Vector) else origin
        self.u = Vector(u) if not isinstance(u, Vector) else u
        self.v = Vector(v) if not isinstance(v, Vector) else v
        self.normal = self.u.cross(self.v).normalize()
        self.material = material
        self.finite = finite

        if self.u.cross(self.v).magnitude() == 0:
            raise ValueError("u and v cannot be parallel")

    def area(self):
        return (self.u.cross(self.v)).magnitude()

    def intersection(self, ray):

        denom = self.normal.dot(ray.direction)
        if np.abs(denom) < 1e-6:
            return None
        d = (self.origin - ray.origin).dot(self.normal) / denom
        if d < 0: 
            return None
        hit_pos = ray.origin + ray.direction * d

        if self.finite:
            proj_u = (hit_pos - self.origin).dot(self.u.normalize())
            proj_v = (hit_pos - self.origin).dot(self.v.normalize())

            if 0 <= proj_u <= self.u.magnitude() and 0 <= proj_v <= self.v.magnitude():
                return d
                print(f"Ray origin: {ray.origin}, direction: {ray.direction}, sphere center: {self.center}")
                print(f"Intersection distance: {dist}")
            else:
                return None

    def contains(self, point):
        if not self.finite:
            return True

        dist = point - self.origin
        proj_u = dist.dot(self.u.normalize())
        proj_v = dist.dot(self.v.normalize())

        return 0 <= proj_u <= self.u.magnitude() and 0 <= proj_v <= self.v.magnitude()


class LightSource:

    def __init__(self, position, colour = Colour.from_rgb(1, 1, 1), velocity = Vector([0,0,0])):
        self.position = Vector(position) if not isinstance(position, Vector) else position
        self.colour = colour
        self.velocity = Vector(velocity) if not isinstance(velocity, Vector) else velocity


class Ray:

    def __init__(self, origin, direction):
        self.origin = Vector(origin) if not isinstance(origin, Vector) else origin
        self.direction = (Vector(direction) if not isinstance(direction, Vector) else direction).normalize()

