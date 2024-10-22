# Dibuat oleh M.Rofi'i Alawi
# Tanggal pengerjaan: 6-10-2024

print("rumus persegi panjang")

def persegi_panjang ():
    p = int(input("Masukkan panjang: "))
    l = int(input("Masukkan lebar: "))
    Luas = lambda p,l: p*l 
    Keliling = lambda p,l: 2*(p+l)

    print(f"Luas Persegi Panjang\t\t : ",Luas(p,l),"cm2")
    print(f"Keliling Persegi Panjang\t :",Keliling(p,l),"cm")

persegi_panjang()
