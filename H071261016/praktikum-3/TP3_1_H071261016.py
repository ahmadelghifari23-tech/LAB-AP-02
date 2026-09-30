print("Rekapitulasi transaksi dins store")
print("ketik 0 untuk menutup toko dan mengakhiri transaksi")

while True:
    try:
        jumlah_item = int(input("masukkan jumlah item =")) 
    except:
        ValueError 
        print("input harus berupa angka")
        continue
    else:
        if jumlah_item < 0:
            print("jumlah tidak boleh negatif")
            continue
        elif jumlah_item > 100:
            print("maksimal 100 item per trensaksi")
            continue
        elif jumlah_item == 0:
            print("toko tutup. sesi rekap selesai")
            break

    print("transaksi",jumlah_item,"item berhasil")