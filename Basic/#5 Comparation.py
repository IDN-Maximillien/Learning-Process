inputUser = float(input('Masukkan angka :'))

a = inputUser < 0
b = inputUser > 5
c = inputUser < 8
d = inputUser > 11
e = a or ( b and c ) or d

print(e)