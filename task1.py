# Задача 30:  
# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

from numpy import arange

start_num   = int(input("Введите значение первого элемента прогресии: "))
step        = int(input("Введите шаг прогрессии: "))
size        = int(input("Введите количество элементов прогрессии: "))
progression = arange(start_num, start_num + (size-1) * step + 1, step).tolist()
print(*progression)
print(*[i for i in range(start_num, start_num + (size-1) * step + 1, step)])