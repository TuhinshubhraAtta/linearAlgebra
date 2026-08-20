import numpy as np

A = np.array([[3, 1, 2], [2, 4, 1], [1, 2, 3]])
b = np.array([10, 12, 13])

print (A.shape)
print (A.T)
print (np.linalg.det(A))
print (np.linalg.matrix_rank(A))
print (np.linalg.inv(A))
print (np.linalg.solve(A, b))

eigenvalues, eigenvectors = np.linalg.eig(A)  # Eigenvalues and eigenvectors of matrix A
print("Eigenvalues of matrix A:", eigenvalues)
print("Eigenvectors of matrix A:", eigenvectors)

print("Verification: A * v = λ * v for each eigenvalue and eigenvector pair:")
for i in range(len(eigenvalues)):
    v = eigenvectors[:, i]
    lambda_v = eigenvalues[i] * v
    Av = np.dot(A, v)
    print(f"Eigenvalue {eigenvalues[i]}:")
    print("A * v =", Av)
    print("λ * v =", lambda_v)
    print("Are they approximately equal?", np.allclose(Av, lambda_v))