"""
CLIENT.PY - Socket Communication Client
"""
import socket
import threading
import sys

class ChatClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = None
        self.running = False
        
    def connect(self):
        """Koneksi ke server"""
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.settimeout(10)  # Timeout 10 detik
            
            print(f"\n🔄 Mencoba koneksi ke {self.host}:{self.port}...")
            self.client_socket.connect((self.host, self.port))
            self.client_socket.settimeout(None)  # Reset timeout setelah koneksi berhasil
            self.running = True
            
            print("=" * 50)
            print(f"✅ TERHUBUNG KE SERVER {self.host}:{self.port}")
            print("=" * 50)
            print("📝 Ketik pesan dan tekan Enter untuk mengirim")
            print("🚪 Ketik 'quit' untuk keluar\n")
            
            # Thread untuk menerima pesan
            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.daemon = True
            receive_thread.start()
            
            # Kirim pesan dari main thread
            self.send_messages()
            
        except ConnectionRefusedError:
            print(f"\n❌ [ERROR] Koneksi ditolak ke {self.host}:{self.port}")
            print("💡 Pastikan:")
            print("   1. Server sudah berjalan (python server.py)")
            print("   2. IP address benar")
            print("   3. Port benar (65432)")
            print("   4. Firewall tidak memblokir")
            print("   5. Kedua device di jaringan yang sama")
        except socket.timeout:
            print(f"\n❌ [ERROR] Timeout! Tidak bisa terhubung ke {self.host}:{self.port}")
            print("💡 Cek koneksi jaringan dan pastikan server berjalan")
        except OSError as e:
            if e.errno == 10060:
                print(f"\n❌ [ERROR] Timeout! Tidak bisa terhubung ke {self.host}:{self.port}")
                print("💡 Cek koneksi jaringan dan pastikan server berjalan")
            else:
                print(f"\n❌ [ERROR] Error koneksi: {e}")
        except Exception as e:
            print(f"\n❌ [ERROR] Kesalahan koneksi: {e}")
        finally:
            self.disconnect()
    
    def receive_messages(self):
        """Terima pesan dari server"""
        while self.running:
            try:
                message = self.client_socket.recv(1024)
                
                if not message:
                    print("\n⚠️  Koneksi ke server terputus")
                    self.running = False
                    break
                
                print(f"\n📨 {message.decode('utf-8')}")
                print("Anda: ", end="", flush=True)
                
            except Exception as e:
                if self.running:
                    print(f"\n❌ [ERROR] Error menerima pesan: {e}")
                break
    
    def send_messages(self):
        """Kirim pesan ke server"""
        while self.running:
            try:
                message = input("Anda: ")
                
                if message.lower() == 'quit':
                    self.running = False
                    break
                
                if message.strip():
                    self.client_socket.send(message.encode('utf-8'))
                    
            except KeyboardInterrupt:
                print("\n🚪 Keluar...")
                self.running = False
                break
            except Exception as e:
                print(f"\n❌ [ERROR] Error mengirim pesan: {e}")
                self.running = False
                break
    
    def disconnect(self):
        """Putuskan koneksi"""
        self.running = False
        if self.client_socket:
            try:
                self.client_socket.close()
                print("\n✅ Koneksi ditutup")
            except:
                pass


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("\n" + "=" * 50)
        print("❌ PENGGUNAAN SALAH!")
        print("=" * 50)
        print("\n📖 Cara menggunakan:")
        print("   python client.py <host> <port>")
        print("\n💡 Contoh:")
        print("   python client.py 192.168.175.241 65432")
        print("=" * 50 + "\n")
        sys.exit(1)
    
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    
    client = ChatClient(HOST, PORT)
    client.connect()