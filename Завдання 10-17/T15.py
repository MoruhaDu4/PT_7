import numpy as np

# Завдання 15


array1 = np.random.randint(1, 11, size=(5, 5))
array2 = np.random.randint(1, 11, size=(5, 5))

print("\narray1:\n")
print(array1)

print("\narray2:\n")
print(array2)

elementwise_maximum = np.maximum(array1, array2)
elementwise_minimum = np.minimum(array1, array2)

print("\nmaximums of array1 and array2:\n")
print(elementwise_maximum)

print("\nminimums of array1 and array2:\n")
print(elementwise_minimum)