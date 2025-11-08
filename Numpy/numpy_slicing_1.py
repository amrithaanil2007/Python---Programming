import numpy as np

# 1-D array
scores_array = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(scores_array)

# Slicing: from index 2 to 4 (5 is excluded)
sliced_array = scores_array[2:5]
print(sliced_array)

# Different slice operations
print(scores_array[:4])
print(scores_array[5:])
print(scores_array[:])      
print(scores_array[::2])
print(scores_array[:3])
print(scores_array[-3:])