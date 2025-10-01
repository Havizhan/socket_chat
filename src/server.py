"""
===========================================
SERVER.PY - Socket Communication Server
===========================================
Simpan file ini sebagai: server.py
Jalankan dengan: python server.py
===========================================
"""

import socket
import threading
import sys

class ChatServer:
    def __init__(self, host='0.0.0.0', port=65432):
        self.host = host
        self.port = port
        self.server_socket = None
        self.clients = []
        self.running = False
        
    def start(self):
        """Memulai server"""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            self.running = True
            
            print("=" * 50)
            print(f"SERVER BERJALAN DI {self.host}:{self.port}")
            print("=" * 50)
            print(f"Menunggu koneksi dari client...")
            print("\nCommand:")
            print("  - Ketik 'clients' untuk melihat daftar client")
            print("  - Ketik 'quit' untuk menghentikan server\n")
            
            # Thread untuk menerima koneksi baru
            accept_thread = threading.Thread(target=self.accept_connections)
            accept_thread.daemon = True
            accept_thread.start()
            
            # Jalankan command loop di main thread
            self.command_loop()
            
        except Exception as e:
            print(f"[ERROR] Gagal memulai server: {e}")
            self.stop()
    
    def accept_connections(self):
        """Menerima koneksi dari client"""
        while self.running:
            try:
                client_socket, address = self.server_socket.accept()
                print(f"\n✅ [KONEKSI BARU] Client terhubung dari {address}")
                
                # Simpan client
                self.clients.append({
                    'socket': client_socket,
                    'address': address
                })
                
                # Buat thread untuk menangani client
                client_thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket, address)
                )
                client_thread.daemon = True
                client_thread.start()
                
            except Exception as e:
                if self.running:
                    print(f"[ERROR] Error menerima koneksi: {e}")
    
    def handle_client(self, client_socket, address):
        """Menangani komunikasi dengan client"""
        try:
            while self.running:
                # Terima data dari client
                data = client_socket.recv(1024)
                
                if not data:
                    break
                
                message = data.decode('utf-8')
                print(f"\n📨 [PESAN dari {address}] {message}")
                
                # Broadcast pesan ke semua client lain
                self.broadcast_message(f"{address}: {message}", client_socket)
                
        except Exception as e:
            print(f"[ERROR] Error dari {address}: {e}")
        finally:
            print(f"\n❌ [DISCONNECT] Client {address} terputus")
            self.remove_client(client_socket)
            client_socket.close()
    
    def broadcast_message(self, message, sender_socket):
        """Kirim pesan ke semua client kecuali pengirim"""
        for client in self.clients:
            if client['socket'] != sender_socket:
                try:
                    client['socket'].send(message.encode('utf-8'))
                except:
                    self.remove_client(client['socket'])
    
    def remove_client(self, client_socket):
        """Hapus client dari daftar"""
        self.clients = [c for c in self.clients if c['socket'] != client_socket]
    
    def command_loop(self):
        """Loop untuk command server"""
        while self.running:
            try:
                cmd = input()
                
                if cmd.lower() == 'quit':
                    self.stop()
                    break
                elif cmd.lower() == 'clients':
                    self.show_clients()
                    
            except KeyboardInterrupt:
                self.stop()
                break
    
    def show_clients(self):
        """Tampilkan daftar client yang terhubung"""
        print("\n" + "=" * 50)
        if not self.clients:
            print("❌ Tidak ada client yang terhubung")
        else:
            print(f"✅ Jumlah client terhubung: {len(self.clients)}")
            for i, client in enumerate(self.clients, 1):
                print(f"   {i}. {client['address']}")
        print("=" * 50 + "\n")
    
    def stop(self):
        """Hentikan server"""
        print("\n🛑 Menghentikan server...")
        self.running = False
        
        # Tutup semua koneksi client
        for client in self.clients:
            try:
                client['socket'].close()
            except:
                pass
        
        # Tutup server socket
        if self.server_socket:
            self.server_socket.close()
        
        print("✅ Server dihentikan")


if __name__ == "__main__":
    # Konfigurasi default
    HOST = '0.0.0.0'  # Dengarkan di semua interface
    PORT = 65432
    
    # Parse argument jika ada
    if len(sys.argv) >= 2:
        PORT = int(sys.argv[1])
    
    # Buat dan jalankan server
    server = ChatServer(HOST, PORT)
    server.start()