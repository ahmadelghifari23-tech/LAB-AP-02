while True:
    try:
        n = int(input("Masukkan jumlah baris: "))
        if n <= 0:
            print("Jumlah baris harus lebih dari 0!")
            continue
    except ValueError:
        print("Input baris harus berupa angka!")
        continue       
    break
  
while True:
    try:
        m = int(input("Masukkan jumlah kursi per baris: "))
        if m <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue
    except ValueError:
        print("Input kursi harus berupa angka!") 
        continue   
    break

for baris in range(1, n+1):
    for kursi in range(1, m+1):
        if kursi == 13:
            continue
        elif baris == 1 and kursi % 2 == 0:
            continue
        print("Baris",baris,"- Kursi",kursi)
