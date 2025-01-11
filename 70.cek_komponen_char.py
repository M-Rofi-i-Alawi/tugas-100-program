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