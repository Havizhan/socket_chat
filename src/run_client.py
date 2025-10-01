#!/usr/bin/env python3
"""
RUN CLIENT - Script untuk menjalankan client dengan mudah
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from client import ChatClient

def main():
    print("=" * 60)
    print("📱 SOCKET CHAT CLIENT")
    print("=" * 60)
    
    # Input IP dan port
    if len(sys.argv) >= 3:
        host = sys.argv[1]
        port = int(sys.argv[2])
    else:
        print("Masukkan informasi server:")
        host = input("IP Server: ").strip()
        if not host:
            print("❌ IP address tidak boleh kosong!")
            return
        
        port_input = input("Port (default 65432): ").strip()
        port = int(port_input) if port_input else 65432
    
    print(f"🎯 Target: {host}:{port}")
    print("=" * 60)
    
    try:
        # Buat dan koneksi client
        client = ChatClient(host, port)
        client.connect()
    except KeyboardInterrupt:
        print("\n🚪 Client dihentikan oleh user")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
