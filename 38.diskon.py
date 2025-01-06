# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal : 6-1-2025

# Input harga barang
barang_1 = int(input("Masukkan harga barang 1: "))
barang_2 = int(input("Masukkan harga barang 2: "))
barang_3 = int(input("Masukkan harga barang 3: "))
barang_4 = int(input("Masukkan harga barang 4: "))
barang_5 = int(input("Masukkan harga barang 5: "))

jumlah = barang_1 + barang_2 + barang_3 + barang_4 + barang_5
diskon = float(input("Diskonnya: "))
jumlah_diskon = (diskon / 100) * jumlah
total_bayar = jumlah - jumlah_diskon

if jumlah > 500000:
    print(f"Anda mendapatkan diskon sebesar {diskon}%")
    print(f"Harga awal: Rp{jumlah:,.2f}")
    print(f"Potongan harga: Rp{jumlah_diskon:,.2f}")
    print(f"Total yang harus Anda bayar: Rp{total_bayar:,.2f}")
else:
    print(f"Anda tidak mendapatkan diskon sebesar {diskon:.2f}%")
    print(f"Total yang harus Anda bayar: Rp{jumlah:,.2f}")
