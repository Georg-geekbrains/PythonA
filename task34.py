# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”,
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

def vowels_sound():
    vowels = {'а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы','А', 'Я', 'У', 'Ю', 'О', 'Е', 'Ё', 'Э', 'И', 'Ы'}
    return vowels   

def count_syllables(string_song):
    word_string = string_song.split()
    slog = []
    
    for word in word_string:
        count = 0
        for ch in word:
            if ch in vowels_sound():
                count += 1
        slog.append(count)
    return slog
     

def main():
   
    vini_string = input('Начинаем напевать: ')
    
    if len(set(count_syllables(vini_string)))<=1:             
                print('Парам пам-пам')
    else:
        print('Пам парам')
    
main()