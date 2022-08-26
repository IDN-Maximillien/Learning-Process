from random import randint

a = randint(1, 100)

def tebak():
    b = int(input('>>> '))
    if b > a:
        print('Terlalu Tinggi!')
        return tebak()
    elif b < a:
        print('Terlalu Rendah!')
        return tebak()
    else:
        print('Benar!')

tebak()