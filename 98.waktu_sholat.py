# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal: 12-1-2025

print("program jadwal sholat")

import requests

# Input lokasi
kota = input("Masukkan kota untuk jadwal sholat: ")

# API URL (menggunakan Aladhan API)
url = f"http://api.aladhan.com/v1/timingsByCity?city={kota}&country=Indonesia&method=2"

# Meminta data dari API
response = requests.get(url)
data = response.json()

# Mengecek apakah permintaan berhasil
if response.status_code == 200 and data["code"] == 200:
    timings = data["data"]["timings"]
    print(f"\nJadwal Sholat untuk {kota.capitalize()}:\n")
    print(f"Subuh   : {timings['Fajr']}")
    print(f"Terbit  : {timings['Sunrise']}")
    print(f"Dzuhur  : {timings['Dhuhr']}")
    print(f"Ashar   : {timings['Asr']}")
    print(f"Magrib  : {timings['Maghrib']}")
    print(f"Isya    : {timings['Isha']}")
else:
    print("Gagal mengambil data jadwal sholat. Pastikan nama kota benar.")
