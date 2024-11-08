# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2 (2024)
# Dibuat tanggal 8-11-2024 (Jum'at)


print('='*40)
print('Rumus jarak')
print('='*40)

def jarak():
    v = float(input("Masukkan kecepatannya : "))
    t = float(input("Masukkan waktunya : "))
    S = lambda v,s: v*t
    print("Jadi jaraknya adalah = ",S(v,t),"km")
    
jarak()