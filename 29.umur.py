# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal : 29-12-2024

import datetime as waktu

print("=" *10 + " Program Data Lahir "+" ="*10)

# Menginput
Nama = str(input("Masukkan nama anda   \t\t: "))
Tanggal = int(input("Masukkan tanggal  \t\t: "))
Bulan = int(input("Masukkan angka bulan\t\t: "))
Tahun = int(input("Masukkan tahun      \t\t: "))

# Membuat tanggal lahir
tanggal_lahir = waktu.date(Tahun,Bulan,Tanggal)
print(f"Tanggal lahir anda adalah = {tanggal_lahir}")

# Membuat ummur dalam hari, bulan dan tahun
hari_ini = waktu.date.today()
print(f"Harinya adalah hari : {tanggal_lahir:%A}")
umur_dalam_hari = hari_ini-tanggal_lahir
print(f"Umur anda dalam hari : {umur_dalam_hari}")
umur_dalam_bulan = (hari_ini.year-tanggal_lahir.year) * 12 + (hari_ini.month-tanggal_lahir.month)
print(f"Bulannya adalah bulan : {tanggal_lahir:%B}")
print(f"Umur anda dalam bulan : {umur_dalam_bulan} bulan")
umur_dalam_tahun = umur_dalam_hari.days // 365
print(f"Umur anda saat ini adalah : {umur_dalam_tahun} tahun")
umur_bulan_sisa = (umur_dalam_hari.days % 365) // 30
print(f"Umur anda adalah = {umur_dalam_tahun} tahun, {umur_bulan_sisa} bulan") # umur bulan sisa untuk menunjukkan berapa bulan lagi untuk nambah umur