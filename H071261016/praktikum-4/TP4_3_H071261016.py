def hitung_mundur(angka):
	print(angka)
	if angka > 0:
		hitung_mundur(angka - 1)
	else:
		print("Luncurkan!")

while True:
    angka_awal = int(input("Masukkan angka awal hitung mundur: "))
    if angka_awal >= 0:
        break  
    print("Input tidak valid, angka tidak boleh negatif.")

hitung_mundur(angka_awal)

