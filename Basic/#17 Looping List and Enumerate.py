a = list(range(1,11))
print('a =', a)

a_sqr = [i**2 for i in a]
print('a squared =', a_sqr)

a_qub = [i**3 for i in a]
print('a cubed =', a_qub)

# While Loop
print('\nWhile Loop')
panjang = len(a)
b = 0
while b < panjang:
    print(f'Data = {a[b]}')
    b += 1

# List Comprehension
print('\nList Comprehension')
[print(f'Kubik = {n}') for n in a_sqr]

# Enumerate
print('\nEnumerate')
for index, angka in enumerate(a_qub):
    print(f"Index : {index}, Data : {angka}")