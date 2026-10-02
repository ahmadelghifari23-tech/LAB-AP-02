def konversi_suhu(nilai, skala_asal, skala_tujuan):
	skala_asal = skala_asal.upper()
	skala_tujuan = skala_tujuan.upper()
	try:
		if skala_asal not in ("C", "F", "K") and skala_tujuan not in ("C", "F", "K"):
			raise ValueError

		if skala_asal == "C":
			celsius = nilai
		elif skala_asal == "F":
			celsius = (nilai - 32) * 5 / 9
		else:
			celsius = nilai - 273

		if skala_tujuan == "C":
			return celsius
		if skala_tujuan == "F":
			return celsius * 9 / 5 + 32
		return celsius + 273
	except ValueError:
		raise ValueError("Skala suhu tidak dikenali.")

print("=== Konversi Suhu ===")
while True:
	input_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
	if input_suhu.strip().lower() == "selesai":
		break

	try:
		suhu = float(input_suhu)
	except ValueError:
		print("Error: Masukkan nilai suhu yang valid.")
		continue

	skala_asal = input("Skala asal (C/F/K): ").strip()
	skala_tujuan = input("Skala tujuan (C/F/K): ").strip()
	try:
		hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)
		print(f"Hasil: {suhu} {skala_asal} = {hasil} {skala_tujuan}")
	except ValueError:
		print("Error: Skala suhu tidak dikenali.")
