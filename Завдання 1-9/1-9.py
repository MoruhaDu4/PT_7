import numpy as np

#Завдання 1#
print("Task 1:")

my_array1 = np.array([[1, 2, 3],
                     [4, 5, 6]], dtype=int)

print(my_array1)

#Завдання 2#

print("\nTask 2:")

my_array2_1 = np.array([[1.0, 2.5, 3.14],
                     [ 0.5, 9.8, 6.2]], dtype=float)

my_array2_2 = np.array([[2 + 3j, 1 - 2j, 4 + 0.5j],
                     [2 + 3j, 1 - 2j, 4 + 0.5j]], dtype=complex)


print("\nArray with elements float:")
print(my_array2_1)

print("\nArray with elements complex:")
print(my_array2_2)

#Завдання 3#

print("\nTask 3:")

my_array_3 = np.zeros((4, 3), dtype=int)

print(my_array_3)

#Завдання 4#

print("\nTask 4:")

my_array_4 = np.ones((5, 3), dtype=int)

print(my_array_4)

#Завдання 5#

print("\nTask 5:")

unit_matrix = np.eye(4, dtype=int)

print(unit_matrix)

#Завдання 6#

print("\nTask 6:")

empty_array = np.empty((4, 4))

print(empty_array)

#Завдання 7#

print("\nTask 7:")

my_array_7 = np.arange(2, 11, 2)

print(my_array_7)

#Завдання 8#

print("\nTask 8:")

my_array_8 = np.linspace(20, 30, 10, dtype=float)

print(my_array_8)

#Завдання 9#

print("\nTask 9:")

rows, cols = 4, 5

my_array_9 = np.fromfunction(lambda i, j: i + 4 * j, (rows, cols), dtype=int)

print(my_array_9)