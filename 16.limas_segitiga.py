# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2 (2024)
# Dibuat tanggal 8-11-2024 (Jum'at)

print('='*40)
print('Rumus limas segitiga')
print('='*40)

def limas_segitiga():
    luas_alas = float(input("Masukkan luas alas: "))
    tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))
    tinggi_limas = float(input("Masukkan tinggi limas: "))
    luas_sisi_tegak_segitiga = float(input("Masukkan luas sisi tegak setiga: "))
    Lp = lambda luas_alas,luas_sisi_tegak_segitiga: (luas_alas+luas_sisi_tegak_segitiga)
    V = lambda luas_alas,tinggi_sgitiga,tinggi_limas: 1/3*(luas_alas*tinggi_segitiga)*tinggi_limas
    print("Luas permukaan = ",Lp(luas_alas,luas_sisi_tegak_segitiga),"cm2")
    print("Volume = ",V(luas_alas,tinggi_segitiga,tinggi_limas),"cm3")
    
limas_segitiga()