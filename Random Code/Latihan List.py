listBuku = []

print('=== Start of Program ===')

while True:
    print('=== Register Buku Baru ===')
    judul = input('Judul Buku\t: ')
    penulis = input('Nama Penulis\t: ')

    buku_baru = [judul,penulis]
    listBuku.append(buku_baru)
    print(listBuku)
    
    print(f"| Id | {'Judul Buku':^15} | {'Penulis':^15} |")
    for index, buku in enumerate(listBuku): 
        print(f"|  {index+1} | {buku[0]:^15} | {buku[1]:^15} |")

    n = input('Continue? (y/n) ')
    if n == 'y':
        continue
    else:
        break

print(listBuku)

print('=== End of Program ===')