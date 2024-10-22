# Dibuat oleh M.Rofi'i Alawi
# Tanggal pengerjaan: 6-10-2024

print("Rumus Segitiga")

def segitiga():
    alas=int(input("Masukkan alas : "))
    tinggi=int(input("Masukkan tinggi : "))
    a=int(input("Masukkan sisi a : "))
    b=int(input("Mbsukkan sisi b : "))
    c=int(input("Masukkan sisi c : "))
    L=lambda alas,tinggi: 1/2*alas*tinggi
    K=lambda a,b,c: a+b+c
    print("Luas = ",L(alas,tinggi),"cm2")
    print("Keliling = ",K(a,b,c),"cm")

segitiga()