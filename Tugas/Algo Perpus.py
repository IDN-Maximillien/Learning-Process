import os

# tipe data list & nested list
dataBuku = [['Blink', 'Gladwell, M.'], ["Pareto's 80/20 Principle", 'Koch, R.'], ['Subtle art of not giving a f*ck', 'Manson, M.']]

# tipe data tuple
dataPeminjam = ('Marc Spector','Steven Grant','Jake Lockey')

# tipe data dictionary
dataPengembang = {
    'nama' : 'Laurent, G.',
    'kampus' : 'UNS',
    'fakultas' : 'MIPA',
    'prodi' : 'Matematika',
    'nim' : 'M0121036'
}

def daftarPeminjam(): # menampilkan data anggota
    # os.system('cls')
    print(f'''=========================================================
| Id | {'Nama Peminjam':^48} |
=========================================================''')
    for i in range(len(dataPeminjam)): 
        print(f"|  {i+1} | {dataPeminjam[i]:^48} |")
    # print('=========================================================')
    mainMenu()

def daftarBuku(): # menampilkan data buku
    # os.system('cls')
    print(f'''=========================================================
| Id | {'Judul Buku':^31} | {'Penulis':^14} |
=========================================================''')
    for index, buku in enumerate(dataBuku): 
            print(f"|  {index+1} | {buku[0]:^31} | {buku[1]:^14} |")
    # print('=========================================================')
    mainMenu()

def inputBuku(): # menambahkan buku baru pada data buku
    # os.system('cls')
    while True:
        print('='*21, 'Register Buku', '='*21)
        judul = input('Judul Buku\t: ')
        penulis = input('Nama Penulis\t: ')
        print()
        buku_baru = [judul,penulis]
        dataBuku.append(buku_baru)
       
        print(f'''=========================================================
| Id | {'Judul Buku':^31} | {'Penulis':^14} |
=========================================================''')
        for index, buku in enumerate(dataBuku): 
            print(f"|  {index+1} | {buku[0]:^31} | {buku[1]:^14} |")
        print('=========================================================')
        n = input('Continue? (y/n) ')
        if n == 'y':
            continue
        else:
            mainMenu()

def infoPengembang(): # menampilkan data pengembang pemrogram
    print(f'''=========================================================
|   Nama            : {dataPengembang['nama']}
|   Kampus          : {dataPengembang['kampus']}
|   Fakultas        : {dataPengembang['fakultas']}
|   Program Studi   : {dataPengembang['prodi']}
|   NIM             : {dataPengembang['nim']}''')
    mainMenu()

def mainMenu(): # menampilkan menu utama
    print(f'''=========================================================
|   Selamat Datang di Program Perpustakaan Sederhana!   |
|                                                       |
|   1. Data Peminjam                                    |
|   2. Tampilkan Data Buku                              |
|   3. Masukkan Buku Baru                               |
|                                                       |
|   9. Informasi Pengembang                             |
|   0. Keluar Program                                   |
=========================================================
''')
    inputUser = input('>>> ')
    if inputUser == '1':
        os.system('cls')
        daftarPeminjam()
    elif inputUser == '2':
        os.system('cls')
        daftarBuku()
    elif inputUser == '3':
        os.system('cls')
        inputBuku()
    elif inputUser == '9':
        os.system('cls')
        infoPengembang()
    elif inputUser == '0':
        print('==================== End of Program =====================')
        exit()
    else:
        os.system('cls')
        print('Invalid Option!')
        mainMenu()

print(f"""=================== Start of Program ====================
|              ,..........   ..........,                |
|          ,..,'          '.'          ',..,            |
|         ,' ,'            :            ', ',           |
|        ,' ,'             :             ', ',          |
|       ,' ,'              :              ', ',         |
|      ,' ,'............., : ,.............', ',        |
|     ,'  '............   '.'   ............'  ',       |
|      '''''''''''''''''';''';''''''''''''''''''        |
|                         '''                           |""")

mainMenu()