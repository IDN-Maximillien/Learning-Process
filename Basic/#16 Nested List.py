a = [1,2]
b = [3,4]
c = a + b
d = a, b
e = [a, b]

print('list a (a)\t:', a)
print('list b (b)\t:', b)
print('list c (a + b)\t:', c)
print('list d (a, b)\t:', d)
print('list e [a, b]\t:', e)

peserta_0 = ['Andi', 'Laki-laki', 9]
peserta_1 = ['Budi', 'Laki-laki', 12]
peserta_2 = ['Charlie', 'Laki-laki', 5]
peserta_3 = ['Devi', 'Perempuan', 10]

list_peserta = [peserta_0, peserta_1, peserta_2, peserta_3]
print('list_peserta = ', list_peserta)

for peserta in list_peserta:
    print(f'''
    Nama \t: {peserta[0]}
    Gender \t: {peserta[1]}
    Kelas \t: {peserta[2]}''')