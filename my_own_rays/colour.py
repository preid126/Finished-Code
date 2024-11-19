import numpy as np
from vector import Vector

# done

class Colour(Vector):

    @classmethod
    def from_rgb(cls, red, green, blue):
        if not (0.0 <= red <= 1.0 and 0.0 <= green <= 1.0 and 0.0 <= blue <= 1.0):
            raise ValueError("RGB values must be in the range [0, 1].")
        return cls(np.array([red, green, blue]))

    def to_rgb(self):
        return tuple(int(max(min(c * 255, 255), 0)) for c in self.vector)

    def as_uint8(self):
        return (np.clip(self.vector * 255, 0, 255)).astype(np.uint8)
