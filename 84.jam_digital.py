# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal: 12-1-2025

from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('jam digital')

def waktu():
  string = strftime('%H:%M:%S %p')
  lbl.config(text=string)
  lbl.after(1000, waktu)

lbl = Label(root, font=('times new roman', 50, 'bold'),
            background = 'green',
            foreground='white')
lbl.pack(anchor=CENTER)
waktu()

mainloop()