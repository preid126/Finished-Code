from engine import Engine
from objects import Sphere, Plane, LightSource, Ray
from visuals import Image, Video
from colour import Colour
from material import Material
from scene import Scene
from vector import Vector
import numpy as np
import os


def main():
    
    WIDTH = 320
    HEIGHT = 200

    #camera position
    CAMERA = Vector([4, 4, 7])

    #material types
    dirt = Material(colour = Colour.from_rgb(0.02, 0.75, 0.02 ), reflection = 0.05)
    metal = Material(colour = Colour.from_rgb(0.6, 0.6, 0.6), ambient = 0.1, reflection = 0.7)
    something_pink = Material(colour = Colour.from_rgb(1.0, 0.4, 0.6), diffusion = 0.6, specular = 0.5 )

    #objects 
    sphere1 = Sphere(center = Vector([2, 1, -2]), radius = 3, material = something_pink)
    sphere2 = Sphere(center = Vector([5, 4, -5]), radius = 2, material = metal)
    plane1 = Plane(origin = Vector([0,-4,-10]), u = Vector([14,0,0]), v = Vector([0,24,0]), material = dirt)

    #light sources
    light1 = LightSource(position = Vector([4, 6, 5]), velocity = Vector([1,0,0]))

    #scene
    scene = Scene(camera = CAMERA, width = WIDTH, height = HEIGHT)
    scene.add_object(sphere1)
    scene.add_object(sphere2)
    scene.add_object(plane1)
    scene.add_light(light1)

    engine = Engine()


    #engine.render(scene, video_mode = False)
    videopath = os.path.expanduser("~/Desktop/rendered_scene.mp4")
    engine.render(scene, video_mode = True, frame_count = 60, fps = 30, output_file = videopath)




if __name__ == "__main__":
    main()
