# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal: 12-1-2025

import sys
import time

def jalanin_lirik():
  lirik = [
      ("I know a place",0.1),
      ("It's somewhere I go when I need to remember your face",0.2),
      ("We get married in our heads",0.2),
      ("Something to do while we try to recall how we me",0.2),
      ("",0.5),
      ("Do you think I have forgotten?",0.2),
      ("Do you think I have forgotten?",0.2),
      ("Do you think I have forgotten",0.2),
      ("About you?",0.2),
      ("",0.6),
      ("You and I (don't let go)",0.2),
      ("We're alive (don't let go)",0.2),
      ("With nothing to do, I could lay and just look in your eyes",0.5),
      ("Wait (don't let go)",0.1),
      ("And pretend (don't let go)",0.2),
      ("And pretend (don't let go)",0.2),
      ("Hold on and hope that we'll find our way back in the end",0.5),
      ("",0.5)
  ]

  delay = [0.3,0.6,0.4,0.6,0.7,0.4,0.4,0.4,0.3,0.7,0.2,0.3,0.5,0.2,0.2,0.5,0.5]
  print("\n   About You 1975  ")
  time.sleep(2)
  for i, (baris_lagu,delay_karakter) in enumerate(lirik):
    for karakter in baris_lagu:
        print(karakter, end='')
        sys.stdout.flush()
        time.sleep(delay_karakter)
    time.sleep(delay[i])
    print('')
  print("// code by Rofi")

jalanin_lirik()