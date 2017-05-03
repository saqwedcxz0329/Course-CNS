from base64 import b64encode
from base64 import b64decode
from pwn import *

connection = remote("140.112.31.109", 10005)
file = open('fake.crt', 'r')

cer = []
for line in file.readlines():
    cer.append(line)

cer = b64encode(''.join(cer))
print cer
connection.sendline(cer)
print connection.recv()
print connection.recv()
print connection.recv()
print connection.recv()
print connection.recv()
print connection.recv()
print connection.recv()
print connection.recv()
print connection.recv()
print connection.recv()
print connection.recv()
print connection.recv()
print connection.recv()
print connection.recv()
print connection.recv()
print connection.recv()
print connection.recv()
print connection.recv()
print connection.recv()
print connection.recv()
