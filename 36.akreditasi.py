# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal : 6-1-2025

Nama = input("Masukkan nama: ")
kelas = input("Masukkan kelas: ")

indonesia = int(input("Masukkan nilai B. Indonesia: "))
ipas = int(input("Masukkan nilai IPA: "))
sunda = int(input("Masukkan nilai B. sunda: "))
mtk = int(input("Masukkan nilai matematika: "))
daspro = int(input("Masukkan nilai kejuruan: "))
informatika = int(input("Masukkan nilai informatika: "))
inggris = int(input("Masukkan nilai B. Inggris: "))

# Menghitung total nilai dan rata-rata
jumlah = indonesia + ipas + sunda + mtk + daspro + informatika + inggris
rata2 = jumlah / 7

# Menentukan akreditasi berdasarkan rata-rata nilai
if 90 <= rata2 <= 100:
    akreditasi = "A"
elif 85 <= rata2 <= 89:
    akreditasi = "B"
elif 80 <= rata2 <= 84:
    akreditasi = "C"
elif 75 <= rata2 <= 79:
    akreditasi = "D"
else:
    akreditasi = "Tidak masuk salah satu akreditasi"

# Menampilkan hasil
print("Total nilai = ", jumlah)
print("Rata-rata nilai = ", rata2)
print("Akreditasi = ", akreditasi)




