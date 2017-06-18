from pwn import *
from base64 import b64encode
from base64 import b64decode

BLOCK_SIZE = 16
IV = "8whXbWqehnACf6tZ"

def get_blocks(ciphertext):
    ciphertext = [ciphertext[i:i + 2 * BLOCK_SIZE]
                  for i in range(0, len(ciphertext), 2 * BLOCK_SIZE)]
    return ciphertext

ciphertext = "eK6+EJRrtcTDgo5d8OYF2tf20dWQ4BQ1ZU0FnnpjEozGPJNVZHDFWpo9dMgEcYddEi5xGZAYLYPVx0H8dtPR4CfBbl5wmPbRFqF+1k+HBXc="
ciphertext = b64decode(ciphertext).encode('hex')
print get_blocks(ciphertext)
IV = IV.encode('hex')
ciphertext = IV + ciphertext
# --------------------------------
connection = remote("140.112.31.109", 10006)
print connection.recv()
print connection.recv()  # cipher text

plainttext = []
for block_index in range(len(get_blocks(ciphertext))-1, 0, -1):
    flag = []
    for last_byte in range(1, 17):
        success = False
        print "Byte: %d" %last_byte
        for cur_guess in range(126):
            if last_byte == 1 and cur_guess == 1:
                continue
            if(cur_guess == 0):
                flag.append(chr(cur_guess))
            else:
                flag[last_byte-1] = chr(cur_guess)
            guess_cipher = get_blocks(ciphertext)
            # print guess_cipher
            replace_byte = []
            for index in range(last_byte, 0, -1):
                if index == 1:
                    b = '{0:02x}'.format(int(guess_cipher[block_index - 1][-index * 2:], 16) ^ ord(flag[index - 1]) ^ last_byte)
                else:
                    b = '{0:02x}'.format(int(guess_cipher[block_index - 1][-index * 2: -(index-1) * 2], 16) ^ ord(flag[index - 1]) ^ last_byte)
                replace_byte.append(b)
            replace_byte = ''.join(replace_byte)
            guess_cipher[block_index - 1] = ''.join((guess_cipher[4][:-last_byte * 2], replace_byte))
            guess_cipher = ''.join(guess_cipher[:block_index+1])
            msg = b64encode(guess_cipher.decode('hex'))
            connection.sendline(msg)
            if "success" in connection.recv():
                print "Plaint text: %s" %chr(cur_guess)
                flag[last_byte-1] = chr(cur_guess)
                success = True
                break
        if not success:
            exit()
    print flag
    for word in flag:
        plainttext.append(word)
plainttext.reverse()
print ''.join(plainttext)
# --------------------------------