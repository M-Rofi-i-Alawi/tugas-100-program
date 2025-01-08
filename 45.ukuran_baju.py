# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal : 8-1-2025

print("ukur baju")
print("="*20)

lebar = int(input("lebar = "))
panjang = int(input("panjang = "))

if lebar >=26:
  print(f"kebesaran",{lebar})
elif panjang >=38:
  print(f"kepanjangan",{panjang})
else:
  print(f"lebarnya",{lebar} ,"tidak kebesaran")
  print(f"panjangnya", {panjang},"tidak kepanjangan")
