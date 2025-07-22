import socket

HOST = '127.0.0.1'  # Or '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"🟢 Server listening on {HOST}:{PORT}")

conn, addr = server_socket.accept()
print(f"✅ Connected by {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        print("🔌 Client disconnected.")
        break

    message = data.decode()
    print(f"📨 Received: {message}")

    if message.lower() == "quit":
        conn.sendall(b"Goodbye!")
        break
    else:
        conn.sendall(f"Received your message: {message}".encode())

conn.close()
server_socket.close()