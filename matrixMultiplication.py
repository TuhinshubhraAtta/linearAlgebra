"""
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

AB = [1(5) + 2(7), 1(6) + 2(8)],
     [3(5) + 4(7), 3(6) + 4(8)]
    = [[19, 22],
       [43, 50]]
"""

import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C = A @ B  # Matrix multiplication using the @ operator
# Alternatively, you can use np.matmul for matrix multiplication

print("Result of matrix multiplication:")
print(C)