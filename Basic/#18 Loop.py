# a = list(range(0,20))
# print(a)
# for i in a:
#     while i < 15:
#         i += 1
#         print(i)
#     # for z in a:
#     #     print(f"{a[z] : ^10}")

# for i in range(1,36,2):
#     print(f"{i*'*':^35}")
#     i += 1

# num = 11
# if num > 1:
# 	for i in range(2, int(num/2)+1):
# 		if (num % i) == 0:
# 			print(num, "is not a prime number")
# 			break
# 	else:
# 		print(num, "is a prime number")
# else:
# 	print(num, "is not a prime number")

num = 407
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)
            break
    else:
        print(num,"is a prime number")
else:
   print(num,"is not a prime number")