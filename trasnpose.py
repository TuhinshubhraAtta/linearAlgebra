"""
A = [[1, 2],
     [3, 4]]

A_T = [[1, 3],
       [2, 4]]
"""

import numpy as np

A = np.array([[1, 2], [3, 4]])
A_T = A.T  # Transpose of matrix A
print("Original matrix A:")
print(A)
print("Transpose of matrix A:")
print(A_T)