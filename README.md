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

### 2. Jalankan Server
Buka terminal 1, lalu ketik:
```bash
python server.py
```

**Output yang diharapkan:**
```
Server berjalan di 0.0.0.0:12345
```

### 3. Jalankan Client
Buka terminal lain (atau komputer lain), lalu jalankan:
```bash
python client.py
```

**Jika berhasil, akan muncul:**
```
Terhubung ke server
```

### 4. Mulai Chat
- Ketik pesan di client 1 → muncul di client 2
- Ketik pesan di client 2 → muncul di client 1
- Jika ingin keluar, ketik: `bye`

---

## 💡 Catatan

- Jika server & client dijalankan di komputer yang sama, gunakan `SERVER_HOST = '127.0.0.1'`
- Jika di komputer berbeda (2 orang), ganti `SERVER_HOST` di `client.py` dengan alamat IP komputer server
- Cek IP server dengan `ipconfig` (Windows) atau `ifconfig` (Linux/Mac)

**Contoh:**
```python
SERVER_HOST = '192.168.1.10'
SERVER_PORT = 12345
```

- Pastikan firewall tidak memblokir Python

---

## 🎥 Demo

- Server dijalankan oleh Orang 1
- Client dijalankan oleh Orang 2  
- Chat berlangsung dua arah dan direkam dalam video untuk tugas