# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal : 10-1-2025

print("program termasuk orang miskin/menengah/orang kaya")
print("="*20)

penghasilan = int(input('masukkan penghasilan anda: '))

if penghasilan >=6000000:
  print("anda orang kaya")
elif 1000000 <=penghasilan>5000000:
  print('anda kelas menengah')
else:
  print("kelas miskin")