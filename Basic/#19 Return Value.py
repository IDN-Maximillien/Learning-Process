def kubik(self):
    n = self ** 3
    print(f'Hasil {self} ^ 3 adalah {n}')
    return n

inputUser = int(input('Masukkan angka : '))
hasil = kubik(inputUser)
print('inputUser : ', inputUser, 'Nilai : ',hasil)