while True:
    try:
        jumlah_kursi = int(input("Masukkan jumlah kursi bus: "))
        if jumlah_kursi <= 0:
            print("Input jumlah kursi tidak valid!")
            continue
    except ValueError:
        print("Input jumlah kursi harus berupa angka!")    
        continue
    break
    
total_pendapatan = 0

while jumlah_kursi > 0:
    print("Sisa kursi =",jumlah_kursi)
    try:
        umur = int(input("Masukkan umur penumpang: "))
    except ValueError:
        print("Input umur harus berupa angka!")
        
    else:
        if umur < 0:
            print("Umur tidak valid!")
            continue
        elif umur <= 5:
            kategori = "Balita"
            harga_tiket = 0
            info_tiket = "- Tiket gratis (Rp 0)"
        elif umur <= 12:
            kategori = "Anak"
            harga_tiket = 50000
            info_tiket = "- Harga = Rp 50000"
        else:
            kategori = "Dewasa"
            harga_tiket = 100000
            info_tiket = "- Harga = Rp 100000"

    print("Kategori :", kategori,info_tiket)

    jumlah_kursi -= 1
    total_pendapatan += harga_tiket

print()
print("---Seluruh kursi telah terisi---")
print("Total pendapatan perjalanan PO BUS kali ini: Rp",total_pendapatan)