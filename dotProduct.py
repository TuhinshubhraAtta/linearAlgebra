import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# logic for dot product
result = np.dot(a, b) # a.b = (1)(4) + (2)(5) + (3)(6) = 4 + 10 + 18 = 32
# for vectors, @ also works for dot product. e.g., result = a @ b
print("Result of dot product:", result)