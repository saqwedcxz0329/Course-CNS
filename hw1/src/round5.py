from fractions import gcd

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
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
    elif (ascii_code > 64):
        return ascii_code - 65 + 26

def shift(sentence):
    new_sentence = sentence[1:] + sentence[0]
    return new_sentence

LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
M = len(LETTERS)

m1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
c1 = "tTKDqQvjNcdFzfCXLHSPiblJagrmZhyxVEoApGeUMwWnkRuOBYIs"
# c2 = "tTKDqQvjNcdFzfCXLHSPiblJagrmZhyxVEoApGeUMwWnkRuOBYIs"
# c3 = "qixrFpoRTgcBLaHEuNvzAWKImOkShteGPbXCwUDfldjQMsyJZVYn"
# c4 = "GKuesHdfDYJOogWrEcyvNXiQwZatAPIVnBmTjMFULhpqxbSClRzk"
c2 = "eKhuah oswesheqs s tmoecHrn i cesednv vaatiared ikuc"

file = open("index.csv", "w")

for a in range(2, M):
    if gcd(a, M) == 1:
        # print a
        for b in range(1, M+1):
            if (a * 1 + b) % M == 20:
                print "===a: %d===b: %d===" %(a,b)
                print (a*2+b)%M
                # if (a * 2 + b) % M == 45:

# file.write("plaintext_index, cipher_index\n")
# for index, character in enumerate(m1):
#     plaintext_index = LETTERS.find(character)
#     cipher_index = LETTERS.find(c1[index])
#     print LETTERS[(plaintext_index - cipher_index) % 52]
#     file.write("%s, %s\n" %(plaintext_index, cipher_index))
# file.close()