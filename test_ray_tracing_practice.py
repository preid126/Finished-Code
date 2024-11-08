import platform
import numpy as np
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
print("sys.path:", sys.path)
from my_vector import Vector

print('Python Version is {}'.format(platform.python_version()))

#Points in 3d space

#trying with classes aswell

class TestVectors(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector(1.0, -2.0, -2.0)
        self.v2 = Vector(1.2, 1.0, -2.0)

    def test_magnitude(self):
        self.assertEqual(self.v1.magnitude(), 3)

    def test_addition(self):
        sum = self.v1 + self.v2
        self.assertEqual(getattr(sum, "x"), 2.2)

    def test_multiplication(self):
        prod = self.v1 * -2.0
        self.assertEqual(getattr(prod, "z"), 4.0)

    def test_div(self):
        coup = self.v1 / -2.0
        self.assertEqual(getattr(coup, "y"), 1.0)


if __name__ == "__main__":
    unittest.main()