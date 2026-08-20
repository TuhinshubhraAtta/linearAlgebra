"""
Consider:

x + 2y = 5
3x + 4y = 6

We can write this as:
    Ax = b

Where:
A = [[1, 2],
     [3, 4]]

x = [x, y]

b = [5, 6]
"""

import numpy as np

A = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])

x = np.linalg.solve(A, b)  # Solving the linear equation Ax = b
print("Solution of the linear equation Ax = b:")
print(x)