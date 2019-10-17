from os import environ
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
environ['ipaddr'] = s.getsockname()[0]
print(environ.get('ipaddr'))
s.close()


print(environ['ipaddr'])
