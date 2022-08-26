# import os
# print(os.getcwd())

#     print(f)

# f = open('test.txt', 'r')
with open('test.txt', 'r') as f:
    f_isi = f.read(10)
    while len(f_isi) > 0:
        print(f_isi, end='')
        f_isi = f.read(10)

