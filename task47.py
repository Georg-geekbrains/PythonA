# Задача N°47. Решение задачи
# У вас есть коД, который вы не можете менять (так часто бывает, когда код в глубине программы используется
#  множество раз и вы не хотите ничего сломать):
# transformation = <???>
# valtès = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений,
# а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed values получился копией values.
# Примет
#Ввод:
# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(trasformation, values))
# if values == transformed values:
# print('ok') h
# else:
# print('fail')
# Skillbox
# proxies
# Вывод:
# ok

trasformation = lambda x: x
values = [1, 23, 42, 'asdfg']
transformed_values = list(map(trasformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')