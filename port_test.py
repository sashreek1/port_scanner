import socket

for port in range(1, 65536):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.25)
    result = sock.connect_ex(("192.168.1.1", port))
    if 0 == result:
        print("Port: {} Open".format(port))
    sock.close()
