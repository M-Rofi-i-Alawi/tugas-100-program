# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal : 9-1-2025

print("program laku atau tidak lakunya suatu barang")
print("="*20)

def laku_atau_tidak():
  jumlah_bayar = int(input("Masukkan jumlah bayar: "))

  if jumlah_bayar>250000:
    print("Barangnya laku")
  else:
    print("Barangnya gak laku")

laku_atau_tidak()