# Dibuat oleh Muhammad Rofi'i Alawi
# Dibuat tanggal 17-12-2024
# Program penerimaan pengurus OSIS atau MPK SMKN 1 Cianjur periode 2025/2026

# Program Seleksi OSIS dan MPK

def seleksi_osis():
    print("Program seleksi osis")
    print("="*15)

    # input data calon peserta osis
    nama = input("Masukkan nama peserta : ")
    kelas = input("Masukkan kelas peserta : ")
    nilai = int(input("Masukkan nilai peserta : "))

    # kriteria menjadi osis 
    if nilai >=75:
        status = "Diterima di osis"
    else:
        status = "Tidak diterima"
        # Output hasil seleksi OSIS
    print("="*15)
    print("Nama peserta : ",nama)
    print("Kelas peserta : ",kelas)
    print("Status peserta : ",status)
    print("="*15)

def seleksi_mpk():
    print("Program seleksi mpk")
    print('='*15)

    # input data calon peserta osis
    nama = input("Masukkan nama peserta : ")
    kelas = input("Masukkan kelas peserta : ")
    nilai = int(input("Masukkan nilai peserta : "))

    # kriteria menjadi mpk
    if nilai >=85:
        status = "Diterima di mpk"
    else:
        status = "Tidak diterima"
        # Output hasil seleksi OSIS
    print("="*15)
    print("Nama peserta : ",nama)
    print("Kelas peserta : ",kelas)
    print("Status peserta : ",status)

# Hasil program
print("Pilih seleksi mau osis/mpk?")
menu = input("Masukkan pilihan peserta (osis/mpk): ")
if menu == "osis":
    seleksi_osis()
elif menu == "mpk":
    seleksi_mpk()