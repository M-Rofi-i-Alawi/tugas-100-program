# Dibuat oleh M.Rofi'i Alawi
# Tanggal pengerjaan: 6-10-2024

print("===========Program persegi==========")

def persegi():
    sisi = int(input('Sisi\t\t: '))
    luas = lambda s: s*s
    keliling = lambda s: 4*s
    
    print(f'Luas\t\t: ',luas(sisi),'cm2')
    print(f"Keliling\t: ",keliling(sisi),"cm")

persegi()
