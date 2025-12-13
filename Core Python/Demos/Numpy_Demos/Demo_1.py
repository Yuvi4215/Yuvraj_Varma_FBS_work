"""
NUMPY COMPLETE IMPORTANT METHODS
================================

This file is a consolidated, interview-ready and practical guide
covering all important NumPy concepts used in:

• Data Analysis
• Machine Learning
• Scientific Computing
• Performance-critical applications

Covers:
1. Why NumPy (Performance vs Python Lists)
2. Array Creation Methods
3. Array Attributes
4. Indexing & Slicing
5. Reshaping & Manipulation
6. Vectorized Mathematical Operations
7. Aggregation & Statistics
8. Broadcasting
9. Linear Algebra (numpy.linalg)
10. Random Data Generation
11. Comparison & Boolean Masking

Author: Practical + Interview Reference
"""

import numpy as np
import time

# ============================================================
# 1. WHY NUMPY? — PERFORMANCE COMPARISON
# ============================================================

print("\n1. PERFORMANCE: NumPy vs Python Lists")

size = 1_000_000

# Python List
list1 = range(size)
list2 = range(size)
start = time.time()
result_list = [x + y for x, y in zip(list1, list2)]
print(f"Python List Time: {time.time() - start:.6f} sec")

# NumPy Array
arr1 = np.arange(size)
arr2 = np.arange(size)
start = time.time()
result_array = arr1 + arr2
print(f"NumPy Array Time : {time.time() - start:.6f} sec")

# ============================================================
# 2. ARRAY CREATION METHODS
# ============================================================

print("\n2. ARRAY CREATION")

# From list / tuple
arr_list = np.array([1, 2, 3, 4])
arr_tuple = np.asarray((5, 6, 7))

# Zeros & Ones
zeros_arr = np.zeros((3, 3))
ones_arr = np.ones((2, 4), dtype=int)

# Range based
arange_arr = np.arange(0, 10, 2)
linspace_arr = np.linspace(0, 1, 5)

# Identity matrix
identity = np.eye(3)

print(arr_list, arr_tuple)
print(zeros_arr)
print(ones_arr)
print(arange_arr)
print(linspace_arr)
print(identity)

# ============================================================
# 3. ARRAY ATTRIBUTES (VERY IMPORTANT)
# ============================================================

print("\n3. ARRAY ATTRIBUTES")

attr_arr = np.array([[1, 2, 3], [4, 5, 6]])

print("ndim     :", attr_arr.ndim)
print("shape    :", attr_arr.shape)
print("size     :", attr_arr.size)
print("dtype    :", attr_arr.dtype)
print("itemsize :", attr_arr.itemsize)

# ============================================================
# 4. INDEXING & SLICING
# ============================================================

print("\n4. INDEXING & SLICING")

one_d = np.array([10, 20, 30, 40, 50])
two_d = np.array([[1, 2, 3], [4, 5, 6]])

print(one_d[0])
print(one_d[1:4])
print(two_d[1, 2])
print(two_d[:, 1])

# ============================================================
# 5. RESHAPING & MANIPULATION
# ============================================================

print("\n5. RESHAPING & MANIPULATION")

reshape_arr = np.arange(1, 13)
reshaped = reshape_arr.reshape(3, 4)

flattened = reshaped.flatten()   # copy
raveled = reshaped.ravel()       # view
transposed = reshaped.T

print(reshaped)
print(flattened)
print(transposed)

# ============================================================
# 6. VECTORIZED MATHEMATICAL OPERATIONS
# ============================================================

print("\n6. MATHEMATICAL OPERATIONS")

math_arr = np.array([10, 20, 30, 40])

print(math_arr + 5)
print(math_arr * 2)
print(math_arr ** 2)

# Universal Functions (ufuncs)
print(np.sqrt(math_arr))
print(np.log(math_arr))
print(np.exp(math_arr))

# ============================================================
# 7. AGGREGATION & STATISTICS
# ============================================================

print("\n7. AGGREGATION FUNCTIONS")

stats_arr = np.array([[10, 20, 30],
                      [40, 50, 60]])

print("Sum       :", np.sum(stats_arr))
print("Mean      :", np.mean(stats_arr))
print("Median    :", np.median(stats_arr))
print("Std Dev   :", np.std(stats_arr))
print("Min       :", np.min(stats_arr))
print("Max       :", np.max(stats_arr))

print("Col-wise Sum :", np.sum(stats_arr, axis=0))
print("Row-wise Mean:", np.mean(stats_arr, axis=1))

# ============================================================
# 8. BROADCASTING
# ============================================================

print("\n8. BROADCASTING")

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
vector = np.array([10, 20, 30])

print(matrix + vector)

# ============================================================
# 9. LINEAR ALGEBRA (numpy.linalg)
# ============================================================

print("\n9. LINEAR ALGEBRA")

A = np.array([[2, 1],
              [1, 3]])
B = np.array([5, 6])

print("Dot Product:\n", np.dot(A, A))
print("Matmul:\n", np.matmul(A, A))
print("Determinant:", np.linalg.det(A))
print("Inverse:\n", np.linalg.inv(A))
print("Solve Ax=B:", np.linalg.solve(A, B))

# Additional operations
print("Vdot :", np.vdot(A, A))
print("Inner:\n", np.inner(A, A))

# ============================================================
# 10. RANDOM DATA GENERATION
# ============================================================

print("\n10. RANDOM MODULE")

np.random.seed(42)

rand_uniform = np.random.rand(3, 3)
rand_int = np.random.randint(1, 100, 10)
rand_normal = np.random.randn(5)

print(rand_uniform)
print(rand_int)
print(rand_normal)

# ============================================================
# 11. COMPARISON & BOOLEAN MASKING
# ============================================================

print("\n11. BOOLEAN MASKING")

filter_arr = np.array([10, 25, 30, 45, 50])
mask = filter_arr > 30

print("Mask :", mask)
print("Filtered Values:", filter_arr[mask])

# ============================================================
# END OF FILE
# ============================================================

"""
INTERVIEW TAKEAWAYS:
• NumPy arrays are faster and memory-efficient
• Vectorization eliminates Python loops
• Broadcasting enables operations on different shapes
• numpy.linalg supports optimized matrix operations
• NumPy is the foundation of Pandas, SciPy, ML & DL
"""
