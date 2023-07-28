# Семинар 4. Словари, множества и профилирование
# Задача N°25. Решение задачи
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _п.
# Input: a a a b caad cd d
# Output:aa_1a_2bca_3 a_4d c_1 d_1 d_2
# Skillbox
# Для решения данной задачи используйте функцию
# .splitO

stroka = input().split()
res = {}
for i in stroka:
    if i in res:
        print(f'{i}_{res[i]}', end= ' ')
    else:
        print(i, end= ' ')
    res[i] = res.get(i, 0) + 1