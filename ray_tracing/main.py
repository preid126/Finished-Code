#!/usr/bin/venv python

import argparse
import importlib
from my_vector import Vector
from colour import Colour
from image import Image
from point import Point
from sphere import Sphere
from scene import Scene #
from engine import RenderEngine
from light import Light
from material import Material
import math
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("scene", help = "Path to scene file")
    args = parser.parse_args()
    mod = importlib.import_module(args.scene)

    scene = Scene(mod.CAMERA, mod.OBJECTS, mod.LIGHTS, mod.WIDTH, mod.HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)


    os.chdir(os.path.dirname(os.path.abspath(mod.__file__)))
    with open(mod.RENDERED_IMG, "w") as img_file:
        image.write_ppm(img_file)

if __name__ == "__main__":
    main()


