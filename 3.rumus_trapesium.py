# Dibuat oleh M.Rofi'i Alawi
# Tanggal pengerjaan: 6-10-2024

print("Rumus Trapesium")

def trapesium():
    a = int(input("Masukkan sisi a : "))
    b = int(input("Masukkan sisi b : "))
    c = int(input("Masukkan sisi c : "))
    d = int(input("Masukkan sisi d : "))
    t = int(input("Masukkan tinggi : "))
    L = lambda a,b,t: 1/2*(a+b)*t
    K = lambda a,b,c,d: (a+b+c+d)

    print(f"Luas =",L(a,b,t),"cm2")
    print(f"Keliling =",K(a,b,c,d),"cm")

trapesium()