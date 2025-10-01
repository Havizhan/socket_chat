#!/usr/bin/env python3
"""
DEBUG CONNECTION - Script untuk debug koneksi socket
"""

import socket
import sys
import subprocess
import platform

def get_local_ip():
    """Dapatkan IP address lokal"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "Tidak bisa mendapatkan IP"

def ping_host(host):
    """Ping host untuk test konektivitas"""
    try:
        if platform.system().lower() == "windows":
            result = subprocess.run(['ping', '-n', '1', host], 
                                  capture_output=True, text=True, timeout=10)
        else:
            result = subprocess.run(['ping', '-c', '1', host], 
                                  capture_output=True, text=True, timeout=10)
        return result.returncode == 0
    except:
        return False

def test_port(host, port):
    """Test apakah port terbuka"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except:
        return False

def main():
    print("=" * 60)
    print("🔍 DEBUG CONNECTION - Socket Chat App")
    print("=" * 60)
    
    # 1. Cek IP lokal
    local_ip = get_local_ip()
    print(f"📍 IP Address lokal: {local_ip}")
    print()
    
    # 2. Input target
    if len(sys.argv) >= 3:
        target_ip = sys.argv[1]
        target_port = int(sys.argv[2])
    else:
        target_ip = input("Masukkan IP address target: ").strip()
        if not target_ip:
            print("❌ IP address tidak boleh kosong!")
            return
        target_port = int(input("Masukkan port (default 65432): ").strip() or "65432")
    
    print(f"\n🎯 Target: {target_ip}:{target_port}")
    print()
    
    # 3. Test ping
    print("1️⃣ Testing ping...")
    if ping_host(target_ip):
        print("✅ Ping berhasil - Host dapat dijangkau")
    else:
        print("❌ Ping gagal - Host tidak dapat dijangkau")
        print("   Kemungkinan:")
        print("   - IP address salah")
        print("   - Device tidak dalam jaringan yang sama")
        print("   - Device mati/offline")
        return
    
    print()
    
    # 4. Test port
    print("2️⃣ Testing port...")
    if test_port(target_ip, target_port):
        print(f"✅ Port {target_port} terbuka - Server berjalan")
    else:
        print(f"❌ Port {target_port} tertutup - Server tidak berjalan")
        print("   Pastikan:")
        print("   - Server sudah dijalankan di device target")
        print("   - Firewall tidak memblokir port")
        print("   - Antivirus tidak memblokir koneksi")
        return
    
    print()
    print("🎉 Semua test berhasil! Koneksi seharusnya bisa dilakukan.")
    print(f"💡 Gunakan: python client.py {target_ip} {target_port}")

if __name__ == "__main__":
    main()
