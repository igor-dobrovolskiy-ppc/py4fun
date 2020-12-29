# random example together with one body bigger mass than others
from py4fun.gravity_simulation.gravity import *


def sample(file_name):
    def add_body(fld, mass, r_x, r_y, r_0, velocity, alpha):
        v = velocity
        a = alpha
        radius_x = r_x
        radius_y = r_y
        m = mass
        fld.add_body(Body(r_0 + radius_x*np.cos((a/360)*2*np.pi), r_0 + radius_y*np.sin(
            (a/360)*2*np.pi), v*np.cos((a/360)*2*np.pi), v*np.sin((a/360)*2*np.pi), mass=m))

    field = GravityField()

    # field.generate_random(15, mass=[20, 100], r_x=[-10, 10], r_y=[-10, 10], r_0=10, velocity=[-3, 3], alpha=[0, 360])
    # field.add_body(Body(x0=0, y0=0, v_x=0, v_y=0, mass=300))

    # field.generate_random(4, mass=[5, 10], r_x=[-10, 10], r_y=[-10, 10], r_0=10, velocity=[-10, 10], alpha=[0, 360])

    add_body(field, 5, 10, 10, 0, 10, 0)
    add_body(field, 20, -10, -10, 0, -10, 120)
    add_body(field, 100, 0, 0, 100, 0, 240)

    field.add_body(Body(x0=0, y0=0, v_x=0, v_y=0, mass=10000))

    field.run(5000, C=0.01)
    field.save_animation(frames=400, name=file_name, reduce_size_body=50)
