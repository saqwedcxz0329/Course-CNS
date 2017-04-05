import hashlib
import random
import time
from pwn import *

p = 262603487816194488181258352326988232210376591996146252542919605878805005469693782312718749915099841408908446760404481236646436295067318626356598442952156854984209550714670817589388406059285064542905718710475775121565983586780136825600264380868770029680925618588391997934473191054590812256197806034618157751903

file = open("try.txt", "w")

def brute(password):
    # try:
    r = remote("140.112.31.109", 10002)
    # password = [2, 20, 5]
    key = 0
    for pwd in password:
        g = pow(pwd, 2, p)
        b = 5
        # Receive   
        recv = r.recv(timeout = 5)        # Round i
        if recv == '':
            raise Exception("Time out!!!")
        A = r.recv(timeout = 5)    # Server send: ...
        if A == '':
            raise Exception("Time out!!!")
        A = int(A[14:].split("G")[0][:-1])
        assert(514 <= A < p-514)
        K = pow(A, b, p)
        key ^= int(hashlib.sha512(str(K)).hexdigest(), 16)
        # Send
        B = pow(g, b ,p)
        r.sendline(str(B))

    recv = r.recv(timeout = 5)
    if recv == '':
        raise Exception("Time out!!!!")
    FLAG = int(recv[9:-1])

    file.write(str(password) + "\n")
    file.write(str(hex(FLAG ^ key)[2:].decode("hex")) + "\n")
    file.write("================\n")
    print password
    print hex(FLAG ^ key)[2:].decode("hex")
    print "=========\n"
    r.close()
    # except:
    #     print "Error!!! try again."
    #     r.close()
    #     brute(password)

password = [13, 19, 17]
# for i in range(2, 21):
#     for j in range(2, 21):
#         for k in range(2, 21):
password = [int(hashlib.sha512(str(pwd)).hexdigest(), 16) for pwd in password]
# password = [i, j, k]
brute(password)

file.close()