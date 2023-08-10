# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

n = int(input("Input array's length: "))
min = int(input("Input min value: "))
max = int(input("Input max value: "))

arr = []
arr2 = []
for i in range(n):
    arr.append(random.randint(-10,10))
        
print(arr)

for i in range(len(arr)):
    if  arr[i] > min and arr[i] < max:
        arr2.append(i)
print(arr2)