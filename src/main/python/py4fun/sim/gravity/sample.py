#random example together with one body bigger mass than others
from gravity_simulation.gravity import *

def sample():
    field = GravityField()

    field.generate_random(15, mass=[20, 500], r_x=[-5, 5], r_y=[-5, 5], velocity=[-5, 5], alpha=[0, 360])
    field.add_body(Body(x0=0, y0=0,v_x=0, v_y=0, mass = 3000))

    field.run(1300, C=0.01)
    field.save_animation(frames=50,name='my_example',reduce_size_body=50)
