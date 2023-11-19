import socket

s = socket.socket()

host = socket.gethostname()
port = 5500

s.connect((host, port))
while True:
    a = input("Client command: ")    
    s.sendall(bytes(a, 'ascii'))
    
    if a == "exit":
        break
    
    recv = s.recv(1024)
    print(str(recv))
    
s.close()