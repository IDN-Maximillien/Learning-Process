from random import randint

print(25*"=")

harga = 10000.1
jumlah = 20.1
f_string = f"Harga total = Rp {(harga*jumlah):,.2f}"
print(f_string)

print(25*"=")

plus = 25
minus = -90
f_plus = f'{plus:.2f}'
f_minus = f'{minus:+.2f}'
print(f_plus)
print(f_minus)

print(25*"=")

a = randint(0, 200)
print('a = ', a)

f_binary = f"Binary = {bin(a)}"
f_octal = f"Octal = {oct(a)}"
f_hex = f"Hexa = {hex(a)}"

print(f_binary)
print(f_octal)
print(f_hex)

print(25*"=")