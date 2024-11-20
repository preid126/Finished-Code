from vector import Vector
from objects import Sphere, Plane, LightSource, Ray
from colour import Colour
from visuals import Image, Video
from scene import Scene
import numpy as np


# not done

class Engine:

    DEPTH = 5
    MIN_DISPLACEMENT = 0.0001


    def find_nearest(self, ray, scene):
        dist_min = None
        obj_hit = None
        for obj in scene.objects:
            dist = obj.intersection(ray)
            if dist is not None and (obj_hit is None or dist < dist_min):
                dist_min = dist
                obj_hit = obj

        return (dist_min, obj_hit)

    def colour_at(self, obj_hit, hit_pos, normal, scene, depth = 0):
        material = obj_hit.material
        obj_colour = material.colour_at(hit_pos)
        to_cam = scene.camera - hit_pos
        specular_k = 50
        colour = material.ambient * Colour.from_rgb(1, 1, 1)

        for light in scene.lights:
            to_light = Ray(hit_pos, light.position - hit_pos)
            light_dir = to_light.direction.normalize()

            colour += (obj_colour * material.diffusion * max(normal.dot(light_dir), 0))

            half_vec = (to_light.direction + to_cam).normalize()
            colour += light.colour * material.specular * (max(normal.dot(half_vec), 0) ** specular_k)



        if material.reflection > 0 and depth < self.DEPTH:
            reflected_dir = normal * 2 * normal.dot(to_light.direction) - to_light.direction
            reflected_ray = Ray(hit_pos, reflected_dir)

            reflected_colour = self.ray_trace(reflected_ray, scene, depth+1)
            colour += material.reflection * reflected_colour

        return colour

    def render(self, scene, video_mode = False, frame_count = 1, fps = 30, output_file = "output.mp4"):
        width, height = scene.width, scene.height
        aspect_ratio = width/height

        if video_mode:
            video = Video(width, height, frame_count)
        else:
            image = Image(width, height)

        for frame_idx in range(frame_count if video_mode else 1):
            if video_mode:
                print(f"Rendering frame {frame_idx + 1}/{frame_count}...")
                scene.update_scene(frame_idx / fps)

            for y in range(height):
                for x in range(width):
                    corrected_x = (x + 0.5) / width
                    corrected_y = (y + 0.5) / height

                    screen_x = (2 * corrected_x - 1) * aspect_ratio
                    screen_y = 1 - 2 * corrected_y

                    ray_ar = np.array([screen_x, screen_y, -1])
                    ray_direction = Vector(ray_ar).normalize()

                    ray = Ray(scene.camera, ray_direction)
                    colour = self.ray_trace(ray, scene)

                    if video_mode:
                        video.set_pixel(frame_idx, x, y, colour)
                    else:
                        image.set_pixel(x, y, colour)
    
        if video_mode:
            video.write_mp4(output_file, fps = fps)
            print(f'Video saved to {output_file}')

        else:
            output_name = 'output.png'
            image.save(f"/Users/paulreid/Desktop/{output_name}")
            print(f'Image saved to {output_name}')
        

    def ray_trace(self, ray, scene, depth = 0):
       
        base_col = Colour.from_rgb(0,0,0)

        if depth >= self.DEPTH:
            return base_col

        dist, obj_hit = self.find_nearest(ray, scene)

        if obj_hit is None:
            return base_col

        hit_pos = ray.origin + ray.direction * dist
        if isinstance(obj_hit, Sphere):
            normal = obj_hit.normal(hit_pos)
        elif isinstance(obj_hit, Plane):
            normal = obj_hit.normal
        else:
            raise TypeError("Unsupported Object Type")


        colour = self.colour_at(obj_hit, hit_pos, normal, scene, depth)

        return colour

    
    