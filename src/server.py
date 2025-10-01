import socket
import threading

HOST = '0.0.0.0'   # bisa diakses dari semua IP
PORT = 12345

clients = []

def handle_client(client_socket, addr):
    print(f"[+] New connection from {addr}")
    while True:
        try:
            msg = client_socket.recv(1024)
            if not msg:
                break
            print(f"Message from {addr}: {msg.decode()}")

            # kirim ke semua client lain
            for c in clients:
                if c != client_socket:
                    c.send(msg)
        except:
            break

    print(f"[-] Connection closed {addr}")
    clients.remove(client_socket)
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Reuse address
    server.settimeout(1.0)  # Timeout untuk accept
    
    try:
        server.bind((HOST, PORT))
        server.listen(5)  # Max 5 pending connections
        
        print("=== Socket Chat Server ===")
        print(f"🚀 Server berjalan di {HOST}:{PORT}")
        print("📱 Client dapat terhubung menggunakan IP ini:")
        print("   - Untuk device yang sama: 127.0.0.1")
        print("   - Untuk device lain di jaringan: [IP komputer ini]")
        print("💡 Tekan Ctrl+C untuk menghentikan server\n")

        while True:
            try:
                client_sock, addr = server.accept()
                print(f"🔗 Koneksi baru dari {addr}")
                clients.append(client_sock)
                thread = threading.Thread(target=handle_client, args=(client_sock, addr))
                thread.daemon = True
                thread.start()
            except socket.timeout:
                continue  # Timeout normal, lanjut loop
            except KeyboardInterrupt:
                print("\n🛑 Server dihentikan oleh user")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
                break
                
    except OSError as e:
        if e.errno == 10048:  # Address already in use
            print(f"❌ Port {PORT} sudah digunakan!")
            print("💡 Coba ganti port atau matikan program yang menggunakan port tersebut")
        else:
            print(f"❌ Error binding: {e}")
    finally:
        # Cleanup semua client
        for client in clients:
            try:
                client.close()
            except:
                pass
        server.close()
        print("🔌 Server ditutup")

if __name__ == "__main__":
    main()
