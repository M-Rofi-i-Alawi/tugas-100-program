# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal : 6-1-2025

print("="*20)
print("Program harga jual")
print("="*20)

def harga_jual():
    persentase__rugi= float(input("Masukkan persentase ruginya : "))
    harga_beli = int(input("Masukkan harga belinya : "))
    harga_jual = lambda persentase_rugi,harga_beli : (100-persentase_rugi)/100*harga_beli
    print("Jadi harga yang terjualnya adalah = ",harga_jual(persentase__rugi,harga_beli))

harga_jual()
    