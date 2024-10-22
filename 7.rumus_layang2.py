# Dibuat oleh M.Rofi'i Alawi
# Tanggal pengerjaan: 8-10-2024

print("="*40)
print('Rumus Layang-Layang')
print("="*40)

def layang2():
    d1 = int(input("masukkan diagonal 1 : "))
    d2 = int(input("masukkan diagonal 2 : "))
    s = int(input("masukkan sisi panjang : "))
    L = lambda d1,d2: 2/d1+d2
    K = lambda s: 4*s
    print("Luas = ",L(d1,d2),"cm2")
    print('Keliling = ',K(s),"cm")

layang2()