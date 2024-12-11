# Dibuat oleh Muhammad Rofi'i Alawi
# Dibuat tanggal 9-12-2024

def energi_potensial():
    m = int(input("Masukkan massa benda = ")) # kg
    g = 10 # m/s2
    h = int(input("Masukkan tinggi benda dari permukaan tanah = ")) # meter
    Ep = lambda m,g,h: m*g*h # Energi potensial (J)
    print("Ep = ",Ep(m,g,h),"Joule")

energi_potensial()