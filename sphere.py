import math

class Sphere:
    """Sphere is the only 3d shape, has radius, centre and material"""
    def __init__(self, centre, rad, mat):
        self.rad = rad
        self.centre = centre
        self.mat = mat


    def volume(self,rad):
        return self.rad * self.rad * self.rad * math.pi * (4/3)

    def intersects(self, ray):
        """Checks for intersections, returns ditsance if occured"""

        sphere_to_ray = ray.origin - self.centre
        b = 2 * ray.direction.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - self.rad * self.rad
        disc = b * b - 4 * c
         
        if disc >= 0:
            dist = (-b - math.sqrt(disc))/2
            if dist > 0:
                return dist

        return None

        

    
    
