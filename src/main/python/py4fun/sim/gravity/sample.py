# random example together with one body bigger mass than others
from gravity_simulation.gravity import *


def sample(file_name):
    field = GravityField()

    field.generate_random(15, mass=[20, 100], r_x=[-10, 10], r_y=[-10, 10], r_0=10, velocity=[-3, 3], alpha=[0, 360])
    field.add_body(Body(x0=0, y0=0, v_x=0, v_y=0, mass=300))

    field.run(10000, C=0.01)
    field.save_animation(frames=320, name=file_name)     # , reduce_size_body=50)
