import numpy as np

#Завдання 16

array = np.random.uniform(1, 11, size=(5, 5))

# Масив з абсолютними значеннями елементів
abs_array = np.abs(array)

# Масив з квадратами елементів
squared_array = np.square(array)

# Масив з експонентами елементів
exp_array = np.exp(array)

# Масив з синусами елементів
sin_array = np.sin(array)

# Масив з знаками кожного елементу
sign_array = np.sign(array)

# Масив з дробовими та цілими частинами елементів
fractional_part = array - np.floor(array)  # Дробова частина
integer_part = np.floor(array)  # Ціла частина

print("\nArray:\n")
print(array)

print("\nAbsolute array:\n")
print(abs_array)

print("\nSquared array\n:\n")
print(squared_array)

print("\nExponentiated array:\n")
print(exp_array)

print("\nArray with sines of elements:\n")
print(sin_array)

print("\nArray with signs of the elements:\n")
print(sign_array)

print("\nFractional array:\n")
print(fractional_part)

print("\nInteger array:\n")
print(integer_part)