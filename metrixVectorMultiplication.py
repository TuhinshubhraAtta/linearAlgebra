"""
A = [[1, 2],
     [3, 4]]

x = [5, 6]

Ax = [1(5) + 2(6),
          3(5) + 4(6)]
         = [17, 39]
"""

import numpy as np

A = np.array([[1, 2], [3, 4]])
x = np.array([5, 6])

result = A @ x  # Matrix-vector multiplication using the @ operator
# Alternatively, you can use np.dot for matrix-vector multiplication

print("Result of matrix-vector multiplication:")
print(result)