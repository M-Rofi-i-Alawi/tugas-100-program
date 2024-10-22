# Dibuat oleh M.Rofi'i Alawi
# Tanggal pengerjaan: 8-10-2024

print('='*40)
print("Rumus Kubus")
print('='*40)

def kubus():
    s = int(input("Masukkan sisi : "))
    v = lambda s: s*3
    lp = lambda s: 6*(s*s)
    k = lambda s: 12*s
    l = lambda s: s*s
    print("Volume = ",v(s),"cm3")
    print("Luas Permukaan = ",lp(s),"cm2")
    print("Keliling = ",k(s),"cm")
    print("Luas = ",l(s),"cm2")

kubus()