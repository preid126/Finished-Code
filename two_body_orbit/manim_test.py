from manim import *

class Orbit(ThreeDScene):
    def construct(self) -> None:
        axes = ThreeDAxes()

        #Parameters
        g = 1

        #body 1
        m1 = 1
        r1 = np.array([2,3,1])
        v1 = 0.5

        body1 = Sphere(radius = 0.2, color = GREEN)
        body2 = Sphere(radius = 0.1, color = RED).move_to(r1)

