# Gunakan image dasar Python yang ringan
FROM python:3.10-slim

# Tentukan direktori kerja di dalam container
WORKDIR /app

# Salin file kebutuhan ke dalam container
COPY requirements.txt .

# Instal library Python yang diperlukan
RUN pip install --default-timeout=100 --no-cache-dir -r requirements.txt

# Salin seluruh kode aplikasi ke dalam container
COPY . .

# Beritahu Docker bahwa aplikasi berjalan di port 8501
EXPOSE 8501

# Perintah untuk menjalankan Streamlit saat container dimulai
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]