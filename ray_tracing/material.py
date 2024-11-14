from colour import Colour
from light import Light

class Material:
    """Material has colour and properties that reacts to light"""

    def __init__(self, colour = Colour.from_hex("#FFFFFF"), ambient = 0.05, diffuse = 1.0, specular = 1.0, reflection = 0.5):
        self.colour = colour
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.reflection = reflection



    def colour_at(self, position):
        return self.colour

class ChequeredMaterial:
    """Material has ChessBoard Pattern from two colours"""

    def __init__(self, colour1 = Colour.from_hex("#FFFFFF"), colour2 = Colour.from_hex("#000000"), ambient = 0.05, diffuse = 1.0, specular = 1.0, reflection = 0.5):
        self.colour1 = colour1
        self.colour2 = colour2
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.reflection = reflection


    def colour_at(self, position):
        if int((position.x + 0.5) * 3.0) % 2 == int(position.z * 3.0) % 2:
            return self.colour1 
        else:
            return self.colour2
        