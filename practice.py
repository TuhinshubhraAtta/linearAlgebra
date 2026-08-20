"""
Given Vectors:
    a = [1, 2, 3]
    b = [4, 5, 6]

Given Metrices:
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
"""

import numpy as np

# Vector Operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Vector addition:", a + b)
print("Vector subtraction:", a - b)
print("Vector scalar multiplication (a * 2):", a * 2)
print("Vector scalar multiplication (b * 3):", b * 3)
print("Vector dot product:", np.dot(a, b))
print("Vector cross product:", np.cross(a, b))
print("Vector magnitude of a:", np.linalg.norm(a))
print("Vector magnitude of b:", np.linalg.norm(b))
print("Vector Element-wise multiplication:", a * b)

# Matrix Operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix addition:\n", A + B)
print("Matrix subtraction:\n", A - B)
print("Matrix scalar multiplication (A * 2):\n", A * 2)
print("Matrix scalar multiplication (B * 3):\n", B * 3)
print("Matrix multiplication (A * B):\n", A @ B)
print("Matrix transpose:\n", A.T)
print("Matrix determinant of A:", np.linalg.det(A))
print("Matrix determinant of B:", np.linalg.det(B))
print("Matrix inverse of A:\n", np.linalg.inv(A))
print("Matrix inverse of B:\n", np.linalg.inv(B))

# Metrix-Vector Multiplication
print("Matrix-Vector multiplication (A * a):\n", A @ a[:2])  # Using first two elements of a to match dimensions

# Solving Linear Equations
A = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])

x = np.linalg.solve(A, b)
print("Solution of the linear equation Ax = b:\n", x)

# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues of matrix A:", eigenvalues)
print("Eigenvectors of matrix A:\n", eigenvectors)

eigenvalues_B, eigenvectors_B = np.linalg.eig(B)
print("Eigenvalues of matrix B:", eigenvalues_B)
print("Eigenvectors of matrix B:\n", eigenvectors_B)