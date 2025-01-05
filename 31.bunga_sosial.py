# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal : 31-12-2024

print("="*20 + " Program Bunga dalam aritmatika sosial " + "="*20)

def bunga_harian():
    print("="*25+"hitung bunga harian"+"="*25)
    p = float(input("Masukkan suku bunga : "))
    Mo = int(input("Masukkan modal awal : "))
    t = int(input("Masukkan jumlah hari : "))
    harian = lambda p,Mo,t: p*Mo*t/360
    print("Jadi bunga dalam harian adalah = ",harian(p,Mo,t))

def bunga_bulanan():
    print("="*25+"hitung bunga bulanan"+"="*25)
    p = float(input("Masukkan suku bunga : "))
    Mo = int(input("Masukkan modal awal : "))
    t = int(input("Masukkan jumlah bulan : "))
    bulanan = lambda p,Mo,t: p*Mo*t/12
    print("Jadi bunga dalam bulanan adalah = ",bulanan(p,Mo,t))

def bunga_tahunan():
    print("="*25+"hitung bunga tahunan"+"="*25)
    p = float(input("Masukkan suku bunga : "))
    Mo = int(input("Masukkan modal awal : "))
    t = int(input("Masukkan jumlah tahun : "))
    tahunan = lambda p,Mo,t: p*Mo*t
    print("Jadi bunga dalam tahunan adalah = ",tahunan(p,Mo,t))

print("Pilih bunga mau bentuk apa?")
pilihan = input("Pilih mau yang mana? (tahunan/bulanan/harian) : ")
if pilihan == "harian":
    bunga_harian()
elif pilihan == "bulanan":
    bunga_bulanan()
elif pilihan == "tahunan":
    bunga_tahunan()
