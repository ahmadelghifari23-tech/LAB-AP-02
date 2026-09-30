menu = ["kopi susu", "matcha latte", "americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

sub_kopi_susu = harga[0] * jumlah[0]
sub_matcha_latte = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]

subtotal_pendapatan = sub_kopi_susu + sub_americano + sub_matcha_latte
BIAYA_OPERASIONAL = 15000
pendapatan_bersih = subtotal_pendapatan - BIAYA_OPERASIONAL
jumlah_barang = sum(jumlah)
target_tercapai = subtotal_pendapatan > 200000 and jumlah_barang > 10

print("subtotal pendapatan:",subtotal_pendapatan)
print("pendapatan bersih:",pendapatan_bersih)
print("target_tercapai:",target_tercapai)
