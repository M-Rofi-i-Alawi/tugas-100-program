# Dibuat oleh Muhammad Rofi'i Alawi
# Dibuat tanggal 8-11-2024 (Jum'at)

print('='*40)
print('Rumus limas Segi empat')
print('='*40)

def limas_segi_empat():
    sisi = float(input("Masukkan sisi: "))
    tinggi_limas = float(input("Masukkan tinggi limas: "))
    tinggi_segitiga_sisi_tegak = float(input("Masukkan tinggi segitiga sisi tegak: "))
    Lp = lambda sisi,tinggi_segitiga_sisi_tegak:(sisi**2)+(4*1/2*sisi*tinggi_segitiga_sisi_tegak)
    V = lambda sisi,tinggi_limas: (1/3*sisi**2*tinggi_limas)
    print("Luas permukaan = ",Lp(sisi,tinggi_segitiga_sisi_tegak),"cm2")
    print("Volume = ",V(sisi,tinggi_limas),"cm3")
    
limas_segi_empat()