from object import Sphere
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


body1 = Sphere(np.array([0,0,0]), np.array([1,1,2]), 100000, lambda r: 0.2*r)
body2 = Sphere(np.array([30000,-200000,2]), np.array([0,30,4]), 50000, lambda r: 0.3*r)

G = 6.6743e-20
mu = body1.mass() * body2.mass() / (body1.mass() + body2.mass())

rel_pos = body2.center_pos - body1.center_pos
rel_vel = body2.center_velocity - body1.center_velocity

def rotation_matrix(vec):
    unit_vec = vec / np.linalg.norm(vec)

    target = np.array([1, 1, 0])
    target_unit_vec = target / np.linalg.norm(target)

    a = unit_vec
    b = target_unit_vec

    rot_axis = np.cross(a,b)

    cos = np.dot(a,b)
    sin = np.linalg.norm(rot_axis)

    if sin == 0:
        return np.eye(3)

    skew_symmetric = np.array([[0, -rot_axis[2], rot_axis[1]],
                                [rot_axis[2], 0, -rot_axis[0]],
                                [-rot_axis[1], rot_axis[0], 0]])

    R = np.eye(3) + skew_symmetric + skew_symmetric @ skew_symmetric * (1/(1+cos))
    rotated_vec = R @ vec
    if abs(rotated_vec[2]) < 1e-12:
        rotated_vec[2] = 0.0

    return rotated_vec

rel_pos = rotation_matrix(rel_pos)[:2]
rel_vel = rotation_matrix(rel_vel)[:2]

def cart2pol(vec):
    if len(vec) > 2:
        raise TypeError("Only 2d vectors")
    r = np.sqrt(vec[0]**2 + vec[1]**2)
    theta = np.arctan2(vec[1], vec[0])
    return r, theta

r, theta = cart2pol(rel_pos)
rdot, thetadot = cart2pol(rel_vel)
udot = 1/rdot

l = r * rdot * np.sin(thetadot) # angular velocty per unit mass

def rwiththeta(theta, u, G, mu, l):
    d2udo2 = -u + (G * mu) / (l**2)
    return d2udo2

o_0 = 0
o_f = 2 * np.pi
o_points = np.linspace(o_0, o_f,4000)

params = (G, mu, l)

def ode_system(theta, u):
    return [rwiththeta(theta, u[0], G, mu, l)]


initial_u = [1/r]
result = solve_ivp(ode_system, [o_0, o_f],  initial_u, t_eval = o_points)
u_theta = result.y[0]
r_theta = 1/ u_theta


# fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
# ax.plot(o_points, r_theta)
# plt.show()

k = G * (body1.mass() + body2.mass())
initial = np.concatenate([rel_pos, rel_vel])

time = (0, 24* 3600* 31)
time_eval = np.linspace(time[0], time[1], 1000)

def motion(t, state):
    x, y, v_x, v_y = state
    r = np.sqrt(x**2 + y**2)

    a_x = - G * body1.mass() * x / r**3
    a_y = - G * body1.mass() * y / r**3

    return [v_x, v_y, a_x, a_y]

sol = solve_ivp(motion, time, initial, t_eval = time_eval, rtol = 1e-9, atol = 1e-9)

x_orbit = sol.y[0]
y_orbit = sol.y[1]

print(body1.mass())
print(body2.mass())

plt.figure(figsize = (8,8))
plt.plot(x_orbit, y_orbit)
plt.scatter(0,0, s=100, color = 'red')
plt.grid(True)
plt.show()




