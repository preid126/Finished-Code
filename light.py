from colour import Colour

class Light:
    """Light represents a point light source of a certain colour"""

    def __init__(self, position, colour = Colour.from_hex("#FFFFFF")):
        self.position = position
        self.colour = colour

        