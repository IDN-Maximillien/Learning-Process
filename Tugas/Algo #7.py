# for i in range(4):
#     for j in range(4):
#         print(f'{i,j}', end=(' '))
#     print()

# A = [[3,5],[4,6]]
# s = 0
# for i in range(len(A)):
#     for j in range(len(A[0])):
#         s += A[i][j]
#         print(A[i][j], end=' ')
#     print()
# print(s)

Angka = int(input('Berapa? '))
for i in range(Angka):
    k = 1 
    for j in range(Angka+1):
        print(Angka, end=(' '))
        Angka += 1
    print()