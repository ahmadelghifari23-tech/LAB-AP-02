import re


def validasi_nim(nim):
	return re.fullmatch(r"H071\d{6}", nim) is not None


def validasi_email(email):
	pola_email = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"
	return re.fullmatch(pola_email, email) is not None


def validasi_telepon(telepon):
	return re.fullmatch(r"\d{10,13}", telepon) is not None


print("=== Validasi Data Mahasiswa ===")
nim = input("\nMasukkan NIM     : ").strip()
email = input("Masukkan Email   : ").strip()
telepon = input("Masukkan No. Telp : ").strip()

nim_valid = validasi_nim(nim)
email_valid = validasi_email(email)
telepon_valid = validasi_telepon(telepon)

print("\n--- Hasil Validasi ---")
print(f"NIM          : {'Valid' if nim_valid else 'Tidak valid'}")
print(f"Email        : {'Valid' if email_valid else 'Tidak valid'}")
print(f"No. Telepon  : {'Valid' if telepon_valid else 'Tidak valid'}")

if not nim_valid:
	print("Format NIM tidak valid!")
if not email_valid:
	print("Format email tidak valid!")
if not telepon_valid:
	print("Nomor telepon tidak valid!")

if nim_valid and email_valid and telepon_valid:
	print("\nData mahasiswa berhasil diverifikasi!")
