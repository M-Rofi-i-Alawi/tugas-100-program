# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal: 12-1-2025

import requests

api_url = "https://api.numlookupapi.com/v1/validate"  # Ganti dengan URL API yang Anda gunakan
headers = {"Authorization": "Bearer YOUR_API_KEY"}  # Ganti dengan API Key Anda
params = {"number": "+6287812822400"}  # Ganti dengan nomor Anda

response = requests.get(api_url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    print("Data Ditemukan:", data)
else:
    print("Gagal Mengakses API:", response.status_code)
    print("Pesan Kesalahan:", response.text)

