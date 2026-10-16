def bersihkan_teks(teks):
    ALFABET = "abcdefghijklmnopqrstuvwxyz"
    return "".join(huruf.lower() for huruf in teks if huruf.lower() in ALFABET)

def inti_palindrome(teks):
    teks_bersih = bersihkan_teks(teks)
    palindrom_terpanjang = ""
    indeks_awal = 0
    for i in range(len(teks_bersih)):
        for j in range(i + 1, len(teks_bersih) + 1):
            sub = teks_bersih[i:j]
            if sub == sub[::-1] and len(sub) > len(palindrom_terpanjang):
                palindrom_terpanjang = sub
                indeks_awal = i
    return {
        "teks": palindrom_terpanjang,
        "panjang": len(palindrom_terpanjang),
        "indeks_awal": indeks_awal,
    }

teks = input("Masukkan teks prasasti: ")
teks_bersih = bersihkan_teks(teks)
hasil = inti_palindrome(teks)
print(f"Teks Bersih: {teks_bersih}")
print(f"Output Terharap: {hasil}")