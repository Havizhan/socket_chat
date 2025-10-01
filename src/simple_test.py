#!/usr/bin/env python3
"""
Simple Socket Test - Test koneksi socket dengan debugging
"""

import socket
import sys
import time

def test_server(host='0.0.0.0', port=12345):
    """Test server - jalankan di device pertama"""
    print("=== SIMPLE SOCKET TEST - SERVER ===")
    
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((host, port))
        server.listen(1)
        
        print(f"✅ Server berjalan di {host}:{port}")
        print("⏳ Menunggu koneksi...")
        
        client, addr = server.accept()
        print(f"🔗 Koneksi diterima dari {addr}")
        
        # Test kirim pesan
        client.send(b"Hello from server!")
        print("📤 Mengirim: Hello from server!")
        
        # Test terima pesan
        msg = client.recv(1024)
        print(f"📥 Menerima: {msg.decode()}")
        
        client.close()
        server.close()
        print("✅ Test berhasil!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    return True

def test_client(host, port=12345):
    """Test client - jalankan di device kedua"""
    print("=== SIMPLE SOCKET TEST - CLIENT ===")
    
    try:
        print(f"🔍 Mencoba terhubung ke {host}:{port}...")
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(10)
        client.connect((host, port))
        
        print("✅ Terhubung ke server!")
        
        # Test terima pesan
        msg = client.recv(1024)
        print(f"📥 Menerima: {msg.decode()}")
        
        # Test kirim pesan
        client.send(b"Hello from client!")
        print("📤 Mengirim: Hello from client!")
        
        client.close()
        print("✅ Test berhasil!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    return True

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python simple_test.py server")
        print("  python simple_test.py client <IP_ADDRESS>")
        print()
        print("Contoh:")
        print("  python simple_test.py server")
        print("  python simple_test.py client 10.50.139.38")
        return
    
    mode = sys.argv[1].lower()
    
    if mode == 'server':
        test_server()
    elif mode == 'client':
        if len(sys.argv) < 3:
            print("❌ IP address diperlukan untuk client")
            print("Contoh: python simple_test.py client 10.50.139.38")
            return
        host = sys.argv[2]
        test_client(host)
    else:
        print("❌ Mode tidak valid. Gunakan 'server' atau 'client'")

if __name__ == "__main__":
    main()
