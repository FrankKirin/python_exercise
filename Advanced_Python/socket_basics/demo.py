import socket
# AF_INET refer to the address family ipv4
# SOCK_STREAM means connection oriented TCP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to a server:
# if any error occurs during the creation of a socket than a socket.error is thrown and we
# can only connect to a server by knowing it's ip
ip = socket.gethostbyname('www.baidu.com')
print('IP address is', ip)