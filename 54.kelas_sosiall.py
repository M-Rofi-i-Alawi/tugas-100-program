# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal : 10-1-2025

print("program termasuk orang miskin/menengah/orang kaya")
print("="*20)

penghasilan = int(input('Masukkan penghasilan Anda: '))

if penghasilan >= 6000000:
    print("Anda kelas atas")
elif 1000000 <= penghasilan <= 5999999:
    print("Anda kelas menengah")
else:
    print("Kelas miskin")
