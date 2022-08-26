#a = ("""
#Ing ngarsa sung tuladha
#Ing madya mangun karsa
#Tut wuri handayani""")

#print('huruf a pada :', a , '\nada', a.count('a'))

nama_lengkap = "Emmanuel Aji Sadewa"

print(nama_lengkap)
print(len(nama_lengkap), 'karakter string')
print(nama_lengkap[0:19:2])

nama_upper = nama_lengkap.upper()
nama_lower = nama_lengkap.lower()
print(nama_upper)
print(nama_lower)

check_lower1 = nama_lower.islower()
check_lower2 = nama_lower.isupper()
print('nama_lower is lower =', str(check_lower1))
print('nama_lower is upper =', str(check_lower2))

check_upper1 = nama_upper.islower()
check_upper2 = nama_upper.isupper()
print('nama_upper is lower =', str(check_upper1))
print('nama_upper is upper =', str(check_upper2))