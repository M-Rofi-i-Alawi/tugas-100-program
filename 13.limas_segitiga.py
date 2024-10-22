# Dibuat oleh M.Rofi'i Alawi
# Tanggal pengerjaan: 10-10-2024

print('='*40)
print('Program limas segitiga')
print('='*40)

def limas_segitiga():
    luas_alas = int(input("Masukkan luas alas : "))
    t = int(input("Masukkan tinggi : "))
    luas_sisi_tegak = int(input("Masukkan luas sisi tegak : "))
    V = lambda luas_alas,t: 1/3*luas_alas*t
    Lp = lambda luas_alas,luas_sisi_tegak: luas_alas+luas_sisi_tegak
    print("Volume = ",V(luas_alas,t),"cm3")
    print("Luas Peermukaan = ",Lp(luas_alas,luas_sisi_tegak),"cm2")

limas_segitiga()