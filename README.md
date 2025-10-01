# Socket Chat App (Server - Client)

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

</div>

Proyek sederhana **socket communication** menggunakan Python.  
Aplikasi ini mensimulasikan layanan chatting antara 2 orang/tim dengan model **server-client**.

---

## 📂 Struktur Folder

```
socket-server-client/
│
├── src/
│   ├── server.py    # Program server
│   └── client.py    # Program client
├── requirements.txt
└── README.md
```

---

## 🚀 Cara Menjalankan

### 1. Persiapan
- Pastikan sudah menginstal **Python 3.x**  
- Clone / download repo ini, lalu buka folder `src`
- Pastikan kedua device berada di jaringan yang sama (WiFi/LAN yang sama)

### 2. Jalankan Server (Device 1)
Buka terminal di komputer pertama, lalu ketik:
```bash
python server.py
```

**Output yang diharapkan:**
```
=== Socket Chat Server ===
🚀 Server berjalan di 0.0.0.0:12345
📱 Client dapat terhubung menggunakan IP ini:
   - Untuk device yang sama: 127.0.0.1
   - Untuk device lain di jaringan: [IP komputer ini]
💡 Tekan Ctrl+C untuk menghentikan server
```

### 3. Jalankan Client (Device 2)
Buka terminal di komputer kedua, lalu jalankan:
```bash
python client.py
```

**Saat diminta IP server, masukkan:**
- `127.0.0.1` (jika testing di komputer yang sama)
- `10.50.139.38` (ganti dengan IP komputer server - lihat output server)

**Jika berhasil, akan muncul:**
```
✅ Terhubung ke server!
💡 Ketik 'bye' untuk keluar
```

### 4. Mulai Chat
- Ketik pesan di client 1 → muncul di client 2
- Ketik pesan di client 2 → muncul di client 1
- Jika ingin keluar, ketik: `bye`

---

## 💡 Catatan

- Jika server & client dijalankan di komputer yang sama, gunakan `127.0.0.1`
- Jika di komputer berbeda (2 orang), gunakan IP address komputer server
- Cek IP server dengan `ipconfig` (Windows) atau `ifconfig` (Linux/Mac)
- Pastikan kedua device berada di jaringan yang sama (WiFi/LAN yang sama)

## 🔧 Troubleshooting

### Jika Tidak Bisa Terhubung:

1. **Test Koneksi:**
   ```bash
   python test_connection.py
   ```

2. **Cek Firewall:**
   ```bash
   python firewall_helper.py
   ```

3. **Pastikan Server Berjalan:**
   - Server harus dijalankan terlebih dahulu
   - Cek apakah port 12345 terbuka

4. **Cek IP Address:**
   - Pastikan IP address benar
   - Kedua device harus di jaringan yang sama

### Error Umum:
- **`[WinError 10060]`** → Server tidak berjalan atau IP salah
- **`Connection refused`** → Firewall memblokir atau server mati
- **`No route to host`** → Device tidak dalam jaringan yang sama

---

## 🎥 Demo

- Server dijalankan oleh Orang 1
- Client dijalankan oleh Orang 2  
- Chat berlangsung dua arah dan direkam dalam video untuk tugas