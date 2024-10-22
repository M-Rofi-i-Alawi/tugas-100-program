# Dibuat oleh M.Rofi'i Alawi
# Tanggal pengerjaan: 9-10-2024

print('='*40)
print('Program bola')
print('='*40)

def bola():
    r = float(input("Masukkan jari-jari : "))
    phi = 3.14
    V = lambda phi,r: 4/3*phi*r**3
    Lp = lambda phi,r: 4*phi*r**2
    print("Volume = ",V(phi,r),"cm3")
    print("Luas Permukaan = ",Lp(phi,r),"cm2")

bola()