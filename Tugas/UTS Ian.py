# No 1
print('===== No 1 =====\n')
population = 9870
countYear = 0
while population < 30000:
    population += population/10
    countYear += 1
print(countYear,'Tahun')

# No 2
print('\n===== No 2 =====\n')
a = 5
num = 0

for i in range(0, a):
    num = 0
    for j in range(0, i+1):
        print(num, end=" ")
        num += 1
    print()

for i in range(a, -1, -1):
    num = 0
    for j in range(0, i+1):
        print(j, end=" ")
        num -= 1
    print("\r")

# No 3
print('\n===== No 3 =====\n')
listData = []
for i in range(3):
    b = int(input())
    listData.append(b)
listData.sort()
print(listData)

# No 4
print('\n===== No 4 =====\n')
c = 9
for i in range(4):
    print(c, c-1, c-2)
    c -= 1