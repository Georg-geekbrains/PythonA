# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

p = int(input("Произведение двух загаданных чисел: "))
s = int(input("Введите сумму двух загаданных чисел: "))

count = []
for i in range(1, 1001):
    for j in range(1, 1001):
        if i + j == s and i * j == p:
            print(f'Вы загадали числа {i} и {j}')
            break
    else: 
            continue
    break