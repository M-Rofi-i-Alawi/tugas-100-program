# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal : 5-1-2025

print("="*20 + " Program total rugi dalam aritmatika sosial " + "="*20)

def rugi():
    print("="*25 + " Hitung Rugi " + "="*25)
    harga_beli = int(input("Masukkan harga beli: "))
    harga_jual = int(input("Masukkan harga jual: "))
    total = lambda harga_beli, harga_jual: harga_jual - harga_beli

    selisih = total(harga_beli, harga_jual)
    
    if selisih >= 0:
        status = "tidak rugi"
    else:
        status = "rugi"

    print("Total = ", selisih)
    print("Status = ", status)

rugi()

