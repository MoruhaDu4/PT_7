import numpy as np

#Завдання 10#

import random

n = 4  

c = np.random.randint(1, 10, size=n)  
d = np.random.randint(1, 10, size=n)

print("\nArray c:\n")
print(c)

print("\nArray d:\n")
print(d)

# Різниця масивів
difference = c - d

# Сума масивів
sum_result = c + d

# Піднесення до квадрату всіх елементів
squared_c = c**2
squared_d = d**2

# Попарний добуток відповідних елементів
multiply = c * d

# Попарна частка відповідних елементів
division = c / d

# Піднесення елементів масиву c до відповідних степенів, які є елементами масиву d
powered_c = c**d


print("\narray difference:\n")
print(difference)

print("\narray sum:\n")
print(sum_result)

print("\nelevation to the square of the array c:\n")
print(squared_c)

print("\nelevation to the square of the array d\n")
print(squared_d)

print("\nMultiply arrays (c*d):\n")
print(multiply)

print("\nDivision arrays (c/d):\n")
print(division)

print("\npowered c (c^d):\n")
print(powered_c)