# # x = int(input('x = '))
# # for i in range(1,x):
# #     print(i)

# # # i = 0
# # # while True:
# # #     i += 1
# # #     print(i)

# # # print(3**0)

# # for a in range(1,11,3):
# #     print(a)

# m = int(input())
# for i in range(0,m+1,2):
#     print(i)

# n = 0
# s = 0
# # while n < 50:
# #     n += 2
# #     s = s + n*n
# while n <=50 :
#     n += 2
#     s = s + n*n
#     # if n == 50:
#     #     print(s)
#     #     break
#     # else:
#     #     continue
# print(s)

A = [[1,2,3],[4,5,6],[7,8,9]]
print(len(A))
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=' ')
    print()