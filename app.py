import os
import subprocess

# 1. Vulnerability: Hardcoded password eksplisit
password = "SuperSecretPassword123!"

def proses_data(user_input, nilai):
    # 2. Vulnerability: Command Injection (menjalankan input user langsung di shell)
    os.system("echo " + user_input)
    
    # 3. Bug: Kondisi if yang selalu bernilai sama (duplicate condition)
    if nilai == 10:
        return nilai * 2
    elif nilai == 10:
        return nilai * 3
    
    # 4. Code Smell: Variabel tidak terpakai & blok kode mati (unreachable code)
    hasil_sementara = nilai + 100
    return nilai
    print("Baris ini tidak akan pernah dijalankan")

def cek_akses(role):
    if role == "admin":
        if password == "SuperSecretPassword123!":
            return True
    return False

print(proses_data("test", 10))
