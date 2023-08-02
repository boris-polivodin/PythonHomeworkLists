# Задача 32: 
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

down_value  = int(input("Введите нижнюю границу диапазона: "))
up_value    = int(input("Введите верхнюю границу диапазона: "))
size        = int(input("Задайте размер массива: "))
array       = [randint(-10, 10) for i in range(size)]
ind         = []
for i in range(0, len(array)):
    if array[i] in range(down_value, up_value + 1):
        ind.append(i)
print(array)
print(ind)