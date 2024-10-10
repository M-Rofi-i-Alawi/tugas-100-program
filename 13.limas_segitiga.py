# Dibuat oleh M.Rofi'i Alawi
# Tanggal pengerjaan: 10-10-2024

luas_alas = int(input("Masukkan luas alas : "))
t = int(input("Masukkan tinggi : "))
luas_sisi_tegak = int(input("Masukkan luas sisi tegak : "))

V = 1/3*luas_alas*t
Lp = luas_alas+luas_sisi_tegak

print("Volume = ",V,"cm3")
print("Luas Peermukaan = ",Lp,"cm2")