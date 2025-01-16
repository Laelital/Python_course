# Сформировать и заполнить массив случайными числами 
# и вывести максимальное, минимальное и среднее значение
# Использовать метод math.random(), который возвр [0, 1]
import random                          # Импортируем метод random
list = []                              # Сформировываем список
for _ in range(int(input())):          
    list.append(random.uniform(0, 1))  # Заполнение случайными числами [0, 1]. Используется метод random.uniform (Python) аналогичный math.random (Java)

print(max(list))                       # Вывод максимального значения
print(min(list))                       # Вывод минимального значения
print(sum(list)/len(list))             # Вывод среднего значения


# квадратный корень n = math.sqrt(4) 
# округление числа вверх n2 = math.ceil(3.8)
# округление числа вниз n3 = math.floor(3.8)
# from math import * # импорт всех функций модуля
# num1 = sqrt(2)
# num2 = ceil(3.8)   
# num3 = floor(3.8)  
# print(num1, num2, num3)