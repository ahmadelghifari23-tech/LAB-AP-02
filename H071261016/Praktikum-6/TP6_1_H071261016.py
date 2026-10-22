def tambah_buku(inventaris, judul, penulis, harga, stok):
	buku = {
		"judul": judul,
		"penulis": penulis,
		"harga": harga,
		"stok": stok,
	}
	inventaris.append(buku)
	print(f"Buku '{judul}' berhasil ditambahkan!")


def cari_buku(inventaris, kata_kunci):
    hasil = [
        buku for buku in inventaris
        if kata_kunci.lower() in buku["judul"].lower()
    ]

    if not hasil:
        print("Buku tidak ditemukan.")
        return

    print(f"Ditemukan {len(hasil)} buku:")
    nomor = 1
    for buku in hasil:
        print(
            f" {nomor}. {buku['judul']} - {buku['penulis']} | "
            f"Rp{buku['harga']} | Stok: {buku['stok']}"
        )
        nomor += 1


def update_stok(inventaris, judul, jumlah):
	for buku in inventaris:
		if buku["judul"].lower() == judul.lower():
			stok_baru = buku["stok"] + jumlah
			if stok_baru < 0:
				print("Gagal: stok tidak boleh menjadi negatif.")
				return

			buku["stok"] = stok_baru
			if jumlah > 0:
				print(
					f"Stok '{buku['judul']}' bertambah {jumlah}. "
					f"Stok sekarang: {buku['stok']}"
				)
			elif jumlah < 0:
				print(
					f"Stok '{buku['judul']}' berkurang {abs(jumlah)}. "
					f"Stok sekarang: {buku['stok']}"
				)
			else:
				print(f"Stok '{buku['judul']}' tidak berubah: {buku['stok']}")
			return

	print(f"Error: buku '{judul}' tidak ditemukan.")

def ringkasan_inventaris(inventaris):
	jumlah_jenis = len(inventaris)
	total_stok = sum(buku["stok"] for buku in inventaris)
	total_aset = sum(buku["harga"] * buku["stok"] for buku in inventaris)

	print("========================================")
	print("RINGKASAN INVENTARIS BOOKNEST")
	print("========================================")
	print(f"Jumlah jenis buku : {jumlah_jenis}")
	print(f"Total seluruh stok: {total_stok}")
	print(f"Total nilai aset : Rp{total_aset}")
	print("========================================")

	if inventaris:
		harga_tertinggi = inventaris[0]["harga"]
		for buku in inventaris:
			if buku["harga"] > harga_tertinggi:
				harga_tertinggi = buku["harga"]

		daftar_termahal = []
		for buku in inventaris:
			if buku["harga"] == harga_tertinggi:
				daftar_termahal.append(buku)

		print("Buku termahal:")
		for buku in daftar_termahal:
			print(f"- {buku['judul']} (Rp{buku['harga']})")
	else:
		print("Buku termahal : Tidak ada")

inventaris = []
print("========================================")
print(" SISTEM INVENTARIS TOKO BUKU BOOKNEST")
print("========================================")

while True:
	print("Menu:")
	print("1. Tambah Buku")
	print("2. Cari Buku")
	print("3. Update Stok")
	print("4. Ringkasan Inventaris")
	print("5. Keluar")
	pilihan = input("Pilih menu (1-5): ").strip()

	if pilihan == "1":
		judul = input("Judul buku: ").strip()
		penulis = input("Penulis: ").strip()
		try:
			harga = float(input("Harga: "))
			stok = int(input("Stok awal: "))
			if harga < 0 or stok < 0:
				print("Harga dan stok tidak boleh negatif.")
				continue
		except ValueError:
			print("Harga harus berupa angka dan stok harus berupa bilangan bulat.")
			continue
		tambah_buku(inventaris, judul, penulis, harga, stok)
	elif pilihan == "2":
		kata_kunci = input("Masukkan kata kunci judul: ").strip()
		cari_buku(inventaris, kata_kunci)
	elif pilihan == "3":
		judul = input("Judul buku yang ingin diupdate: ").strip()
		try:
			jumlah = int(
				input("Jumlah perubahan (positif=tambah, negatif=kurang): ")
			)
		except ValueError:
			print("Jumlah perubahan harus berupa bilangan bulat.")
			continue
		update_stok(inventaris, judul, jumlah)
	elif pilihan == "4":
		ringkasan_inventaris(inventaris)
	elif pilihan == "5":
		print("Terima kasih telah menggunakan BookNest!")
		break
	else:
		print("Pilihan tidak valid. Silakan pilih menu 1-5.")


