"""
The length of a vector is called its magnitude or norm. The magnitude of a vector is calculated using the formula:
||v|| = sqrt(v1^2 + v2^2 + ... + vn^2)
"""

import numpy as np

a = np.array([1, 2, 3])

result = np.linalg.norm(a)
print("Result of vector magnitude:", result)