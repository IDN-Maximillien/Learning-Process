print(10*'=','Simple Calculator',10*'=')

def masuk():
    
    angka1 = float(input('Masukkan Angka\t\t:'))
    operator = input('Operator (*,/,+,-)\t:')
    angka2 = float(input('Masukkan Angka\t\t:'))
    
    if operator == '*':
        hasil = f'{(angka1*angka2):,.2f}'
    elif operator == '/':
        hasil = f'{(angka1/angka2):,.2f}'
    elif operator == '+':
        hasil = f'{(angka1+angka2):,.2f}'
    elif operator == '-':
        hasil = f'{(angka1-angka2):,.2f}'
    else:
        print('====== Invalid Request ======')
        return masuk()
    
    print(10*'=','\nHasil =', hasil)

    ulang = input('''Mau menggunakan Kalkulator lagi ? (y/n)
    >>>''')
    if ulang == 'y':
        masuk()

masuk()
   
print(10*'=','End of program', 10*'=')