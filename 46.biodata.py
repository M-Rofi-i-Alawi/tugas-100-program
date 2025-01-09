# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal : 8-1-2025

print("biodataku")
print("="*20)

instruksi = input("Tekan enter dan masukkan biodata Anda: ")
nama = input("Nama: ")
umur = input("Umur: ")
pendidikan_terakhir = input("Pendidikan Terakhir: ")
pengalaman_kerja = input("Pengalaman Kerja: ")

if umur >= 20 and umur <= 35:
	if pendidikan_terakhir == "SMK" or pendidikan_terakhir == "S1"or pendidikan_terakhir == "S2" or pendidikan_terakhir == "S3":
	    if pengalaman_kerja >= 2:
	    	print("Selamat!", nama,"Anda diterima di perusahaan kami ")
else:
   print("Maaf",nama,"Anda masih belom lolos!. Silahkan coba lagi tahun depan ")