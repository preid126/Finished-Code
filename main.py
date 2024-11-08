#!/usr/bin/venv python
from my_vector import Vector
from colour import Colour
from image import Image
from point import Point
from sphere import Sphere
from scene import Scene
from engine import RenderEngine

def main():
    WIDTH = 320 # upper case means constant
    HEIGHT = 200
    camera = Vector(0, 0, -1)
    objects = [Sphere(Point(0, 0, 0), 0.5, Colour.from_hex("#FF0000"))]
    scene = Scene(camera, objects, WIDTH, HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)



    with open("test.ppm", "w") as img_file:
        image.write_ppm(img_file)

if __name__ == "__main__":
    main()


