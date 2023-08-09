#Напишите программу, котороф на вход принимает два числа A и B
# и возводит число A  в целую степень B с помощью рекурсии

x = int(input('Input x: '))
y = int(input('Input y: '))

def recurs(x,y):
    if y <= 0:
        return 1
    else:
        return x * recurs(x,y-1)

print(f'{recurs(x,y)}')