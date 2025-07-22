import socket

HOST = '127.0.0.1'  # Or '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Send initial greeting
client_socket.sendall(b'Hello from client!')
data = client_socket.recv(1024)
print(f"🤖 Server: {data.decode()}")

while True:
    message = input("📝 Your message (type 'quit' to exit): ")

    client_socket.sendall(message.encode())

    data = client_socket.recv(1024)
    print(f"📬 Server: {data.decode()}")

    if message.lower() == "quit":
        print("👋 Exiting.")
        break

client_socket.close()