list_a = ['a', 'b', 'c']
list_b = list_a
list_c = list_a.copy()

print(list_a, hex(id(list_a)))
print(list_b, hex(id(list_b)))
print(list_c, hex(id(list_c)))

list_b[1] = 'andra'
list_c[0] = 'Neko'

print(list_a, hex(id(list_a)))
print(list_b, hex(id(list_b)))
print(list_c, hex(id(list_c)))