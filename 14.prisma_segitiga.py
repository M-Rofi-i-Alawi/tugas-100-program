# Dibuat oleh M.Rofi'i Alawi
# Tanggal pengerjaan: 25-10-2024

print("="*40)
print("Prisma segitiga")
print("="*40)

def prisma_segitiga():
    luas_alas = int(input("Masukkan luas alas : ")) 
    keliling_alas = int(input("Masukkan keliling alas :"))
    tinggi_prisma = int(input("Masukkan tinggi prisma : "))
    keliling_sisi = int(input("Masukkan keliling sisi : "))
    tinggi_segitiga = int(input("Masukkan tinggi segitiga : "))    
    L = lambda luas_alas,keliling_alas,tinggi_prisma: (2*luas_alas)+(keliling_alas*tinggi_prisma) # Ini rumus luas permukaan
    K = lambda luas_alas,keliling_sisi: (2*luas_alas)+(3*keliling_sisi)
    V = lambda luas_alas,tinggi_segitiga,tinggi_prisma: ((luas_alas*tinggi_segitiga)/2)*tinggi_prisma
    print("Luas Permukaan = ",L(luas_alas,keliling_alas,tinggi_prisma),"cm")
    print("Keliling prisma segitiga = ",K(luas_alas,keliling_sisi),"cm")
    print("Volume = ",V(luas_alas,tinggi_segitiga,tinggi_prisma),"cm")

prisma_segitiga()