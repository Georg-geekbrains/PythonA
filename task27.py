# Семинар 4. Словари, множества и профилирование
# Задача N°27. Решение задачи
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. 
# So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Skillbox proxies
# Output: 13

stroka = input().split()
set1 = set()
for i in stroka:
    set1.add(i.lower())
print(len(set1))