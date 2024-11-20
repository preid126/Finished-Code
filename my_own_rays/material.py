import numpy as np
from vector import Vector
from colour import Colour
from visuals import Image, Video

# done I think

class Material():
    
    def __init__(self, colour = Colour.from_rgb(0.5,0.5,0.5), ambient = 0.05, diffusion = 0.9, specular = 0.8, reflection = 0.4 ):
        self.colour = colour
        self.ambient = ambient
        self.diffusion = diffusion
        self.specular = specular
        self.reflection = reflection

    def colour_at(self, position):
        return self.colour