ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k):
	posisi = ALFABET.find(ch.lower())
	if posisi == -1:
		return ch

	hasil = ALFABET[(posisi + k) % len(ALFABET)]
	return hasil.upper() if ch.isupper() else hasil

def mesin_enkripsi(teks, k):
	return "".join(cek_sandi(ch, k) for ch in teks)

def mesin_dekripsi(teks, k):
	return mesin_enkripsi(teks, -k)

def retas_sandi(sandi, kata_kunci):
	kemungkinan = []
	kata_kunci = kata_kunci.lower()

	for kunci in range(26):
		pesan_asli = mesin_dekripsi(sandi, kunci)
		if pesan_asli.lower().find(kata_kunci) != -1:
			kemungkinan.append((kunci, pesan_asli))

	return kemungkinan

sandi = input("Masukan pesan tersita: ")
kata_kunci = input("Masukan kata kunci target: ")
print("Output Deskripsi:", retas_sandi(sandi, kata_kunci))
