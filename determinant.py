"""
For a square matrix (2x2, 3x3, etc.) A, the determinant is a scalar value that can be computed using the formula:
det(A) = a11 * (a22 * a33 - a23 * a32) - a12 * (a21 * a33 - a23 * a31) + a13 * (a21 * a32 - a22 * a31)
Where aij represents the element in the ith row and jth column of matrix A.

det(A) = ad - bc
det(A) = 1(4) - 2(3) = 4 - 6 = -2
"""

import numpy as np

A = np.array([[1, 2], [3, 4]])
det_A = np.linalg.det(A)  # Determinant of matrix A
print("Determinant of matrix A:", det_A)