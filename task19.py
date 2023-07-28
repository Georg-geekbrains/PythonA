# Семинар 3. Списки и словари
# Задача N°19. Решение задачи
# Дана последовательность из N целых чисел и число
# К. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на К элементов вправо, К - положительное число.
# Input: [1, 2, 3, 4, 5]k = 3
# Output: [3, 4, 5, 1, 2, ]
# Примечание: Пользователь может вводить значения списка или список задан изначально.

list = [1,2,3,4,5]
k = int(input())
k = k % len(list)
#i=1
#print(list[len(list)-1-i])

listres = []
for i in range(k):
    listres.append(list[len(list)-1-i])
    #print(listres[i])
print(listres)
for i in range(len(list)-k):
    listres.append(list[i])
print(listres)
