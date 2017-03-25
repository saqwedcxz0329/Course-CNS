import collections

UNKNOWN_CHARACTER = "*"
key = [None] * 200
def strxor(a, b):     # xor two strings (trims the longer input)
    result = []
    for x, y in zip(a, b):
        ascii_code = ord(x) ^ ord(y)
        if ascii_code == 0: # the same character
            result.append("$") 
        elif (ascii_code>64 and ascii_code<91) or (ascii_code>96 and ascii_code<123): # is alphabet
            result.append(chr(ascii_code))
        else:
            result.append(UNKNOWN_CHARACTER)
    return "".join(result)

file = open("xor.txt", 'w')
with open("cipher") as f:
    content = f.readlines()
content = [x.strip() for x in content] 

for cur_index, ciphertext in enumerate(content):
    counter = collections.Counter()
    file.write(ciphertext.decode("hex") + "\n")
    for index, ciphertext2 in enumerate(content):
        if cur_index != index:
            c1XORc2 = strxor(ciphertext.decode('hex'), ciphertext2.decode('hex'))
            file.write(str(index) + "\n")
            file.write(c1XORc2 + "\n")
            file.write("---------------------------\n")
            for char_index , character in enumerate(strxor(ciphertext.decode('hex'), ciphertext2.decode('hex'))):
                if character != UNKNOWN_CHARACTER:
                    counter[char_index] += 1
    for index, value in counter.items():
        if value == 9:
            key[index] = chr(ord(ciphertext.decode("hex")[index]) ^ ord(" "))
    file.write("==============================\n")
print key
key_hex = ''.join([value.encode("hex") if value is not None else '00' for value in key])
print key_hex
for ciphertext in content:
    print strxor(ciphertext.decode("hex"), key_hex.decode("hex"))
file.close()