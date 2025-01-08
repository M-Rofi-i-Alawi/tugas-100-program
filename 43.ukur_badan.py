# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal : 7-1-2025

print('='*40)
print('program ukur badan usia 20 tahun')
print('='*40)

tinggi = int(input("Masukkan tinggi badan (cm): "))
berat = int(input("Masukkan berat badan (kg): "))

if tinggi <120:
    print("Tinggi badan =",tinggi,"cm pendek")
elif 121 <= tinggi <180:
    print("Tinggi badan =",tinggi,"cm ideal")
else: # tinggi lebih dari 181
    print("Tinggi badan = ",tinggi,"cm Setinggi tiang")

if berat <30:
    print("Berat badan =",berat,"kg kurus")
elif 31<= berat <65:
    print("Berat badan =",berat,"kg ideal")
else: # Berat lebih dari 65
    print("Berat badan = ",berat,"kg Setinggi gemuk")
