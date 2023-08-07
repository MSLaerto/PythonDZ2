a = int(input('Введите N: '))

def power(a , b):
    if b <= a :
        print(f"{b}" , end=" ")
        return power(a , b*2)
    else : 
        return 0 
    
power (a , 1 )
    