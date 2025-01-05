# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal : 5-1-2025

print("="*20 + " Program rugi dalam bentuk persen dalam aritmatika sosial " + "="*20)

def rugi_persen():
    print("="*25 + " Hitung Rugi dalam bentuk persen " + "="*25)
    harga_beli = int(input("Masukkan harga yang dibeli: "))
    harga_jual = int(input("Masukkan harga yang terjual: "))
    
    # Menghitung total rugi
    total_rugi = harga_beli - harga_jual
    
    if total_rugi > 0:  # Ada kerugian
        # Menghitung rugi dalam persen
        rugi_persen = (total_rugi / harga_beli) * 100
        print(f"Total kerugian = {total_rugi}")
        print(f"Total kerugian dalam bentuk persen = {rugi_persen:.2f}%")
    else:  # Tidak ada kerugian
        print("Tidak ada kerugian.")

rugi_persen()



