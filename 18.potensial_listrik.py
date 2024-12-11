# Dibuat oleh M.Rofi'i Alawi
# Kelas 10 PPLG 2
# Dibuat tanggal 7-12-2024


print("="*40)
print("Rumus potensial listrik ke statis")
print("="*40)

def potensial_listrik():
    q = int(input("masukkan muatan : "))
    v1 = int(input("Masukkan volt 1 : "))
    v2 = int(input("Masukkan volt 2 : "))
    w = lambda q,v2,v1: q*(v2-v1)
    print("Jadi energi listriknya adalah =",w(q,v2,v1),"Joule")

potensial_listrik()