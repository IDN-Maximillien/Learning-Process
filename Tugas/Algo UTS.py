# i = 0
# j = 5

# while True:
#     i += j
#     print(j)
#     done = input('Selesai? (y/n)')
#     if done == 'y':
#         print('Jumlah =', i)
#         break
#     else:
#         j += 2
#         continue

# batas = int(input('Masukkan batas : '))
# i = 1
# j = 1
# k = 0
# n = 0
# while n < batas:
#     k = i + j
#     i = j
#     j = k
#     n += 1
#     print(k)

n = int(input('Seberapa panjang? '))
p = 2*(n-1)
for i in range(0, n):
    for j in range(p):
        print(end=" ")
    p = p - 2
    for k in range(i+1):
        print("# ", end="")
    print("")