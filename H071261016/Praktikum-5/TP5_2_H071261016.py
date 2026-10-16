def cek_kata(teks_kecil, kata_kecil):
    if kata_kecil == "":
        return []
    indeks = []
    mulai = 0

    while True:
        posisi = teks_kecil.find(kata_kecil, mulai)
        if posisi == -1:
            break
        indeks.append(posisi)
        mulai = posisi + 1

    return indeks

def cek_batas_kata(teks, i, panjang):
    sebelum_huruf = i > 0 and (teks[i - 1].lower() != teks[i - 1].upper())
    sesudah_huruf = i + panjang < len(teks) and (teks[i + panjang].lower() != teks[i + panjang].upper())
    return not sebelum_huruf and not sesudah_huruf

def sensor_kata(teks, kata, simbol):
    indeks_sensor = []
    for i in cek_kata(teks.lower(), kata.lower()):
        if cek_batas_kata(teks, i, len(kata)):
            indeks_sensor.append(i)

    hasil = ""
    posisi_terakhir = 0
    for i in indeks_sensor:
        hasil = hasil + teks[posisi_terakhir:i]
        hasil = hasil + simbol * len(kata)
        posisi_terakhir = i + len(kata)
    hasil = hasil + teks[posisi_terakhir:]

    return hasil, len(indeks_sensor), indeks_sensor

teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")

hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)
print(f"Hasil Teks: {hasil}")
print(f"Jumlah: {jumlah}")
print(f"Indeks: {indeks}")