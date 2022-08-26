menu = [["BU", "Bakso Urat", 15000],
        ["MA", "Mie Ayam", 12000],
        ["NG", "Nasi Goreng", 12000],
        ["ET", "Es Teh", 4000],
        ["AG", "Ayam Goreng", 10000],
        ["AGK", "Ayam Geprek", 15000]]
pesanan = []
border = '='*40
nomorList = 0
posisiList = 0
total = 0

def pesananMasuk():
    global nomorList, posisiList, total
    x = input('Silahkan Pilih Menu : ')
    for m in range(len(menu)):
        posisiList = m-1
        try:
            nomorList = menu[posisiList].index(x)
            break
        except:
            pass
    y = int(input("Berapa banyak? "))
    tempTotal = y * menu[posisiList][2]
    total += tempTotal
    z = [x, y, tempTotal]
    pesanan.append(z)
    mainMenu()

def cetakPesanan():
    print(f"{'Menu' : ^6}{'Jumlah' : ^6}{'Total' : ^10}")
    for i in range(0, len(pesanan)):
    	print(f"{pesanan[i][0] : ^6}{pesanan[i][1] : ^6}{pesanan[i][2] : >10}")
    mainMenu()

def mainMenu():
    print(f"""{border}
Selamat Datang di Los Pollos Hermanos!
{border}""")
    print(f"{'Kode' : ^5}{'Menu' : ^25}{'Harga' : ^10}")
    for i in range(0, len(menu)):
    	print(f"{menu[i][0] : ^5}{menu[i][1] : ^25}{menu[i][2] : >10}")
    print(f"""
I : Memasukan Pesanan
L : Laporan Pesanan
X : Selesai
    """)
    try:
        user = input('>>> ')
        if user == 'I':
            pesananMasuk()
        elif user == 'L':
            cetakPesanan()
        elif user == 'X':
            pass
    except:
        pass
    
    exit()

mainMenu()