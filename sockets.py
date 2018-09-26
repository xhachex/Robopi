import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
request = "GET / HTTP/1.1\nHost: "+"pythonprogramming.net"+"\n\n"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("pythonprogramming.net", 80))
s.send(request.encode())
result = s.recv(4096)

print(result)
