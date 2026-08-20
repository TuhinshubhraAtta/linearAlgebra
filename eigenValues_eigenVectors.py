import numpy as np

A = np.array([[1, 2], [3, 4]])

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