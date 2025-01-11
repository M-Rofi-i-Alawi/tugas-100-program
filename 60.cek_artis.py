# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal: 11-1-2025

print("Program Cek Artis atau Tidak")
print("=" * 30)

nama = input("Masukkan nama: ")
kamu = input("Apakah kamu terkenal? (ya/yes/tidak/no): ").lower()

if kamu == "ya" or kamu == "yes":
    print(f"{nama}, kamu adalah seorang artis: {True}")
else:
    print(f"{nama}, kamu bukan seorang artis: {True}")
