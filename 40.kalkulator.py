# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal : 6-1-2025

print('='*40)
print('Kalkulator')
print('='*40)

def pertambahan():
    angka1 = int(input("Masukkan angka pertama : "))
    angka2 = int(input("Masukkan angka kedua : "))
    angka3 = int(input("Masukkan angka ketiga : "))
    pertambahan = lambda angka1,angka2,angka3: angka1+angka2+angka3
    print("hasilnya adalah = ",pertambahan(angka1,angka2,angka3))

def pengurangan():
    angka1 = int(input("Masukkan angka pertama : "))
    angka2 = int(input("Masukkan angka kedua : "))
    angka3 = int(input("Masukkan angka ketiga : "))
    pengurangan = lambda angka1,angka2,angka3: angka1-angka2-angka3
    print("hasilnya adalah = ",pengurangan(angka1,angka2,angka3))

def perkalian():
    angka1 = int(input("Masukkan angka pertama : "))
    angka2 = int(input("Masukkan angka kedua : "))
    angka3 = int(input("Masukkan angka ketiga : "))
    perkalian = lambda angka1,angka2,angka3: angka1*angka2*angka3
    print("hasilnya adalah = ",perkalian(angka1,angka2,angka3))
def pembagian():
    angka1 = int(input("Masukkan angka pertama : "))
    angka2 = int(input("Masukkan angka kedua : "))
    angka3 = int(input("Masukkan angka ketiga : "))
    pembagian = lambda angka1,angka2,angka3: angka1/angka2/angka3
    print("hasilnya adalah = ",pembagian(angka1,angka2,angka3))

# Hasil program
print("Pilih program yang pertambahan/pengurangan/perkalian/pembagian?")
menu = input("Masukkan pilihan (pertambahan/pengurangan/perkalian/pembagian): ")
if menu == "pertambahan":
    pertambahan()
elif menu == "pengurangan":
    pengurangan()
elif menu == "perkalian":
    perkalian()
elif menu == "pembagian":
    pembagian()
