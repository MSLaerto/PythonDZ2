s = int(input('Введите S: '))
p = int(input('Введите P: '))

def guess(s , p ):
    for x in range (0 , s) :
        if x * (s-x) == p and x <= s-x: 
            print (f"X = {x} , Y = {s-x}")
guess(s,p)