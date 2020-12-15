from typing import Callable
import numpy as np

def solve_euler_explicit(f: Callable, x0: float, dt: float, t0: float, tf: float):
    """
    This function applies an explicit Euler scheme to numerically calculate the points of a function x defined by its first
    derivative function f, using a set time step, on a set time interval.
    
    :param f: The derivative function of x, as f(t, x)
    :param x0: The initialisation point (= x(t0))
    :param dt: The calculation time step
    :param t0: The initial time (left bound of the time interval)
    :param tf: The final time (right bound of the time interval)
    
    :returns: The array of time points and the array of values of the x function
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
        
        # Calculate the approximation function for the integral (rectangle approximation on the left)
        gradient_diff = time_delta * f(time_previous, x_previous)

        # Calculate x_current
        x_current = x_previous + gradient_diff

        # Add to the points array
        points_array[time_index] = x_current

    return time_array, points_array



### Newton function from the UE11-calcul-differentiel GitHub repository
def Newton(F:Callable, x0:float, y0:float, eps:float=eps, N:int=N) -> tuple:
    """
    This function solves the equation F(x,y) = 0 around (x0,y0) using the Newton algorithm.

    :param F: The function to solve for — it must necessarily have a multi-dimensional image in a np.ndarray type
    :param x0: The initial x-axis coordinate
    :param y0: The initial y-axis coordinate
    :param eps: The acceptable precision of the algorithm
    :param N: The maximum number of iterations (will raise an error if exceeded)

    :returns: The solution to the equation F(x,y) = 0, to a precision of eps
    """

    #   0. Troubleshooting types (ugly)
    x0, y0 = float(x0), float(y0)

    #   1. Defining the X0 point
    X0 = np.array([x0, y0])

    #   2. Generating the jacobian matrix of F (n-dimensional derivative)
    jacF = DFunc.jacobian(F)

    #   3. Running the method in a loop to refine the calculation
    for iter_counter in range(N):

        #   3.1. Inverting F's jacobian matrix
        try:
            jacF_inv = npy.linalg.inv( jacF( *(X0.tolist()) ) )
        except npy.linalg.linalg.LinAlgError:
            raise ValueError('The function to solve for has got a singular jacobian matrix in the desired point.')

        #   3.2. Dot product between jacF and F(X0)
        F_dot = npy.dot( jacF_inv, F( *(X0.tolist()) ) )

        #   3.3. Computing the new X point
        X = X0 - F_dot

        #   3.4. Exiting the function once the desired precision is reached
        if npy.linalg.norm( X - X0 ) <= eps:
            return tuple(X.tolist())

        #   3.5. Performing end-of-loop actions
        X0 = X.copy()

    #   4. Raising an error when no solution is found and the max number of iterations is exceeded
    raise ValueError(f'No convergence in {N} steps.')



eps = 10**-7  # to change later, maybe
def solve_euler_implicit(f: Callable, x0: float, dt: float, t0: float, tf: float, itermax:int=100):
    """
    This function applies an implicit Euler scheme to numerically calculate the points of a function x defined by its first
    derivative function f, using a set time step, on a set time interval.
    
    :param f: The derivative function of x, as f(t, x)
    :param x0: The initialisation point (= x(t0))
    :param dt: The calculation time step
    :param t0: The initial time (left bound of the time interval)
    :param tf: The final time (right bound of the time interval)
    :param itermax: The maximum number of iterations for solving the equation using the Newton algorithm
    
    :returns: The array of time points and the array of values of the x function
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
        
        # Calculate the function to solve for using the Newton algorithm
        def F(X, _):
            return x_previous - X + time_delta * f(time_current, X)

        # Calculate x_current
        x_current = Newton(F=F, x0=x_previous, y0=0, eps=eps, N=itermax) [0]  # intialise around the previous point
        
        # Add to the points array
        points_array[time_index] = x_current

    return time_array, points_array
