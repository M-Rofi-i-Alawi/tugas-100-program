# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal : 6-1-2025

nama_akun = input("Masukkan nama akun anda : ")
sandi = input("Masukkan kata sandi akun anda : ")

if nama_akun != 'rofikun@gmail.com':
    print(f"Nama akun yang anda masukkan salah {nama_akun:}")
elif sandi != 'rofkuy':
    print(f"sandi yang anda masukkan salah {sandi}")
else:
    print("Selamat datang")