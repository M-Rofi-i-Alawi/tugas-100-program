# Dibuat oleh M.Rofi'i Alawi
# Tanggal pengerjaan: 8-10-2024

print('='*40)
print('Rumus Kerucut')
print('='*40)

def kerucut():
    r = int(input("Masukkan jari-jari : "))
    t = int(input("Maasukkan tinggi : "))
    phi = 3.14
    s = int(input("sisi miring : "))
    V = lambda phi,r,t: 1/3*phi*r**2*t
    Lp = lambda phi,r,s: (phi*r**2)+(phi*r*s)
    print("Volume = ",V(phi,r,t),"cm3")
    print("Luas Permukaan = ",Lp(phi,r,s),"cm2")

kerucut()