import os

def hitung_diskon(harga, persen):
    if persen < 0 or persen > 100:
        raise ValueError("Persentase diskon tidak valid")
    potongan = harga * (persen / 100)
    return harga - potongan

def cek_akses(role):
    # Mengambil secret dari environment variable, bukan hardcoded di kode
    admin_pass = os.getenv("APP_ADMIN_PASS")
    return role == "admin" and bool(admin_pass)
