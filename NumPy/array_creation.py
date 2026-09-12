"""
-> Array creation
- numpy.array()
- numpy.zeros()
- numpy.ones()
- numpy.arange()
- numpy.linspace()
"""

import numpy as np

x = np.zeros((2, 3))
print(x)

"""
মানে 2 rows × 3 columns-এর array।
"""

# Shape
print(x.shape)

x = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(x.shape)

"""
Output: (2, 3)

অর্থ:
2 rows
3 columns
"""

# Dimension
print(x.ndim)


# Data type
print(x.dtype)


# Indexing এবং slicing
print(x[0])
print(x[0, 1])
print(x[:, 1])
print(x[1, :])


# Vectorized operation
x = np.array([7, 8, 9, 10])
print(x * 2)


# Aggregation
print(x.sum())
print(x.mean())
print(x.min())
print(x.max())
print(x.std())


# Matrix multiplication
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

C = A @ B

print(C)

"""
এখানে, @ matrix multiplication-এর জন্য ব্যবহৃত হচ্ছে।
"""

