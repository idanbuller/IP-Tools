import socket

user_input = str(input("Example: hacker.io \nEnter the domain name: "))

hostname = user_input

hostname_ip = socket.gethostbyname(hostname)

print(hostname_ip)
