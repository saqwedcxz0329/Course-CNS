from pwn import *
from base64 import b64encode
from base64 import b64decode
from binascii import hexlify, unhexlify


BLOCK_SIZE = 16

def get_blocks(message, ciphertext):
    while len(message) % BLOCK_SIZE:
        message += "_"
    message = [message[i:i + BLOCK_SIZE]
               for i in range(0, len(message), BLOCK_SIZE)]

    ciphertext = [ciphertext[i:i + 2 * BLOCK_SIZE]
                  for i in range(0, len(ciphertext), 2 * BLOCK_SIZE)]
    return message, ciphertext

def register(username, pwd):
    connection = remote("140.112.31.109", 10004)
    connection.recv()
    connection.sendline('0')
    connection.recv()
    connection.sendline(username)
    connection.recv()
    connection.sendline(pwd)
    return connection.recv().strip().split(' ')[3]

def login(token, username, pwd):
    connection = remote("140.112.31.109", 10004)
    connection.recv()
    connection.sendline('1')
    connection.recv()
    connection.sendline(token)
    connection.recv()
    connection.sendline(username)
    connection.recv()
    connection.sendline(pwd)
    return connection.recv()


if __name__ == '__main__':
    username = 'aaaaaaaaaaaaaaaaaaaa'
    pwd = 'bbbbbbbbbbbb'
    m1 = 'login=%s&role=user&pwd=b' %username
    m2 = 'login=aaaaaaaaaaadmin&role=user&pwd=%s' %pwd
    token_1 = register(username, 'b')
    token_1 = b64decode(token_1).encode('hex')
    m1, token_1 = get_blocks(m1, token_1)

    token_2 = register('aaaaaaaaaaadmin', pwd)
    token_2 = b64decode(token_2).encode('hex')
    m2, token_2 = get_blocks(m2, token_2)
    token = [token_1[0], token_1[1]]
    for i in token_2[1:]:
        token.append(i)

    token =  ''.join(token)
    token =  b64encode(token.decode("hex"))
    print login(token, username, pwd)