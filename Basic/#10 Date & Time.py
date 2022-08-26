import datetime
from re import A

today = datetime.date.today() 
hari = datetime.datetime.now()
print(today.strftime('%A'))
print(hari.strftime('%A'))

if (today)=="Saturday":
    print("Sabtu")
    
print(f"Hari ini adalah hari {today:%A}")

print('\n', 20*'=','\n')


tanggal = int(input('Tanggal lahir anda? '))
bulan = int(input('Bulan lahir anda? '))
tahun = int(input('Tahun lahir anda? '))

tanggal_lahir = datetime.date(tahun,bulan,tanggal)

u_hari = today - tanggal_lahir
u_tahun = u_hari.days // 365
u_bulan = (u_hari.days % 365) // 30
u_sisa = (u_hari.days % 365) % 30

print(f'Hari saat anda lahir adalah {tanggal_lahir:%A}')
print(f'Umur anda adalah {u_tahun} tahun, {u_bulan} bulan, {u_sisa} hari.')