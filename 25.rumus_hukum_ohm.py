# Dibuat oleh Muhammad Rofi'i Alawi
# Dibuat tanggal 9-12-2024

def ohm():
    I = float(input("Masukkan kuat arus : ")) # ampere
    R = float(input("Masukkan hambatannya : ")) # ohm
    V = lambda I,R: I*R
    print("tegangan listriknya ",V(I,R),"volt")

ohm()