import tkinter as tk
from tkinter import ttk
from googletrans import Translator

# Fungsi untuk menerjemahkan teks
def translate_text():
    # Ambil teks dari input
    teks_yang_ditranslate = entry.get()
    # Ambil bahasa tujuan
    bahasa_dituju = tombol_bahasa.get()
    
    # Menerjemahkan teks
    translator = Translator()
    translated = translator.translate(teks_yang_ditranslate, dest=bahasa_dituju)
    
    # Menampilkan hasil terjemahan di label
    result_label.config(text=translated.text)

# Membuat jendela utama
root = tk.Tk()
root.title("Translate Bahasa")

# Menambahkan label untuk petunjuk
label = tk.Label(root, text="Teks yang ingin diterjemahkan:")
label.pack(pady=10)

# Menambahkan input text (Entry) untuk pengguna memasukkan teks
entry = tk.Entry(root, width=60)
entry.pack(pady=10)

# Menambahkan label untuk memilih bahasa tujuan
label_bahasa = tk.Label(root, text="Pilih Bahasa :")
label_bahasa.pack(pady=10)

# Daftar bahasa yang bisa dipilih (kode bahasa)
languages = ['english', 'indonesian', 'italian', 'japan', 'korean', 'russian','arabian','romanian']

# Membuat combobox untuk memilih bahasa
tombol_bahasa = ttk.Combobox(root, values=languages, state="readonly")
tombol_bahasa.set('pilih bahasa')  # Set default bahasa ke Indonesia
tombol_bahasa.pack(pady=10)

# Tombol untuk menerjemahkan
translate = tk.Button(root, text="Terjemahkan", command=translate_text)
translate.pack(pady=50)

# Label untuk menampilkan hasil terjemahan
result_label = tk.Label(root, text="", font=("Novel", 15), width=100, height=10, relief="solid")
result_label.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()