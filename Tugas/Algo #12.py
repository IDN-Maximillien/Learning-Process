sebuah_angka = 29

try:
    print(sebuah_angka / 0)
except:
    print("proses perhitungan gagal ")

print("proses cetak ini masih dapat dijalankan ")

try:
    print(sebuah_angka / 0)
except (ZeroDivisionError):
    print("proses perhitungan gagal")

print("proses cetak ini masih dapat dijalankan ")

print(sebuah_angka / 0)