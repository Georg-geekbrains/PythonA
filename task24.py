# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – 
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста
# и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.


import random

bluebarryBush = int(input('Number of bushes: '))
harvest = []
for i in range(0,bluebarryBush):
    harvest.append(random.randint(1,10))
print(harvest)
harvest += [harvest[0],harvest[1]]

sumHarvest = 0
for i in range(bluebarryBush):
    s = harvest[i]+harvest[i+1]+harvest[i+2]
    
    if s > sumHarvest:
        sumHarvest = s
        
print(f'Max number of bluebarry is: {sumHarvest}')