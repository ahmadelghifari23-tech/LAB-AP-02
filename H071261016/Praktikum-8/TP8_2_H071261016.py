import re


def validasi_username(username):
	return re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{4,11}", username) is not None


username_valid = []

print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.")
print()

while True:
	username = input("Masukkan username: ")

	if username.lower() == "selesai":
		break

	if validasi_username(username):
		print("Username tersedia.")
		username_valid.append(username)
	else:
		print("Username tidak valid!")
	print()

print("=== Rekapitulasi ===")
print("Username valid:")
nomor = 1
for username in username_valid:
    print(f"{nomor}. {username}")
    nomor += 1 

print(f"\nJumlah username valid: {len(username_valid)}")
