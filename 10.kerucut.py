# Dibuat oleh M.Rofi'i Alawi
# Tanggal pengerjaan: 8-10-2024

print('='*40)
print('Rumus Kerucut')
print('='*40)

r = int(input("Masukkan jari-jari : "))
t = int(input("Maasukkan tinggi : "))
phi = 3.14
s = int(input("sisi miring : "))

V = 1/3*phi*r**2*t
Lp = (phi*r**2)+(phi*r*s)

print("Volume = ",V,"cm3")
print("Luas Permukaan = ",Lp,"cm2")