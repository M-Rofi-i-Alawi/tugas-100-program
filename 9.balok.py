# Dibuat oleh M.Rofi'i Alawi
# Tanggal pengerjaan: 8-10-2024

print("="*40)
print("Rumus Balok")
print("="*40)

def balok():
    p = int(input("Masukkan panjang : "))
    l = int(input("Masukkan lebar : "))
    t = int(input("Masukkan tinggi : "))
    V = lambda p,l,t: p*l*t
    L = lambda p,l,t: 2*(p*l)+(p*t)+(l*t)
    K = lambda p,l,t: 4*(p+l+t)
    print("Volume   = ",V(p,l,t),"Cm3")
    print("Luas     = ",L(p,l,t),"Cm3")
    print("Keliling = ",K(p,l,t),"Cm3")

balok()
