# Dibuat oleh M.Rofi'i Alawi
# Tanggal pengerjaan: 8-10-2024

print('='*40)
print("Rumus Jajar Genjang")
print('='*40)

def jajar_genjang():

    alas = int(input("Masukkan alas : "))
    tinggi = int(input("Masukkan tinggi : "))
    sisi_miring = int(input("Masukkan  sisi miring : "))
    luas =  lambda alas,tinggi: alas * tinggi
    keliling = lambda alas,sisi_miring : 2*(alas+sisi_miring)
    print('Luas = ',luas(alas,tinggi),"cm2")
    print("Keliling = ",keliling(alas,sisi_miring),'cm')

jajar_genjang()

