# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#         print(summa)

# sum_numbers(5)

# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa

# print(sum_numbers(5))

# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa
# a = sum_numbers(5)
# print(a)

# def sum_numbers(n, y = 'Hello'):
#     print(y)
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa
# a = sum_numbers(5)
# print(a)

# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res
# print(sum_str('q','e','l'))
# print(sum_str('q','e','l','q','e','l'))
 

 #Mодульность

# import Lesson7Modul

# print(Lesson7Modul.max1(5,9))
#------------------------
# from Lesson7Modul import max1

# print(max1(5,9))
#------------------------
# from Lesson7Modul import *

# print(max1(10,9))

#------------------------
# import Lesson7Modul as m1
# print(m1.max1(10,9))
#------------------------

# Рекурсия

# def fib(n):
#     if n in[1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)
# list_1 = []
# for i in range(1,10):
#     list_1.append(fib(i))
# print(list_1)
#------------------------------

#Алгоритмы
#Быстрая сортировка
# def quik_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quik_sort(less) + [pivot] + quik_sort(greater)
# print(quik_sort([14,5,9,6,3,58,7,5,2,7]))

#Сортировка слиянием

def merge_sort(nums):
    if len(nums) >1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and  j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
list1 = [1,5,9,8,7,2,1,55,2,4]
merge_sort(list1)
print(list1)
        




