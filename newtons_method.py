# Name: Sarah Shakim      
# Student ID: 20824519

import numpy as np
import math as m

def newtons_method(x0, f, dfdx, e_tol, N_max = 500):
    """
    Finds the root of a single equation using Newton's method.

    :param x0:      Initial guess for the root.
    :param f:       Function to find the root, takes one input gives one output.
    :param dfdx:    The derivative of the function.
    :param e_tol:   The relative error tolerance.
    :param N_max:   The maximum number of iterations. Default 500.

    :return:        1. The value of the root
                    2. The final relative error
                    3. The number of iterations taken
    """
    # Initializing a value for the error to compare it to the tolerance
    err = 1000
    # Setting the inital guess to a variable
    x = [x0] 
    # Initializing counter for the loop
    i=0
    # Initializing counter for the amount of iterations
    N=0
    # Looping through the value for the initial guess to see if the error for that value will be less than the tolerance value.
    while e_tol<err and i<N_max:
        # Calculating the value for the next guess with the Newton Rhapson method.
        new_x = x[i]-f(x[i])/(dfdx(x[i]))

        x.append(new_x)
        # Calculating the value for the error
        err = abs((x[i+1]-x[i])/(x[i+1])) * 100
        i+=1
        N+=1

    # checks when while loop has ended
    # check to see if the answer diverges after the while loop
    if e_tol<err:
        print("Could not find the root")
    return x[-1], err, N

(x_value, error, iterations) = newtons_method(2, lambda x: m.exp(-x) - x, lambda x: -m.exp(-x)-1, 10**2)

print(x_value, error, iterations)
