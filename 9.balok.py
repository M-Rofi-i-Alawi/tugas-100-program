# Dibuat oleh M.Rofi'i Alawi
# Tanggal pengerjaan: 8-10-2024

print("="*40)
print("Rumus Balok")
print("="*40)

p = int(input("Masukkan panjang : "))
l = int(input("Masukkan lebar : "))
t = int(input("Masukkan tinggi : "))

V = p*l*t
L = 2*(p*l)+(p*t)+(l*t)
K = 4*(p+l+t)

print("Volume   = ",V,"Cm3")
print("Luas     = ",L,"Cm3")
print("Keliling = ",K,"Cm3")
