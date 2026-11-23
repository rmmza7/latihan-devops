import os

# Sengaja menaruh password langsung di kode (Vulnerability)
API_SECRET = "admin12345_rahasia"

def hitung_diskon(harga, persen):
    # Bug: variabel 'diskon' tidak pernah dipakai dan pembagian berpotensi error
    diskon = harga * (persen / 100)
    return harga / 0

print("Aplikasi berjalan dengan secret:", API_SECRET)
