
# Семинар 5.
# Задача N°35. Решение задачи
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и п(само число)
# Input: 5
# Output: ves

def f(n):
    if n == 0:
        return ''
    k = int(input())
    return f(n-1) + f'{k}'
# n= 2
# 3
# 4
#                 + '4'  + '3'
n = int(input())

print(f(n))