# Dibuat oleh Muhammad Rofi'i Alawi
# Dibuat tanggal 9-12-2024

def panjang_gelombang():
    c = float(input("Masukkan kecepatan suara : "))
    f = float(input("Masukkan frekuensi gelombang : "))
    λ = lambda c,f: c/f
    print("gelombang elektronya = ",λ(c,f),"λ")

panjang_gelombang()