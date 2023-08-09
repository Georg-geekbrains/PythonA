# Напишите рекурсивную функцию sum(a,b) возвращающню суььу двух целых неотрицательных чисел.
# Из всех арифметически операций допускаются только +1 и -1

a = int(input('Input a: '))

b = int(input('Input b: '))

def sum(a,b):
    if b == 0:
        return a
    elif a == 0:
         return b
    else:
        return sum(a + 1, b - 1)


print(sum(a,b))