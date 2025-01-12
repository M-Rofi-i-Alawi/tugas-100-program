# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal: 12-1-2025

from turtle import*
speed(0)
bgcolor('black')
hideturtle()

warna = [(78,253,84),
         (32,210,244),
         (255,7,58)]

def putar(n,x,angle):
  for i in range(n):
      colormode(255)

      pencolor(warna[i%3])
      fillcolor(warna[i%3])

      begin_fill()

      for _ in range(5):
          forward(5 * n-5 *i)
          right(x)
          forward(5 * n-5 * i)
          right(72 -x)

      end_fill()
      rt(angle)
  done()

n = 30
x = 144
angle = 25

putar(n,x,angle)

