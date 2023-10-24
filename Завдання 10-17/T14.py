import numpy as np

#Завдання 14

array = np.random.randint(-10, 11, size=(4, 3))

print("\nYour array:\n")
print(array)

# Середнє значення всіх елементів масиву
average_of_all_elements = np.mean(array)

# Середнє значення по кожному рядку
average_per_row = np.mean(array, axis=1)

# Середнє значення по кожному стовпцю
average_per_column = np.mean(array, axis=0)


print("\nArray: average of all elements 'your array':\n", average_of_all_elements)
print("\nArray: average per row 'your array':\n", average_per_row)
print("\nArray: average per column 'your array':\n", average_per_column)


array[array >= 0] = 5  # Замінить невід'ємні значення на 5

print("\nNew array '>= 0' -> '5':\n")
print(array)

array[array > 0] = 3  # Замінить додатні значення на 3

print("\nNew array '> 0' -> '3':\n")
print(array)
