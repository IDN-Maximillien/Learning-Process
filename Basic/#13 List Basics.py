print(40*'=')

print(10*'-', 'List Angka Genap', 10*'-')
list_a = [i for i in range(1,51) if i%2 == 0]
print(list_a)

print(10*'-', 'List Angka Ganjil', 10*'-')
list_b = [i for i in range(1,51) if i%2 != 0]
print(list_b)

print(40*'=')

data = ['Andre', 'Budi', 'Caca', 'Dita']
print(data, '\n- Data Original')

data.append('Erwin')
print(data, '\n- "Erwin" ditambahkan')

data[2] = "Charlie"
print(data, '\n- "Caca" diganti menjadi "Charlie"')

data.insert(1, 'Bani')
print(data, '\n- ditambahkan "Bani" sebelum "Budi"')

data.remove('Budi')
print(data, '\n- "Budi" dikeluarkan')

data.extend(list(range(1, 5)))
print(data, '\n- ditambahkan kumpulan angka di belakang')

n = data.pop()
print('\nData yang berada di ujung belakang adalah', n)

print('\nData ke 5 pada list adalah', data[4])
print(f'\nData {data[5]} ada pada urutan ke 6')
print('\nString "Andre" ada pada urutan ke', (data.index('Andre') + 1) )