import numpy as np

A = np.array([[1, 2], [3, 4]])

A_inv = np.linalg.inv(A)  # Inverse of matrix A
print("Inverse of matrix A:")
print(A_inv)
print("Verification (A * A_inv):")
# Verify that A * A_inv is the identity matrix
I = np.dot(A, A_inv)
print(I)