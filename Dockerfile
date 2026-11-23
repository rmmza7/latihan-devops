# 1. Gunakan base image Python resmi yang ringan (slim)
FROM python:3.11-slim

# 2. Tentukan direktori kerja di dalam container
WORKDIR /app

# 3. Salin file aplikasi dari laptop ke dalam image
COPY app.py test_app.py ./

# 4. Buat user non-root demi keamanan produksi
RUN useradd -m appuser
USER appuser

# 5. Perintah default saat container dijalankan
CMD ["python3", "-m", "unittest", "test_app.py"]
