import hashlib
import random
from pwn import *

def alarm(time):
    def handler(signum, frame):
        print 'You need to be faster'
        exit()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(time)

def sha1(content):
    Hash=hashlib.sha1()
    Hash.update(content)
    return Hash.digest()

P = "25 50 44 46 2d 31 2e 33 0a 25 e2 e3 cf d3 0a 0a 0a 31 20 30 20 6f 62 6a 0a 3c 3c 2f 57 69 64 74 68 20 32 20 30 20 52 2f 48 65 69 67 68 74 20 33 20 30 20 52 2f 54 79 70 65 20 34 20 30 20 52 2f 53 75 62 74 79 70 65 20 35 20 30 20 52 2f 46 696c 74 65 72 20 36 20 30 20 52 2f 43 6f 6c 6f 72 53 70 61 63 65 20 37 20 30 20 52 2f 4c 65 6e 67 74 68 20 38 20 30 20 52 2f 42 69 74 73 50 65 72 43 6f 6d 70 6f 6e 65 6e 74 20 38 3e 3e 0a 73 74 72 65 61 6d 0a ff d8 ff fe 00 24 53 48 41 2d 31 20 69 73 20 64 65 61 64 21 21 21 21 21 85 2f ec 09 23 39 75 9c 39 b1 a1 c6 3c 4c 97 e1 ff fe 01"
P = ''.join(P.split(' '))
M11 = "7f 46 dc 93 a6 b6 7e 01 3b 02 9a aa 1d b2 56 0b 45 ca 67 d6 88 c7 f8 4b 8c 4c 79 1f e0 2b 3d f6 14 f8 6d b1 69 09 01 c5 6b 45 c1 53 0a fe df b7 60 38 e9 72 72 2f e7 ad 72 8f 0e 49 04 e0 46 c2"
M11 = ''.join(M11.split(' '))
M12 = "30 57 0f e9 d4 13 98 ab e1 2e f5 bc 94 2b e3 35 42 a4 80 2d 98 b5 d7 0f 2a 33 2e c3 7f ac 35 14 e7 4d dc 0f 2c c1 a8 74 cd 0c 78 30 5a 21 56 64 61 30 97 89 60 6b d0 bf 3f 98 cd a8 04 46 29 a1"
M12 = ''.join(M12.split(' '))
M21 = "73 46 dc 91 66 b6 7e 11 8f 02 9a b6 21 b2 56 0f f9 ca 67 cc a8 c7 f8 5b a8 4c 79 03 0c 2b 3d e2 18 f8 6d b3 a9 09 01 d5 df 45 c1 4f 26 fe df b3 dc 38 e9 6a c2 2f e7 bd 72 8f 0e 45 bc e0 46 d2"
M21 = ''.join(M21.split(' '))
M22 = "3c 57 0f eb 14 13 98 bb 55 2e f5 a0 a8 2b e3 31 fe a4 80 37 b8 b5 d7 1f 0e 33 2e df 93 ac 35 00 eb 4d dc 0d ec c1 a8 64 79 0c 78 2c 76 21 56 60 dd 30 97 91 d0 6b d0 af 3f 98 cd a4 bc 46 29 b1"
M22 = ''.join(M22.split(' '))

pre_traversal = {}
try:
    file = open("hex.txt", "r")
    for line in file.readlines():
        line = line.strip().split(" ")
        pre_traversal[line[1]] = line[0]
        times = int(line[0]) + 1
    file.close()
except:
    times = 0
file = open("hex.txt", "a")

target = "1859d1"
M1 = None
M2 = None
if target in pre_traversal:
    S = hex(int(pre_traversal[target]))[2:]
    if len(S) % 2 == 1:
        S = '0' + S
    M1 = P + M11 + M12 + S
    M2 = P + M21 + M22 + S
else:
    try:
        S = hex(times)[2:]
        if len(S) % 2 == 1:
            S = '0' + S
        M1 = P + M11 + M12 + S
        while True:
            print "===%s===" %S
            file.write("%s %s\n" %(times, sha1(M1.decode("hex")).encode("hex")[-6:]))
            print sha1(M1.decode("hex")).encode("hex")[-6:]
            if sha1(M1.decode("hex")).encode("hex")[-6:]==target:
                break
            randomstring = hex(random.randint(0,16777216))[2:]
            times += 1
            S = hex(times)[2:]
            if len(S) % 2 == 1:
                S = '0' + S
            M1 = P + M11 + M12 + S
        M2 = P + M21 + M22 + S
    except KeyboardInterrupt:
        file.write("%s %s\n" %(times, sha1(M1.decode("hex")).encode("hex")[-6:]))
        
if M2 is not None:
    print "M1: " + M1
    print "M2: " + M2
file.close()