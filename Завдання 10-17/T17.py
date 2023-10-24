import numpy as np

#Завдання 17#
import random

array = np.array([random.randint(1, 10) for _ in range(5)])


print("\nYour array:\n")
print(array)

accumulative_sums = np.zeros_like(array, dtype=int)
accumulative_products = np.zeros_like(array, dtype=int)

for i in range(array.shape[0]):
    if i == 0:
        accumulative_sums[i] = array[i]
        accumulative_products[i] = array[i]
    else:
        accumulative_sums[i] = accumulative_sums[i - 1] + array[i]
        accumulative_products[i] = accumulative_products[i - 1] * array[i]

print("\nArray with increasing sums:\n")
print(accumulative_sums)
print("\nArray with increasing products:")
print(accumulative_products)


