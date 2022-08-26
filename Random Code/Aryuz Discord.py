# # Solusi 1
# def perhitungan1():
#     a = list(range(1, 101))
#     print(60*'=', "\nList:", a)
#     for b in a :
#         if b % 2 == 0 :
#             continue
#         elif b > 15 :
#             break
#         result = b * ( b + 10 )
#         print(result)
#     perhitungan1()

# Solusi 2 
def perhitungan2():
    m = [i for i in range(1, 101) if i%2 != 0]
    print(60*'=', '\nList:', m)
    for n in m :
        result = n * ( n + 10 )
        if n > 16 : break
        print(result)
perhitungan2()

def perhitungan3():
    m = [i for i in range(1, 101) if i%2]
    print(60*'=', '\nList:', m)
    for n in m :
        result = n * ( n + 10 )
        if n > 16 : break
        print(result)
perhitungan3()