# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal : 8-1-2025

print('='*40)
print('program kualitas laptop')
print('='*40)

harga = int(input("Masukkan harganya: "))
kualitas = str(input("Masukkan kualitasnya (Oke/bagus/lumayan): ")).lower()

if kualitas == "oke" and harga > 1000000:
    print("Harga segitu bagus untuk dipakai.")
elif kualitas == "bagus" and harga > 1000000:
    print("Harga segitu masih bisa dipakai, tapi harga perlu dipertimbangkan kembali")
elif kualitas == "lumayan" and harga > 1000000:
    print("Harga segitu masih layak untuk bisa dipakai.")
elif harga > 2000000 and kualitas == "oke":  # Harga mahal tapi spesifikasi bagus
    print("Harganya kemahalan, tapi spesifikasinya bagus, perlu dipertimbangkan.")
elif harga > 2000000 and kualitas in ["lumayan", "bagus"]:  # Harga mahal dan kualitas biasa
    print("Harganya terlalu mahal, jadi tidak layak dipakai, jika dilihat kualitasnya.")
elif harga < 1000000 and kualitas in ["bagus", "lumayan"]:
    print("Harga murah, kualitasnya masih layak untuk dipakai.")
elif harga < 1000000 and kualitas not in ["oke", "bagus", "lumayan"]:
    print("Harga murah, tapi kualitasnya tidak layak.")
else:
    print("Gak layak dipakai.")
