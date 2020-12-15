from typing import Callable

import numpy as np

def solve_euler_explicit(f: Callable, x0, dt, t0, tf):
    

    time_points = np.ceil( (tf - t0) / dt )  # will round up
    


    for point in time_points:
        pass




    return t, x