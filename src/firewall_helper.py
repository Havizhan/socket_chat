import subprocess
import platform
import os

def check_firewall_status():
    """Cek status Windows Firewall"""
    try:
        if platform.system().lower() == "windows":
            result = subprocess.run(['netsh', 'advfirewall', 'show', 'allprofiles', 'state'], 
                                  capture_output=True, text=True)
            return result.stdout
        else:
            return "Firewall check hanya untuk Windows"
    except:
        return "Tidak bisa cek firewall"

def add_firewall_rule():
    """Menambahkan rule firewall untuk Python"""
    try:
        if platform.system().lower() == "windows":
            # Menambahkan rule untuk Python
            python_path = os.path.join(os.path.dirname(os.__file__), 'python.exe')
            
            commands = [
                ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 
                 'name=Python Socket Server', 'dir=in', 'action=allow', 
                 'protocol=TCP', 'localport=12345'],
                ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 
                 'name=Python Socket Client', 'dir=out', 'action=allow', 
                 'protocol=TCP', 'remoteport=12345']
            ]
            
            for cmd in commands:
                result = subprocess.run(cmd, capture_output=True, text=True)
                if result.returncode == 0:
                    print(f"✅ {cmd[5]} berhasil ditambahkan")
                else:
                    print(f"❌ Gagal menambahkan {cmd[5]}: {result.stderr}")
        else:
            print("Firewall helper hanya untuk Windows")
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    print("=== Firewall Helper ===")
    print()
    
    print("1. Status Firewall:")
    print(check_firewall_status())
    print()
    
    print("2. Menambahkan rule firewall untuk Python...")
    add_firewall_rule()
    print()
    
    print("💡 Jika masih bermasalah:")
    print("   - Matikan Windows Firewall sementara untuk testing")
    print("   - Matikan antivirus sementara")
    print("   - Pastikan kedua device di jaringan yang sama")

if __name__ == "__main__":
    main()
