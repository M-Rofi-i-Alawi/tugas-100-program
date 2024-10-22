# Dibuat oleh M.Rofi'i Alawi
# Tanggal pengerjaan: 6-10-2024
print('Linngkaran')

def lingkaran():
    r=float(input("Masukkan jari-jari : "))
    phi=3.14
    L=lambda phi,r: phi*r*r
    K=lambda phi,r: 2*phi*r
    print("Luas = ",L(phi,r),"cm2")
    print("Luas = ",K(phi,r),"cm")

lingkaran()