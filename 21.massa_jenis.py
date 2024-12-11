# Dibuat oleh Muhammad Rofi'i Alawi
# Dibuat tanggal 9-12-2024

def massa_jenis():
    m = int(input("massa = ")) # massa (kg) 
    v = int(input("volume = ")) # volume (m3)
    p = lambda m,v: m/v
    print("p = ",p(m,v),"kg/m3")

massa_jenis()
massa_jenis()
