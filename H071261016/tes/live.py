usia = int(input("Masukkan usia: "))
anggota = input("Apakah anda anggota (ya/tidak):").lower()

if 0 < usia < 5:
    biaya = 0
elif 5 <= usia <= 12:
    biaya = 50000
elif 13 <= usia <= 59:
    biaya = 100000
elif usia >= 60:
    biaya = 70000
else:
    print("Usia tidak valid")

total_biaya = int(biaya * 0.8) if anggota == "ya" else biaya
print("Tarif tiket", total_biaya )
