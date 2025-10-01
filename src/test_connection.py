import socket
import subprocess
import platform

def get_local_ip():
    """Mendapatkan IP address lokal"""
    try:
        # Membuat koneksi dummy untuk mendapatkan IP lokal
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "Tidak bisa mendapatkan IP"

def test_port(host, port):
    """Test apakah port terbuka"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)  # Timeout 5 detik
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except:
        return False

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

def main():
    print("=== Socket Connection Tester ===")
    print()
    
    # 1. Cek IP lokal
    local_ip = get_local_ip()
    print(f"📍 IP Address lokal: {local_ip}")
    print()
    
    # 2. Input IP target
    target_ip = input("Masukkan IP address target: ").strip()
    if not target_ip:
        print("❌ IP address tidak boleh kosong!")
        return
    
    port = 12345
    
    print(f"\n🔍 Testing koneksi ke {target_ip}:{port}...")
    print()
    
    # 3. Test ping
    print("1. Testing ping...")
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
    print("2. Testing port 12345...")
    if test_port(target_ip, port):
        print("✅ Port 12345 terbuka - Server berjalan")
    else:
        print("❌ Port 12345 tertutup - Server tidak berjalan")
        print("   Pastikan:")
        print("   - Server sudah dijalankan di device target")
        print("   - Firewall tidak memblokir port 12345")
        print("   - Antivirus tidak memblokir koneksi")
        return
    
    print()
    print("🎉 Semua test berhasil! Koneksi seharusnya bisa dilakukan.")
    print(f"💡 Gunakan IP: {target_ip} di client.py")

if __name__ == "__main__":
    main()
