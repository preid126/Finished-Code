import numpy as np
import scipy as sp
from scipy.integrate import quad
import math

class Sphere:
    def __init__(self, center_pos, center_velocity, radius, density_function):

        """
        Defining a sphereical object
        - center_pos: a np array of [x,y,z]
        - center_velocity: np array of [v_x, v_y, v_z]
        - radius: constant radius of the sphere
        - density_function: a density dependent on displacement from the center (r)
        """

        self.center_pos = center_pos
        self.center_velocity = center_velocity
        self.radius = float(radius)
        self.density_function = density_function 

    def volume(self) -> float:
        return (self.radius **3) * math.pi * (4/3)

    def mass(self) -> float:
        result, error = quad(lambda r: self.density_function(r) * (r**2), 0, self.radius)
        return 4 * math.pi * result