# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal: 12-1-2025

print("Program Cek kehadiran")
print("=" * 30)

nama = input("nama: ")
kelas = input("kelas: ")
kehadiran = input("kehadiran: ")

if kehadiran == "hadir":
  print(nama)
  print(kelas)
  print("mengikuti pembelajaran dikelas")

elif kehadiran == "izin":
  print(nama)
  print(kelas)
  print("tidak mengikuti pembelajaran dikelas dikarenakan sedang izin")
elif kehadiran == "sakit":
  print(nama)
  print(kelas)
  print("tidak mengikuti pembelajaran dikelas dikarenakan sedang sakit")
elif kehadiran == "alpha":
  print(nama)
  print(kelas)
  print("tidak mengikuti pembelajaran dikelas dikarenakan bolos sekolah")
else:
  print(nama)
  print(kelas)
  print("status kehadiran tidak valid")
