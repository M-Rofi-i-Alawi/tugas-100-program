# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal: 11-1-2025

print("Program Cek kehadiran")
print("=" * 30)

nama = input("nama: ")
kelas = input("kelas: ")
kehadiran = input("kehadiran: ")

if kehadiran == "hadir" and "Hadir":
  print(nama)
  print(kelas)
  print("mengikuti pembelajaran dikelas")

elif kehadiran == "izin" and "Izin":
  print(nama)
  print(kelas)
  print("tidak mengikuti pembelajaran dikelas dikarenakan sedang izin")
elif kehadiran == "sakit" and "sakit":
  print(nama)
  print(kelas)
  print("tidak mengikuti pembelajaran dikelas dikarenakan sedang sakit")
elif kehadiran == "alpha" and "Alpha":
  print(nama)
  print(kelas)
  print("tidak mengikuti pembelajaran dikelas dikarenakan bolos sekolah")
