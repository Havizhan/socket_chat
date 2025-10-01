# Konfigurasi Socket Chat App

# Port yang digunakan untuk komunikasi
PORT = 12345

# IP Address untuk testing lokal
LOCAL_IP = '127.0.0.1'

# Contoh IP untuk jaringan lokal (ganti sesuai dengan IP komputer server)
# Contoh: '10.50.139.38', '192.168.1.100', dll
NETWORK_IP = '10.50.139.38'  # Ganti dengan IP komputer server

# Pesan bantuan
HELP_MESSAGE = """
=== Socket Chat App ===
1. Jalankan server.py di komputer pertama
2. Jalankan client.py di komputer kedua
3. Masukkan IP address server saat diminta
4. Mulai chatting!

IP yang bisa digunakan:
- 127.0.0.1 (untuk testing di komputer yang sama)
- {network_ip} (untuk koneksi antar device)
""".format(network_ip=NETWORK_IP)
