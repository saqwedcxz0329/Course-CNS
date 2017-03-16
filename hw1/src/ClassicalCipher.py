from pwn import *

lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
capital_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def decode(cipher, offset):
    decode_msg = ""
    for character in cipher:
        ascii_code = ord(character)
        append_character = ""
        if (ascii_code == 32):
            append_character = " "
        # lower case
        elif (ascii_code > 96):
            ascii_code = ascii_code - 97
            append_character = lower_alphabet[(ascii_code - offset) % 26]
        # capital case
        else:
            ascii_code = ascii_code - 65
            append_character = capital_alphabet[(ascii_code - offset) % 26]
        decode_msg += append_character
    return decode_msg

r = remote("140.112.31.109", 10000)
## Round 1
print r.recv()
msg = r.recv()
print msg
msg = msg.split("\n")
m1 = msg[0].split("=")[1][1:]
c1 = msg[1].split("=")[1][1:]
c2 = msg[3].split("=")[1][1:]
offset = ord(c1[0]) - ord(m1[0])
m2 = decode(c2, offset)
print "offset: " + str(offset)
print m2 + "\n"
r.sendline(m2)

## Round 2
print r.recv()
msg = r.recv()
print msg
msg = msg.split("\n")
c1 = msg[0].split("=")[1][1:]
for i in range(1, 26):
    m1 = decode(c1, i)
    print "offset: " + str(i)
    print m1 + "\n"
r.interactive()
#print r.recv()