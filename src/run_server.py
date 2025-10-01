#!/usr/bin/env python3
"""
RUN SERVER - Script untuk menjalankan server dengan mudah
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from server import ChatServer

def main():
    print("=" * 60)
    print("🚀 SOCKET CHAT SERVER")
    print("=" * 60)
    
    # Konfigurasi default
    HOST = '0.0.0.0'
    PORT = 65432
    
    # Parse argument jika ada
    if len(sys.argv) >= 2:
        PORT = int(sys.argv[1])
    
    print(f"📍 Server akan berjalan di {HOST}:{PORT}")
    print("💡 Tekan Ctrl+C untuk menghentikan server")
    print("=" * 60)
    
    try:
        # Buat dan jalankan server
        server = ChatServer(HOST, PORT)
        server.start()
    except KeyboardInterrupt:
        print("\n🛑 Server dihentikan oleh user")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
