alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
capital_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            
file = open("round5.csv", 'w+')

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
            append_character = alphabet[(ascii_code - offset) % 52]
        # capital case
        else:
            ascii_code = ascii_code - 65 + 26
            append_character = alphabet[(ascii_code - offset) % 52]
        decode_msg += append_character
    return decode_msg

def changerNum(ascii_code):
    if (ascii_code > 96):
        return ascii_code - 97
    else:
        return ascii_code - 65 + 26

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
    translated = [] # stores the encrypted/decrypted message string
    keyIndex = 0

    for symbol in message: # loop through each character in message
        num = LETTERS.find(symbol)
        if num != -1: # -1 means symbol.upper() was not found in LETTERS
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex]) # add if encrypting
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex]) # subtract if decrypting

            num %= len(LETTERS) # handle the potential wrap-around

            # add the encrypted/decrypted symbol to the end of translated.
            translated.append(LETTERS[num])
            # if symbol.isupper():
            #     translated.append(LETTERS[num])
            # elif symbol.islower():
            #     translated.append(LETTERS[num].lower())

            keyIndex += 1 # move to the next letter in the key
            if keyIndex == len(key):
                keyIndex = 0
        else:
            # The symbol was not in LETTERS, so add it to translated as is.
            translated.append(symbol)

    return ''.join(translated)

def printGap(plaintext, ciphertext):
    for index, character in enumerate(plaintext):
        if character == " ":
            continue
        offset = changerNum(ord(ciphertext[index])) - changerNum(ord(plaintext[index]))
        file.write(str(offset % 52) + ",")
    file.write("\n")

LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
m1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
c1 = "YpyRPBQWZgwNkonilLcISbuxzfVDOEavrsTAHtJdjehKqCGFXMmU"
c2 = "tTKDqQvjNcdFzfCXLHSPiblJagrmZhyxVEoApGeUMwWnkRuOBYIs"
c3 = "qixrFpoRTgcBLaHEuNvzAWKImOkShteGPbXCwUDfldjQMsyJZVYn"
c4 = "GKuesHdfDYJOogWrEcyvNXiQwZatAPIVnBmTjMFULhpqxbSClRzk"
# c2 = "  orh evat i ylxo pcsicSmralpacktt eiaahteelacssecnh"

offset_list = []
printGap(m1, c1)
printGap(m1, c2)
printGap(m1, c3)
printGap(m1, c4)

# for index, character in enumerate(m1):
#     if character == " ":
#         continue
#     offset = changerNum(ord(c1[index])) - changerNum(ord(m1[index]))
#     offset_list.append(offset % 52)
#     print offset % 52,
# print ""

key_list = ""
for index, character in enumerate(m1):
    p = LETTERS.find(m1[index])
    c = LETTERS.find(c1[index])
    y = 0
    key = c + len(LETTERS) * y - p
    while key < 0 :
        y += 1
        key = c + len(LETTERS) * y - p
    key_list += alphabet[key]
print key_list

print encryptMessage(key_list, m1)
print decryptMessage(key_list, c2)