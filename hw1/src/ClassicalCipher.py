from pwn import *

r = remote("140.112.31.109", 10000)
r.recv()
msg = r.recv()
print msg
msg = msg.split("\n")
m1 = msg[0].split("=")[1][1:]
c1 = msg[1].split("=")[1][1:]
c2 = msg[3].split("=")[1][1:]
print m1[0]
print c1[0]
print abs(ord(m1[0]) - ord(c1[0])) % 26
print c2
#r.sendline("121233")
#print r.recv()
