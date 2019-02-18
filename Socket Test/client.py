import socket

print("ready")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket initialized")
s.connect(("127.0.0.1", 1111))
print("socket connected to server")
print(s.getsockname)

name = "john"

s.send(name.encode())
print("socket sent")

r = s.recv(9999999)
print("socket finished")

print(r)