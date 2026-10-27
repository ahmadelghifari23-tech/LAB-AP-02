from datetime import datetime
from pathlib import Path
import random

DIREKTORI_INVOICE = Path("invoices")
FILE_RIWAYAT = Path("trx_history.txt")


def buat_invoice(kasir):
    daftar_produk = []
    while True:
        while True:
            nama = input("Masukkan nama produk               : ").strip()
            if nama:
                break
            print("Nama produk tidak boleh kosong.")
            
        try:
            harga = int(input("Masukkan harga produk              : "))
            jumlah = int(input("Masukkan jumlah produk             : "))
            if harga <= 0 or jumlah <= 0:
                print("Masukkan angka lebih dari 0")
                continue
        except ValueError:
            print("Masukkan angka bilangan bulat")
            continue
        daftar_produk.append((nama, harga, jumlah))
        
        while True:
            print("=" * 54)
            tambah = input("Tambah produk? (y/t)               : ").strip().lower()
            print("=" * 54)
            if tambah in ["y", "t"]:
                break
            print("Pilihan tidak valid. Masukkan 'y' atau 't'.")
            
        if tambah == "t":
            break

    waktu_transaksi = datetime.now()
    DIREKTORI_INVOICE.mkdir(exist_ok=True)
    
    inisial = "".join(bagian[0] for bagian in kasir.split()).upper()
    while True:
        id_transaksi = (
            f"{inisial}{waktu_transaksi:%y%m%d%H%M}{random.randint(100, 999)}"
        )
        jalur_invoice = DIREKTORI_INVOICE / f"{id_transaksi}.txt"
        if not jalur_invoice.exists():
            break

    total = sum(harga * jumlah for _, harga, jumlah in daftar_produk)
    baris_teks = [
        "=" * 48,
        "                 INVOICE",
        "=" * 48,
        f"ID Transaksi : {id_transaksi}",
        f"Waktu        : {waktu_transaksi:%Y-%m-%d %H:%M:%S}",
        f"Kasir        : {kasir}",
        "-" * 48,
    ]
    for nama, harga, jumlah in daftar_produk:
        baris_teks.extend([nama, f"  {jumlah} x Rp. {harga:,} = Rp. {harga * jumlah:,}"])
    baris_teks.extend(["-" * 48, f"TOTAL        : Rp. {total:,}", "=" * 48])
    jalur_invoice.write_text("\n".join(baris_teks) + "\n")

    pemisah = "=" * 70
    if not FILE_RIWAYAT.exists() or FILE_RIWAYAT.stat().st_size == 0:
        with FILE_RIWAYAT.open("w") as riwayat:
            riwayat.write(pemisah + "\n")
            riwayat.write("| Waktu               | ID Transaksi       | Nominal Transaksi |\n")
            riwayat.write(pemisah + "\n")
    with FILE_RIWAYAT.open("a") as riwayat:
        riwayat.write(
            f"| {waktu_transaksi:%Y-%m-%d %H:%M:%S} | {id_transaksi:<18} "
            f"| Rp. {total:<13,} |\n{pemisah}\n"
        )

    print("=" * 54)
    print("                    TRANSAKSI BERHASIL")
    print("=" * 54)

def cari_invoice():
    id_transaksi = input("Masukkan ID transaksi: ").strip()
    jalur_invoice = DIREKTORI_INVOICE / f"{id_transaksi}.txt"
    try:
        print("\n" + jalur_invoice.read_text(), end="")
    except FileNotFoundError:
        print("Invoice tidak ditemukan.")


print("=" * 54)
print("                        SELAMAT DATANG")
print("=" * 54)
while True:
    kasir = input("Masukkan nama kasir                : ").strip()
    if kasir:
        break
    print("Nama tidak boleh kosong")

while True:
    print("=" * 54)
    print("Pilih opsi:")
    print("1. Transaksi baru")
    print("2. Cari transaksi")
    print("3. Keluar")
    print("=" * 54)
    pilihan = input("Masukkan opsi pilihan              : ").strip()
    print("=" * 54)
    
    if pilihan == "1":
        buat_invoice(kasir)
    elif pilihan == "2":
        cari_invoice()
    elif pilihan == "3":
        print("Terima kasih.")
        break
    else:
        print("Pilihan tidak valid.")