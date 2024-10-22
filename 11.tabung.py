# Dibuat oleh M.Rofi'i Alawi
# Tanggal pengerjaan: 9-10-2024

print('='*40)
print('Program tabung')
print('='*40)

def tabung():
    phi = 3.14
    t = int(input("Masukkan tinggi : "))
    r = int(input("Masukkan jari- jari : "))
    v = lambda phi,r,t: phi*r**2*t
    lp = lambda phi,r,t: 2*phi*r*(r+t)
    print("Volume = ",v(phi,r,t),"cm3")
    print("Luas Permukaan = ",lp(phi,r,t),"cm2")

tabung()