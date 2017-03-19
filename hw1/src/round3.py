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

m1 = "computers developed Classical ciphers are commonly"
c1 = "ivuyeeqeg tvnxfjlbb Cmcvwniht mtbusgi sky ylkloonb"
c2 = "nl txzif pdp tgjqkr og spfoubnhe nbs tgklzommmdjpj"

offset = (ord(c1[0]) - ord(m1[0])) % 26
"""
offset = (ord(c1[0]) - ord(m1[0])) % 26
for index, character in enumerate(m1):
    offset = ord(c1[index]) - ord(m1[index])
    print offset % 26
"""
m2 = ""
for index , character in enumerate(c2):
    cur_offset  =  (offset + index) % 26
    m2 += decode(character, cur_offset)
print m2 + "\n"