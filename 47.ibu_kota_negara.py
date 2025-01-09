# Dibuat oleh Muhammad Rofi'i Alawi
# Kelas X PPLG 2
# Tanggal : 8-1-2025

print("capital city")
print("="*20)

negara = ["indonesia","jepang","china","korea selatan","korea utara","malaysia","singapura"]
ibukota =["Jakarta","Tokyo","Beijing","Seoul","Pyongyang","Kuala Lumpur","Singapura"]

capital_city = dict(zip(negara,ibukota))
#print(capital_city)

while True:
	nama_negara = input("Negara: ").lower()
	nama_ibukota = capital_city[nama_negara]
	
	print("Ibukota",nama_negara.title(),"adalah",nama_ibukota,end="\n\n")