# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal: 12-1-2025

import sys
import time

while True:
  jam = time.strftime("%H:%M:%S", time.localtime())
  sys.stdout.write("\r" + "sekarang jam : " + jam)
  sys.stdout.flush()
  time.sleep(1)

