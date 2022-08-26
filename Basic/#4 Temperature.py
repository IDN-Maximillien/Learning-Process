print('====Temperature Conversion - Celcius====')

celcius = float(input('Input suhu : '))
print('Suhu dalam Celcius adalah ', celcius, ' Celcius')
reamur = (4/5) * celcius
print('Suhu dalam Reamur adalah ', reamur, ' Reamur')
fahrenheit = ((9/5) * celcius) + 32
print('Suhu dalam Fahrenhreit adalah ', fahrenheit, ' Fahrenhreit')
kelvin = celcius + 273
print('Suhu dalam Celcius adalah ', kelvin, ' Kelvin')

print('====Temperature Conversion - Kelvin====')

kelvin = float(input('Input suhu : '))
print('Suhu dalam Kelvin adalah ', kelvin, ' Kelvin')
celcius = kelvin - 273
print('Suhu dalam Celcius adalah ', celcius, ' Celcius')
reamur = celcius * (4/5)
print('Suhu dalam Reamur adalah ', reamur, ' Reamur')
fahrenheit = (celcius * (9/5)) + 32
print('Suhu dalam Fahrenheit adalah ', fahrenheit, ' Fahrenheit')

print('====Temperature Conversion - Fahrenhreit====')

fahrenheit = float(input('Input suhu : '))
print('Suhu dalam Fahrenheit adalah ', fahrenheit, ' Fahrenheit')
celcius = (fahrenheit - 32) * (5/9)
print('Suhu dalam Celcius adalah ', celcius, ' Celcius')
reamur = (fahrenheit - 32) * (4/9)
print('Suhu dalam Reamur adalah ', reamur, ' Reamur')
kelvin = celcius + 273
print('Suhu dalam Kelvin adalah ', kelvin, ' Kelvin')