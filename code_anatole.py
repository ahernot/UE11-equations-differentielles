from typing import Callable
import numpy as np

def solve_euler_explicit(f: Callable, x0: float, dt: float, t0: float, tf: float):
    """
    This function applies an Euler scheme to numerically calculate the points of a function x defined by its first derivative function f, using a set time step, on a set time interval.
    :param f: The derivative function of x, as f(t, x)
    :param x0: The initialisation point (= x(t0))
    :param dt: The calculation time step
    :param t0: The initial time (left bound of the time interval)
    :param tf: The final time (right bound of the time interval)
    """

    # Initialise the arrays for time and points
    time_array = np.arange(t0, tf, dt)
    points_array = np.empty_like(time_array)

    # Get the number of time points
    time_len = time_array.shape[0]

    # Fill the initial value
    points_array[0] = x0


    for time_index in range(1, time_len):
        # Get the previous point
        x_previous = points_array[time_index - 1]
        
        # Calculate the time delta between both calculations
        time_previous = time_array[time_index - 1]
        time_current = time_array[time_index]
        time_delta = time_current - time_previous
        
        # Calculate the approximation function for the integral
        gradient_diff = time_delta * f(time_previous, x_previous)

        # Calculate x_current and add to the points array
        x_current = x_previous + gradient_diff
        points_array[time_index] = x_current

    return time_array, points_array