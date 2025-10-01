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
    server.bind((HOST, PORT))
    server.listen()
    
    print("=== Socket Chat Server ===")
    print(f"🚀 Server berjalan di {HOST}:{PORT}")
    print("📱 Client dapat terhubung menggunakan IP ini:")
    print("   - Untuk device yang sama: 127.0.0.1")
    print("   - Untuk device lain di jaringan: [IP komputer ini]")
    print("💡 Tekan Ctrl+C untuk menghentikan server\n")

    while True:
        try:
            client_sock, addr = server.accept()
            clients.append(client_sock)
            thread = threading.Thread(target=handle_client, args=(client_sock, addr))
            thread.start()
        except KeyboardInterrupt:
            print("\n🛑 Server dihentikan oleh user")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            break
    
    server.close()

if __name__ == "__main__":
    main()
