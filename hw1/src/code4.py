from pwn import *
import base64

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

def get_offset_list(key_legth, msg):
    offset_list = []
    # print len(msg)
    for i in range(key_legth):
        offset_list.append(len(msg) / key_legth)
    for i in range(len(msg) % key_legth):
        offset_list[i] = offset_list[i] + 1
    return offset_list

def decrypto(ciphertext, offset_list):
    cipher_len = len(ciphertext)
    index = 0
    plaintext = [ciphertext[index]]
    while len(plaintext) < cipher_len:
        for offset in offset_list:
            index = index + offset
            if index >= cipher_len:
                index = (index % cipher_len) + 1
            plaintext.append(ciphertext[index])
            if len(plaintext) >= cipher_len:
                break
    plaintext = ''.join(plaintext)
    return plaintext

def round1(connection):
    connection.recv()
    msg = connection.recv()
    print msg
    msg = msg.split("\n")
    m1 = msg[0].split("=")[1][1:]
    c1 = msg[1].split("=")[1][1:]
    c2 = msg[3].split("=")[1][1:]
    offset = (ord(c1[0]) - ord(m1[0])) % 26
    m2 = decode(c2, offset)
    print "offset: " + str(offset)
    print m2 + "\n"
    connection.sendline(m2)

def round2(connection):
    print connection.recv()
    msg = connection.recv()
    print msg
    msg = msg.split("\n")
    c1 = msg[0].split("=")[1][1:]
    for i in range(1, 26):
        m1 = decode(c1, i)
        print m1

    m1 = raw_input("Enter your answer: ")
    connection.send(m1)

def round3(connection):
    print connection.recv()
    msg =  connection.recv()
    print msg
    msg = msg.split("\n")
    m1 = msg[0].split("=")[1][1:]
    c1 = msg[1].split("=")[1][1:]
    c2 = msg[3].split("=")[1][1:]

    offset = (ord(c1[0]) - ord(m1[0])) % 26
    m2 = ""
    for index , character in enumerate(c2):
        cur_offset  =  (offset + index) % 26
        m2 += decode(character, cur_offset)
    connection.sendline(m2)

def round4(connection):
    print connection.recv()
    msg =  connection.recv()
    print msg
    msg = msg.split("\n")
    m1 = msg[0].split("=")[1][1:]
    c1 = msg[1].split("=")[1][1:]
    c2 = msg[3].split("=")[1][1:]

    offset_list = []
    for index, character in enumerate(m1):
        if character == " ":
            continue
        offset = ord(c1[index]) - ord(m1[index])
        print offset % 26,
    print ""

    offset_list_string = raw_input("Enter offset list: ")
    for i in offset_list_string.split(" "):
        print i
        if i == '\n':
            break
        offset_list.append(int(i))
    print offset_list

    m2 = ""
    offset_index = 0
    for index , character in enumerate(c2):
        offset_index = offset_index % len(offset_list)
        m2 += decode(character, offset_list[offset_index])
        if character == " ":
            continue
        offset_index += 1
    connection.sendline(m2)

def round5(connection):
    print connection.recv()
    msg =  connection.recv()
    print msg
    msg = msg.split("\n")
    m1 = msg[0].split("=")[1][1:]
    c1 = msg[1].split("=")[1][1:]
    c2 = msg[3].split("=")[1][1:]

    m2 = []
    for character in m1:
        m2.append(c2[c1.find(character)])

    m2 = ''.join(m2)
    connection.sendline(m2)

def round6(connection):
    print connection.recv()
    msg =  connection.recv()
    print msg
    msg = msg.split("\n")
    m1 = msg[0].split("=")[1][1:]
    c1 = msg[1].split("=")[1][1:]
    c2 = msg[3].split("=")[1][1:]

    # target_cipher_len = len(c1)
    key_legth = 2
    while True:
        ori_offset_list = get_offset_list(key_legth, c1)
        plaintext = decrypto(c1, ori_offset_list)
        if plaintext == m1:
            break
        key_legth += 1
    print key_legth

    target_offset_list = get_offset_list(key_legth, c2)
    print target_offset_list
    m2 = decrypto(c2, target_offset_list)
    connection.sendline(m2)

def round7(connection):
    print connection.recv()
    print "====="
    msg = connection.recv()
    print msg
    msg = msg.split("\n")
    c1 = msg[0].split(" ")[2]
    print c1
    m1 = base64.b64decode(c1)
    connection.sendline(m1)


connection = remote("140.112.31.109", 10000)
## Round 1
round1(connection)
## Round 2
round2(connection)
## Round 3
round3(connection)
## Round 4
round4(connection)
## Round 5
round5(connection)
round6(connection)
round7(connection)
print connection.recv()
