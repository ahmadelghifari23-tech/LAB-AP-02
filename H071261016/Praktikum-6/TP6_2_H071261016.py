def daftar_kandidat(kandidat_set, nama):
	nama = nama.strip().capitalize()
	if not nama:
		return
	if nama in kandidat_set:
		print(f"'{nama}' sudah terdaftar sebagai kandidat!")
	else:
		kandidat_set.add(nama)
		print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_asli = nama_pemilih.strip()

    if nama_asli.lower() in rekap_suara:
        print(f"'{nama_asli}' sudah memberikan suara sebelumnya!")
        return

    pilihan = pilihan.strip().capitalize()
    if pilihan not in kandidat_set:
        print(f"Kandidat '{pilihan}' tidak terdaftar! Suara tidak dicatat.")
        return

    rekap_suara[nama_asli.lower()] = pilihan
    print(f"Suara '{nama_asli}' untuk '{pilihan}' berhasil dicatat!")


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}
    for kandidat in kandidat_set:
        perolehan[kandidat] = 0  
    for pilihan in rekap_suara.values():
        if pilihan in perolehan:
            perolehan[pilihan] += 1
    return perolehan


def tampilkan_hasil(perolehan):
	print("========================================")
	print(" HASIL PEMILIHAN KETUA KELAS")
	print("========================================")
	for kandidat, jumlah in perolehan.items():
		print(f" {kandidat}: {jumlah} suara")

	total_suara = sum(perolehan.values())
	print(f"Total suara masuk: {total_suara}")

	if perolehan:
		suara_tertinggi = max(perolehan.values())
		pemenang = [nama for nama, jumlah in perolehan.items()
					if jumlah == suara_tertinggi]
		if len(pemenang) > 1:
			print(f"Hasil SERI antara: {', '.join(pemenang)}")
			print("Perlu dilakukan pemilihan ulang!")
		else:
			print(f"PEMENANG: {pemenang[0]} dengan {suara_tertinggi} suara!")
	print("========================================")



kandidat_set = set()
rekap_suara = {}

print("========================================")
print(" SISTEM PEMILIHAN KETUA KELAS")
print("========================================")
while len(kandidat_set) < 2:
	print("--- FASE PENDAFTARAN KANDIDAT ---")
	while True:
		nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")
		if not nama.strip():
			break
		daftar_kandidat(kandidat_set, nama)
	if len(kandidat_set) < 2:
		print("Minimal harus ada 2 kandidat. Silakan daftarkan kandidat lagi.")

print(f"Kandidat terdaftar: {kandidat_set}")
print("--- FASE PEMUNGUTAN SUARA ---")
while True:
	nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ")
	if not nama_pemilih.strip():
		break
	print(f"Kandidat yang tersedia: {kandidat_set}")
	pilihan = input("Pilih kandidat: ")
	berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

tampilkan_hasil(hitung_suara(rekap_suara, kandidat_set))