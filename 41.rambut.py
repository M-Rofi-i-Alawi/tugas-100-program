# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal : 7-1-2025

print('='*40)
print('Program menentukan rambutnya panjang atau tidak')
print('='*40)

nama = input("Masukkan nama: ")
kelas = input("Masukkan kelas: ")
kelamin = str(input("Masukkan jenis kelaminnya: "))
ukuran = int(input("Masukkan ukuran rambutnya: "))

if kelamin == "Perempuan" and ukuran >10:
    print("Rambutnya panjang")
    
elif kelamin == "Laki-laki" and ukuran >=5:
    print("Rambutnya panjang")
else:
    print("Rambut",nama, "tidak panjang, tapi pendek")