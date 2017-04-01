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

m1 = "such as the Kasiski examination can still be"
c1 = "ibqj jf yxu Ahgkbxn unqtwpjgned shb ucvqb ru"
c2 = "Ssoubvhqb spdjnex qhu jcovbsbo gbwvn rfio jv ptnnp"

offset_list = [16, 7, 14, 2, 9, 13, 5, 16, 16]
# offset_list = []

for index, character in enumerate(m1):
    if character == " ":
        continue
    offset = ord(c1[index]) - ord(m1[index])
    offset_list.append(offset % 26)
    print offset % 26,
print ""

m2 = ""
offset_index = 0
for index , character in enumerate(c2):
    offset_index = offset_index % len(offset_list)
    m2 += decode(character, offset_list[offset_index])
    if character == " ":
        continue
    offset_index += 1
print m2 + "\n"