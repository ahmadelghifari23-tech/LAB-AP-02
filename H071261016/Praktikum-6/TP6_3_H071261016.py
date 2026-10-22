def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
	lagu = (judul.strip(), artis.strip(), genre.strip(), durasi)
	playlist.append(lagu)
	genre_set.add(lagu[2])
	return lagu


def tampilkan_playlist(playlist):
    total_durasi_menit = sum(lagu[3] for lagu in playlist) // 60
    total_durasi_detik = sum(lagu[3] for lagu in playlist) % 60
    
    judul_terpanjang = max(len(lagu[0]) for lagu in playlist)
    artis_tepanjang = max(len(lagu[1]) for lagu in playlist)
    genre_terpanjang = max(len(lagu[2]) for lagu in playlist)
    
    garis = "=" * (judul_terpanjang + artis_tepanjang + genre_terpanjang + 20)
    print(garis)
    print(f" No  Judul{(judul_terpanjang - 5) * ' '}  Artis{(artis_tepanjang - 5) * ' '}  Genre{(genre_terpanjang - 5) * ' '}   Durasi")
    print(garis)

    nomor = 1
    for judul, artis, genre, durasi in playlist:
        print(f" {nomor}   {judul.ljust(judul_terpanjang)}  {artis.ljust(artis_tepanjang)}  {genre.ljust(genre_terpanjang)}   {durasi // 60}:{durasi % 60:02d}")
        nomor += 1

    print(garis)
    print(f"Total durasi playlist: {total_durasi_menit} menit {total_durasi_detik} detik\n")


def filter_genre(playlist, genre_target):
	return [lagu for lagu in playlist if lagu[2].lower() == genre_target.strip().lower()]

def hapus_lagu(playlist, nomor):
	if 1 <= nomor <= len(playlist):
		return playlist.pop(nomor - 1)
	return None

def statistik_playlist(playlist, genre_set):

    distribusi = {}
    for _, _, genre, _ in playlist:
        distribusi[genre] = distribusi.get(genre, 0) + 1

    terpanjang = playlist[0]
    terpendek = playlist[0]
    for lagu in playlist:
        if lagu[3] > terpanjang[3]:
            terpanjang = lagu
        if lagu[3] < terpendek[3]:
            terpendek = lagu

    print("=" * 40)
    print(" STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 40)
    print(f" Total lagu : {len(playlist)}")
    print(f" Jumlah genre : {len(genre_set)}")
    print(f" Daftar genre : {genre_set}")
    print(" Distribusi genre:")
    for genre, jumlah in distribusi.items():
        print(f" {genre} : {'#' * jumlah} ({jumlah})")
    print(f" Lagu terpanjang : {terpanjang[0]} ({terpanjang[3] // 60}:{terpanjang[3] % 60:02d})")
    print(f" Lagu terpendek : {terpendek[0]} ({terpendek[3] // 60}:{terpendek[3] % 60:02d})")
    print("=" * 40)

playlist = []
genre_set = set()

print("=" * 40)
print(" PLAYLIST MUSIK - PLAYTUNE")
print("=" * 40)
while True:
	print("Menu:")
	print("1. Tambah Lagu")
	print("2. Tampilkan Playlist")
	print("3. Filter berdasarkan Genre")
	print("4. Hapus Lagu")
	print("5. Statistik Playlist")
	print("6. Keluar")
	pilihan = input("Pilih menu (1-6): ").strip()

	if pilihan == "1":
			judul = input("Judul lagu: ")
			artis = input("Artis: ")
			
			valid_genre = {"Pop", "Rock", "Jazz", "RnB", "Dangdut"}
			while True:
				genre_input = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip()
				genre_terpilih = None
				for i in valid_genre:
					if i.lower() == genre_input.lower():
						genre_terpilih = i
						break
				
				if genre_terpilih:
					genre = genre_terpilih
					break
				else:
					print("Genre yang anda masukkan tidak valid")
					
			try:
				durasi = int(input("Durasi (dalam detik): "))
				if durasi <= 0:
					raise ValueError
			except ValueError:
				print("Durasi harus berupa angka positif.")
				continue
			lagu = tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
			print(f"Lagu '{lagu[0]}' oleh {lagu[1]} berhasil ditambahkan!")
	
	elif pilihan == "2":
		if playlist:
			tampilkan_playlist(playlist)
		else:
			print("Playlist masih kosong.")
	elif pilihan == "3":
		if playlist:
			print(f"Genre tersedia: {genre_set}")
			genre_target = input("Masukkan genre yang ingin difilter: ")
			hasil = filter_genre(playlist, genre_target)
			print(f"Lagu bergenre '{genre_target}':")
			if hasil:
				nomor = 1
				for judul, artis, _, durasi in hasil:
					print(f" {nomor}. {judul} - {artis} ({durasi // 60}:{durasi % 60:02d})")
					nomor += 1
			else:
				print("Tidak ada lagu dengan genre tersebut.")
		else:
			print("Playlist masih kosong.")
			
	elif pilihan == "4":
		if playlist:
			tampilkan_playlist(playlist)
			try:
				nomor = int(input("Nomor lagu yang ingin dihapus: "))
			except ValueError:
				print("Masukkan nomor yang valid.")
				continue
			lagu = hapus_lagu(playlist, nomor)
			if lagu is None:
				print("Nomor lagu tidak valid.")
			else:
				genre_set.clear()
				for genre in playlist:
					genre_set.add(genre[2])
				print(f"Lagu '{lagu[0]}' berhasil dihapus.")
		else:
			print("Playlist masih kosong.")

	elif pilihan == "5":
		if playlist:
			statistik_playlist(playlist, genre_set)
		else:
			print("Playlist masih kosong.")
	elif pilihan == "6":
		print("Terima kasih telah menggunakan PlayTune!")
		break
	else:
		print("Pilihan tidak valid. Silakan pilih 1-6.")
