import random
angka_rahasia = random.randint(1, 100)
print("Tebak angka antara 1-100.")
while True:
    tebakan = int(input("Masukkan tebakan Anda: "))
    if tebakan < angka_rahasia:
        print("Terlalu kecil!")
    elif tebakan > angka_rahasia:
        print("Terlalu besar!")
    else:
        print(f"Selamat, Anda berhasil menebak angka {angka_rahasia}!")
        break
