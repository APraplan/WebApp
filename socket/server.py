import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 5500
s.bind((host, port))

s.listen(5)
c, addr = s.accept()
print("Connection from: " + str(addr))

while True:
    recv = c.recv(1024)
    print(recv)
    
    if str(recv) == "b'exit'":
        break
    
    a = input("Server command: ")
    c.sendall(bytes(a, 'ascii'))
    
c.close()