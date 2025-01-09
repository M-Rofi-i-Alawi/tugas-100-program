# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal : 6-1-2025

print("="*20)
print("Program pajak gak pake kondisi")
print("="*20)

def pajak():
    gaji = int(input("Masukkan gaji yang didapat dalam sebulan : "))
    pajak = float(input("Masukkan persentase pajak yang didapatkan : "))
    yang_harus_dibayar = lambda gaji,pajak: pajak/100*gaji
    print("Jumlah pajak yang harus dibayar adalah = ",yang_harus_dibayar(gaji,pajak),"rupiah")

pajak()