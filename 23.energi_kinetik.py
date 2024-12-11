# Dibuat oleh Muhammad Rofi'i Alawi
# Dibuat tanggal 9-12-2024

def Ek():
    m = int(input("Masukkan massa benda : "))
    v = int(input("Masukkan kecepatan benda : "))
    Ek = lambda m,v: 1/2*m*v
    print("Ek = ",Ek(m,v),"Joule")

Ek()