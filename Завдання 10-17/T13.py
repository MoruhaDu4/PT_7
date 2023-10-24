import numpy as np

#Завдання 13

array = np.random.randint(1, 10, size=(3, 5))

print("\nYour array:\n")
print(array)

# Сума всіх елементів масиву
sum_of_elements = np.sum(array)

# Мінімальний елемент масиву
min_element = np.min(array)

# Максимальний елемент масиву
max_element = np.max(array)

# Мінімальні елементи в кожному стовпці (стовпцевий мінімум)
min_in_columns = np.min(array, axis=0)

# Максимальні елементи в кожному стовпці (стовпцевий максимум)
max_in_columns = np.max(array, axis=0)

# Мінімальні елементи в кожному рядку (рядковий мінімум)
min_in_rows = np.min(array, axis=1)

# Максимальні елементи в кожному рядку (рядковий максимум)
max_in_rows = np.max(array, axis=1)

# Індекси мінімального елементу
min_index = np.unravel_index(np.argmin(array), array.shape)

# Індекси максимального елементу
max_index = np.unravel_index(np.argmax(array), array.shape)

print("\nsum elements of array:\n", sum_of_elements)
print("\nmin element of array:\n", min_element)
print("\nmax element of array:\n", max_element)
print("\nmin element in columns:\n", min_in_columns)
print("\nmax element in columns:\n", max_in_columns)
print("\nmin element in rows:\n", min_in_rows)
print("\nmax element in rows:\n", max_in_rows)
print("\nindex of min element:\n", min_index)
print("\nindex of max element:\n", max_index)