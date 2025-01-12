# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal: 12-1-2025

import turtle
warna = ['red','purple','blue','green','violet','pink']

pen = turtle.Pen()
turtle.bgcolor('black')

for x in range(360):
  pen.pencolor(warna[x%6])
  pen.width(x//100+1)
  pen.forward(x)
  pen.left(59)
