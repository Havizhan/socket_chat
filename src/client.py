import socket
import threading

# Konfigurasi server
SERVER_PORT = 12345

# Input IP address server
print("=== Socket Chat Client ===")
print("Masukkan IP address server:")
print("Contoh: 10.50.139.38 (untuk koneksi lokal)")
print("Atau: 127.0.0.1 (untuk testing di komputer yang sama)")
SERVER_HOST = input("IP Server: ").strip()

if not SERVER_HOST:
    SERVER_HOST = '127.0.0.1'  # default untuk testing lokal
    print(f"Menggunakan IP default: {SERVER_HOST}")

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024)
            if not msg:
                break
            print("\nPesan dari orang lain:", msg.decode())
        except:
            break

def main():
    try:
        print(f"\nMencoba terhubung ke {SERVER_HOST}:{SERVER_PORT}...")
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((SERVER_HOST, SERVER_PORT))
        print("✅ Terhubung ke server!")
        print("💡 Ketik 'bye' untuk keluar\n")

        # thread khusus buat nerima pesan
        thread = threading.Thread(target=receive_messages, args=(client,))
        thread.daemon = True
        thread.start()

        # kirim pesan
        while True:
            pesan = input("Pesan Anda: ")
            if pesan.lower() == 'bye':
                print("👋 Keluar dari chat...")
                break
            client.send(pesan.encode())

    except ConnectionRefusedError:
        print(f"❌ Tidak bisa terhubung ke {SERVER_HOST}:{SERVER_PORT}")
        print("Pastikan server sudah berjalan dan IP address benar!")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        try:
            client.close()
        except:
            pass

if __name__ == "__main__":
    main()
