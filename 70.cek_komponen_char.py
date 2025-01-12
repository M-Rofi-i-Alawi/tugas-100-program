# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal: 12-1-2025

print("Program mengecek apakah ada komponen char atau string di string")
print("=" * 30)

# mengecek apakah ada komponen char atau string di string

nama_lengkap = "Muhammad Rofi'i Alawi"
nama_awal = "Muhammad"
nama_tengah = "Rofi'i"
tengah = "Rofi'i"
nama_akhir = "Alawi"

status = tengah in nama_lengkap
print("string " + tengah + " ada di " + nama_lengkap + " = " + str(status))

Tengah = "rofi'i"
status = Tengah in nama_lengkap
print("string " + Tengah + " ada di " + nama_lengkap + " = " + str(status))

tengah = "Rofi'i"
status = tengah not in nama_lengkap
print("string " + tengah + " ada di " + nama_lengkap + " = " + str(status))