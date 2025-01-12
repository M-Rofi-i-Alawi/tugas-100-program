# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal: 12-1-2025

print("Program mengkonversi karakter tidak umum menjadi lowercase karakter umum")
print("=" * 30)

# casefold() <-- sama dengan lower()
# bedanya, casefold() mengkonversi karakter tidak umum menjadi lowercase karakter umum
# Contoh  : 'ß' (german) = menjadi 'ss'

tes_casefold = "außen IS AN GERMAN WORD"
cek_hasil = tes_casefold.casefold()
print(cek_hasil)