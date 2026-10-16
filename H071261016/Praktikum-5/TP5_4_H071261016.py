DAFTAR_EMAIL_VALID = []

def deteksi_anomali_email(email):
    anomali = []

    if email.count("@") != 1:
        anomali.append("Harus memiliki tepat satu karakter @.")
        return anomali  

    local, domain = email.split("@")

    if not local or not domain:
        anomali.append(
            "Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong."
        )

    if any(karakter.isspace() for karakter in email):
        anomali.append("Email tidak boleh mengandung spasi.")

    if local and (
        local.startswith(".") or local.endswith(".") or ".." in local
    ):
        anomali.append(
            "Bagian local tidak boleh diawali atau diakhiri titik, "
            "serta tidak boleh mengandung titik berurutan."
        )

    if domain:
        if "." not in domain:
            anomali.append("Bagian domain wajib memiliki minimal satu titik.")
        if domain.startswith(".") or ".." in domain or domain.endswith("."):
            anomali.append(
                "Bagian domain tidak boleh diawali dan diakhiri titik atau mengandung titik berurutan."
            )

    if not email.lower().endswith((".com", ".id", ".ac.id")):
        anomali.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    if any(email.lower() == terdaftar.lower() for terdaftar in DAFTAR_EMAIL_VALID):
        anomali.append("Email sudah terdaftar (Duplikat).")

    return anomali


def cetak_daftar(daftar_email_valid, karakter_border):
    daftar = daftar_email_valid or [""]
    lebar = max(len(email) for email in daftar) + 2
    border = karakter_border * lebar
    baris = [border]
    baris.extend(" " + email.ljust(lebar - 1) for email in daftar)
    baris.append(border)
    return "\n".join(baris)


def main():
    print("Sistem Pencatatan Email Valid")
    karakter_border = input("Masukkan border dengan karakter bebas: ") or "-"
    print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

    while True:
        email = input("Masukkan email: ")
        if email.lower() == "tutup":
            break

        anomali = deteksi_anomali_email(email)
        if anomali:
            print(">> Email DITOLAK karena:")
            for aturan in anomali:
                print(f"    - {aturan}")
            print()
        else:
            DAFTAR_EMAIL_VALID.append(email)
            print(">> Email VALID!")

    print("-- HASIL EMAIL VALID --")
    print(cetak_daftar(DAFTAR_EMAIL_VALID, karakter_border))


main()