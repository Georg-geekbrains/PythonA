#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?


birds = int(input("Введите число журавлей: "))
members = 3

if birds % 6 == 0 and birds >= members*2:
        i = 0
        sum = 0
        while sum < birds:
            p = i
            s = i
            k = 4 * i
            sum = 6 * i 
            i+=1
        print(f"{sum} -> {p} {s} {k}")   
else:
        print('Продолжаем делать птиц')    