def rekap_nilai(*nilai):
	return sum(nilai) / len(nilai), max(nilai), min(nilai)

nilai_siswa = []

while True:
    nilai_awal = float(input("Masukkan nilai ujian siswa (kosongkan untuk selesai): "))
    if nilai_awal == "":
        break
    if "." in nilai_awal:
        angka = float(nilai_awal)
    else:
        angka = int(nilai_awal)

    nilai_siswa += [angka]

if nilai_siswa == []:
    print("Data nilai tidak tersedia.")
else:
    rata_rata, nilai_tertinggi, nilai_terendah = rekap_nilai(*nilai_siswa)
    print(f"Rata-rata kelas: {rata_rata}")
    print(f"Nilai tertinggi: {nilai_tertinggi}")
    print(f"Nilai terendah: {nilai_terendah}")