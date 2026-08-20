"""
I = [[1, 0],
     [0, 1]]
     
A = [[1, 2],
     [3, 4]]
     
AI = [[1, 2],
      [3, 4]]
      
IA = [[1, 0],
      [0, 1]]
"""

import numpy as np

A = np.array([[1, 2], [3, 4]])

I = np.eye(2)  # Create a 2x2 identity matrix
print("Identity matrix I:")
print(I)

# Multiply matrix A with the identity matrix I
result = A @ I
print("Result of matrix multiplication with identity matrix:")
print(result)