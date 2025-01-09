# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal : 9-1-2025

print("program pajak")
print("="*20)

gaji = int(input("masukkan gaji anda: "))
pajak = 15

if gaji >=500000:
  print(f"anda mendapatkan pajak sebesar {pajak}%")
  uang_pajak = (pajak/100)*gaji
  print(f"yang perlu anda bayar pajak sebesar: Rp {uang_pajak}")
  print("sisa uang anda dipakai bayar pajak: ",(gaji-uang_pajak))

elif gaji <=500000:
  print(f"anda mendapatkan pajak sebesar 5%")
  uang_pajak = (5/100)*gaji
  print(f"yang perlu anda bayar pajak sebesar: Rp {uang_pajak}")
  print("sisa uang anda dipakai bayar pajak: ",(gaji-uang_pajak))