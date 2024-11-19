import unittest
from vector import Vector
import numpy as np

# not done

class TestVectors(unittest.TestCase):
    def setup(self):
        a = np.array([1,2,2])
        b = np.array([2,3,-3])

        self.v1 = Vector(a)
        self.v2 = Vector(b)

    def test_magnitude(self):
        self.assertEqual(self.v1.magnitude(), 3)
    
    def test_addition(self):
        sum = self.v1 + self.v2 
        scalsum = self.v1 + 3
        self.assertEqual(sum, np.array([3,5,-1]))
        self.assertEqual(scalsum, np.array([4, 5, 5]))

    def test_multiplication(self):
        pass