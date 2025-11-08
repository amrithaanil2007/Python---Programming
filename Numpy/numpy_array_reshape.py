import numpy as np

# Original array
original_array = np.array([1, 2, 3, 4, 5, 6])
print(original_array)
print(original_array.shape)

# Reshape to 2 rows and 3 columns
reshaped_array = original_array.reshape(2, 3)
print(reshaped_array)
print(reshaped_array.shape)

#3d
reshaped_three_d = original_array.reshape(2, 1, 3)
print(reshaped_three_d)
print(reshaped_three_d.shape)

auto_reshape = original_array.reshape(2, -1)
print(auto_reshape)
print(auto_reshape.shape)