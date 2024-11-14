from image import Image
from ray import Ray
from point import Point
from colour import Colour


class RenderEngine:
    """Renderes 3d objects into 2d objects using ray tracing"""

    MAX_DEPTH = 5
    MIN_DISPLACE = 0.0001

    def render(self, scene):
        width = scene.width
        height = scene.height
        aspect_ratio = float(width)/ height

        x0 = -1.0 
        x1 = 1.0
        xstep = (x1 - x0) / (width - 1)

        y0 = -1.0 / aspect_ratio
        y1 = +1.0 / aspect_ratio
        ystep = (y1 - y0) / (height - 1)

        camera = scene.camera 
        pixels = Image(width, height)

        for j in range(height):
            y = y0 + j*ystep
            for i in range(width):
                x = x0 + i*xstep
                ray = Ray(camera, Point(x,y) - camera)
                pixels.set_pixel(i,j, self.ray_trace(ray,scene) )
            print("{:3.0f}%".format(float(j)/float(height) * 100), end = '\r')
        return pixels

    def ray_trace(self, ray, scene, depth = 0):
        colour = Colour(0,0,0)
        #finding nearest hit
        dist_hit, obj_hit = self.find_nearest(ray, scene)
        if obj_hit is None:
            return colour
        hit_pos = ray.origin + ray.direction * dist_hit
        hit_normal = obj_hit.normal(hit_pos)
        colour += self.colour_at(obj_hit, hit_pos, hit_normal, scene)

        if depth < self.MAX_DEPTH:
            new_ray_pos = hit_pos + hit_normal * self.MIN_DISPLACE
            new_ray_dir = ray.direction - 2*ray.direction.dot(hit_normal) * hit_normal
            new_ray = Ray(new_ray_pos, new_ray_dir)

            colour += self.ray_trace(new_ray, scene, depth + 1) * obj_hit.mat.reflection

        return colour

    def find_nearest(self, ray, scene):
        dist_min = None
        obj_hit = None
        for obj in scene.objects:
            dist = obj.intersects(ray)
            if dist is not None and (obj_hit is None or dist < dist_min):
                dist_min = dist
                obj_hit = obj
        return (dist_min, obj_hit)

    def colour_at(self, obj_hit, hit_pos, normal, scene):
        material = obj_hit.mat
        obj_colour = material.colour_at(hit_pos)
        to_cam = scene.camera - hit_pos
        specular_k = 50
        colour = material.ambient * Colour.from_hex("#FFFFFF")

        #light calculations
        for light in scene.lights:
            to_light = Ray(hit_pos, light.position - hit_pos)

            #diffusive
            colour += (obj_colour * material.diffuse * 
                    max(normal.dot(to_light.direction), 0))
            #specular
            half_vector = (to_light.direction + to_cam).normalize()
            colour+= light.colour * material.specular * max(normal.dot(half_vector), 0) ** specular_k

        return colour


