import socket
import json

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "127.0.0.1"
PORT = 12345
bit = 262144


def set_config():
    global HOST, PORT, bit
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
            PORT = config['port']
            bit = config['bit']
    except Exception as e:
        print(e)
        print("No se pudo leer el archivo de configuración")
        exit()


if __name__ == '__main__':
    set_config()

    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    while True:
        conn, addr = server_socket.accept()
        print('Conexión entrante desde:', addr)
        
        data = conn.recv(bit)
        print('Datos recibidos:', data.decode())
        
        conn.close()
