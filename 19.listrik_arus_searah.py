# Dibuat oleh Muhammad Rofi'i Alawi
# Dibuat tanggal 9-12-2024

def listrik_arus_searah():
    Q = int(input("Jumlah muatan listrik = "))
    t = int(input("Waktu = "))
    R = int(input("Hambatan listrik = "))
    p = int(input("Hambatan jenis penghantar = "))
    L = int(input("Panjang penghantar = "))
    A = int(input("Luas penampang penghantar = "))
    I = lambda Q,t: Q/t
    R = lambda p,L,A: p*L/A
    print("Kuat arus listriknya adalah = ",I(Q,t),"A")
    print("Hambatan listrik = ",R(p,L,A),"Ohm")

listrik_arus_searah()