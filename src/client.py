import socket
import threading

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024)
            if not msg:
                print("Server terputus")
                break
            print("\nPesan dari orang lain:", msg.decode())
        except:
            break
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_HOST, SERVER_PORT))
    print("Terhubung ke server")

    # Buat thread untuk menerima pesan
    recv_thread = threading.Thread(target=receive_messages, args=(client,))
    recv_thread.daemon = True
    recv_thread.start()

    # Looping untuk mengirim pesan
    while True:
        pesan = input()
        if pesan.lower() == 'Bye':
            break
        try:
            client.send(pesan.encode())
        except:
            print("Gagal mengirim pesan.")
            break

    client.close()

if __name__ == "__main__":
    main()

