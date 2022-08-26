from calendar import c


a = 'Kamu ganteng banget'
b = 'Masak sich'
c = 'Hari ini ujian python'

def rvsd_print(x):
    print('Kalimat :', x)
    x = x.split()
    y = len(x)
    print('Ditulis terbalik menjadi :')
    for i in range(y, 0, -1):
        print(x[i-1], end=' ')
    print()

rvsd_print(a)
rvsd_print(b)
rvsd_print(c)