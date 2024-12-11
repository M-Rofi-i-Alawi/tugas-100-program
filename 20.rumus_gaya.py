# Dibuat oleh Muhammad Rofi'i Alawi
# Dibuat tanggal 9-12-2024

def gaya():
    print("Diketahui: ")
    m = float(input("Masukkan massa benda : "))
    a = float(input("Masukkan percepatan  : "))
    f = lambda m,a: m*a # gaya (Newton atau kg.m/s2)
    print("Ditanya f nya berapa?")
    print("Jawab:")
    print("f =",f(m,a),"kg/ms2")

gaya()
gaya()