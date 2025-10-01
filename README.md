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
python run_server.py
# atau: python server.py
```

**Output yang diharapkan:**
```
==================================================
SERVER BERJALAN DI 0.0.0.0:65432
==================================================
Menunggu koneksi dari client...
```

### 3. Jalankan Client (Device 2)
Buka terminal di komputer kedua, lalu jalankan:
```bash
python run_client.py
# atau: python client.py <IP_SERVER> <PORT>
```

**Saat diminta IP server, masukkan:**
- IP address komputer server (dari `ipconfig`)

**Jika berhasil, akan muncul:**
```
✅ TERHUBUNG KE SERVER 192.168.175.142:65432
```

### 4. Mulai Chat
- Ketik pesan di client 1 → muncul di client 2
- Ketik pesan di client 2 → muncul di client 1
- Jika ingin keluar, ketik: `quit`

---

## 💡 Catatan

- Jika server & client dijalankan di komputer yang sama, gunakan `127.0.0.1`
- Jika di komputer berbeda (2 orang), gunakan IP address komputer server
- Cek IP server dengan `ipconfig` (Windows) atau `ifconfig` (Linux/Mac)
- Pastikan kedua device berada di jaringan yang sama (WiFi/LAN yang sama)

## 🔧 Troubleshooting

### Jika Tidak Bisa Terhubung:

1. **Debug Koneksi:**
   ```bash
   python debug_connection.py <IP_SERVER> <PORT>
   # Contoh: python debug_connection.py 192.168.175.142 65432
   ```

2. **Jalankan Server dengan Mudah:**
   ```bash
   python run_server.py
   # atau dengan port custom: python run_server.py 65432
   ```

3. **Jalankan Client dengan Mudah:**
   ```bash
   python run_client.py
   # atau: python run_client.py <IP_SERVER> <PORT>
   ```

4. **Pastikan Server Berjalan:**
   - Server harus dijalankan terlebih dahulu
   - Cek apakah port 65432 terbuka

5. **Cek IP Address:**
   - Pastikan IP address benar
   - Kedua device harus di jaringan yang sama

### Error Umum:
- **`ConnectionRefusedError`** → Server tidak berjalan atau IP salah
- **`[WinError 10060]`** → Timeout, cek koneksi jaringan
- **`No route to host`** → Device tidak dalam jaringan yang sama

### Langkah Debugging:
1. Jalankan `python debug_connection.py` untuk test koneksi
2. Pastikan server berjalan di device pertama
3. Cek IP address dengan `ipconfig` (Windows) atau `ifconfig` (Mac/Linux)
4. Pastikan firewall tidak memblokir port 65432

---

## 🎥 Demo

- Server dijalankan oleh Orang 1
- Client dijalankan oleh Orang 2  
- Chat berlangsung dua arah dan direkam dalam video untuk tugas