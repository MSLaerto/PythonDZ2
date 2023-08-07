import random as rnd

a = int(input('Введите количество монеток: '))
def flip(a):
    b = rnd.randint(0 , a)
    print(f"На столе лежит {b} орлов и {a-b} решек")
    print(f"Нужно перевернуть {min(b , a-b)} монет")       

flip(a)
