import re


print("=== Pembersihan Data Nomor Telepon ===")
jumlah_data = int(input("\nMasukkan jumlah data: "))

data_telepon = []
nomor_valid = []

for i in range(jumlah_data):
	nomor = input(f"\nNomor ke-{i + 1}: ")
	nomor_bersih = re.sub(r"[ -]", "", nomor)
	valid = re.fullmatch(r"\d{10,13}", nomor_bersih) is not None

	data_telepon.append((nomor, nomor_bersih, valid))
	if valid:
		nomor_valid.append(nomor_bersih)

print("\n--- Hasil Pembersihan ---")
nomor = 1
for sebelum, sesudah, valid in data_telepon:
    status = "Valid" if valid else "Tidak valid"
    print(f"\nData {nomor}:")
    print(f"Sebelum : {sebelum}")
    print(f"Sesudah : {sesudah}")
    print(f"Status  : {status}")
    nomor += 1

print(f"\nJumlah nomor valid: {len(nomor_valid)}")
