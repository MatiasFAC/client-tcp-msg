import socket
import json
import sys
import chardet

HOST = '127.0.0.1'
PORT = 12345
message = ''
input_file = ''
bit = 262144


def read_parameters():
    global input_file
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        print("Ingresa la ruta del archivo de texto")
        exit()


def set_config():
    global HOST, PORT, bit
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
            HOST = config['host']
            PORT = config['port']
            bit = config['bit']
    except Exception as e:
        print(e)
        print("No se pudo leer el archivo de configuración")
        exit()


def read_file():
    global message
    try:
        with open(input_file, 'rb') as f:
            result = chardet.detect(f.read())
        # print(f"encoding: {result}")
        with open(input_file, 'r', encoding=result['encoding']) as f:
            message = f.read()
    except Exception as e:
        print(e)
        print("No se pudo leer el archivo de texto")
        exit()


def send_msg_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(message.encode())
        data = s.recv(bit)
    if len(data.decode()) > 0:
        print('Respuesta del servidor:')
        print(data.decode())


if __name__ == '__main__':
    read_parameters()
    set_config()
    read_file()
    print('Host:', HOST)
    print('Port:', PORT)
    print('File:', input_file)
    print('Mensaje a enviar:')
    print(message)
    send_msg_server()
