import collections

UNKNOWN_CHARACTER = "*"
key = [None] * 200
def strxor_define(a, b):     # xor two strings (trims the longer input)
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

def strxor(a, b):
    return ''.join([chr(ord(x) ^ ord(y)) for x, y in zip(a, b)])
        

    
file = open("xor.txt", 'w')
with open("cipher") as f:
    content = f.readlines()

content = [x.strip() for x in content] 
plaintext_list = [[None]*(len(ciphertext)/2) for ciphertext in content]

for cur_index, ciphertext in enumerate(content):
    counter = collections.Counter()
    file.write(ciphertext.decode("hex") + "\n")
    for index, ciphertext2 in enumerate(content):
        if cur_index != index:
            c1XORc2 = strxor_define(ciphertext.decode('hex'), ciphertext2.decode('hex'))
            file.write(str(index) + "\n")
            file.write(c1XORc2 + "\n")
            file.write("---------------------------\n")
            for char_index , character in enumerate(strxor_define(ciphertext.decode('hex'), ciphertext2.decode('hex'))):
                if character != UNKNOWN_CHARACTER:
                    counter[char_index] += 1
    space_index = []
    for index, value in counter.items():
        if value == 9:
            space_index.append(index)
            
    for index in space_index:
        plaintext = plaintext_list[cur_index]
        plaintext[index] = ' '
        plaintext_list[cur_index] = plaintext
        for c2_index, ciphertext2 in enumerate(content):
            if cur_index != c2_index:
                c1XORc2 = strxor_define(ciphertext.decode('hex'), ciphertext2.decode('hex'))
                if c1XORc2[index] != "$":
                    plaintext2 = plaintext_list[c2_index]
                    if c1XORc2[index].isupper():
                        plaintext2[index] = c1XORc2[index].lower()
                    else:
                        plaintext2[index] = c1XORc2[index].upper()
                    plaintext_list[c2_index] = plaintext2

#p1 = "*e is*ap*reh*nsive *bout*his interv*ew f*r th* su*me**inte*nshi**"
#p2 = "*hat *ep*rte* and h*s as*istants bu*st i*to t*nem*nt** sta*tlin**************************"
#p3 = "*erge* a*d a*quisit*on h*s come to *e co*side*ed * n** typ* of *****************"
#p4 = "* wil* g* do*ntown *o pi*k up some *roch*res *rom*th**trav*l ag****"
#p5 = "*he t*ng*e h*lds th* nec*ar by capi*lary*acti*n w*il**rapi*ly m*****************"
#p6 = "*ecau*e *he *ew pap*r mo*ey was eas* to *epli*ate* c**nter*eit **************************"
#p7 = "*here*we*e m*ny fru*tful* historica* pre*eden*s f*r **e us* of ****************"
#p8 = "*apit*li*m e*courag*d op*n competit*on i* pla*e o* s**ial *efer*******************"
#p9 = "*ALSN*us*ng * key o*e ti*e is not e*ough* hav* yo* t**ed u*ing **********"
#p10 = "*ost *mp*rta*t was *hat *hose paint*rs h*d al* ma*nt**ned * cer**************"

p1 = "He is apprehensive about his interview for the summer internship."
p2 = "That reporter and his assistants burst into tenements, sta*tlin**************************"
p3 = "Merger and acquisition has come to be considered a new type of popular"
p4 = "I will go downtown to pick up some brochures from the travel agent*"
p5 = "The tongue holds the nectar by capillary action while rapidly m*****************"
p6 = "Because the new paper money was easy to replicate, counter*eit **************************"
p7 = "There were many fruitful, historical precedents for the us* of ****************"
p8 = "Capitalism encouraged open competition in place of social deference"
p9 = "*ALSN*using a key one time is not enough, have you tried using **********"
p10 = "Most important was that those painters had all maintained * cer**************"

# p10
#predict_key = "7e3e348a47f108c6734ebaca4a1428e164ceece43881baa9bac491c2490cdd38648700a0cb35693d3ff8d468a45e71fcdffb2dd3ed9c196b5d2ab062ae543c69357d70800bb24689350de4994e"
# p8
#predict_key1 = "7e3e348a47f108c6734ebaca4a1428e164ceece43881baa9e4c491c2490cdd38648700a0cb35693d3ff8d468a41871fcdffb2dd3ed9c196b5d2afe61bc543c783a777b800cb546cc310df592014c61a337ca"
# p4
#predict_key2 = "7e3e348a47f108c6734ebaca4a1428e164ceece43881baa9e4c491c2490cdd38648700a0cb35693d3ff8d468a41871fcdffb2dd3ed9c196b5d2afb62ae543c377e3e30"
final_key = "7e3e348a47f108c6734ebaca4a1428e164ceece43881baa9e4c491c2490cdd38648700a0cb35693d3ff8d468a41871fcdffb2dd3ed9c196b5d2afb62ae543c37"
predict_key3 = "7e3e348a47f108c6734ebaca4a1428e164ceece43881baa9e4c491c2490cdd38648700a0cb35693d3ff8d468a41871fcdffb2dd3ed9c196b5d2afb62ae543c377e3e34"
predict_key4 = "7e3e348a47f108c6734ebaca4a1428e164ceece43881baa9e4c491c2490cdd38648700a0cb35693d3ff8d468a41871fcdffb2dd3ed9c196b5d2afb62ae543c377e3e348a47f1"

plaintext_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

keyi = strxor(plaintext_list[2], content[2].decode('hex'))
print "key: " + keyi.encode("hex")

final_key = final_key.decode("hex")
for cur_index, ciphertext in enumerate(content):
    plaintext = []
    ciphertext = ciphertext.decode("hex")
    for index, character in enumerate(ciphertext):
        index = index % len(final_key)
        plaintext.append(chr(ord(final_key[index]) ^ ord(character)))
    print ''.join(plaintext)


#for index, plaintext in enumerate(plaintext_list):
##    plaintext = ''.join(value if value is not None else "*" for value in plaintext)
##    print plaintext
###    print "plaintext: " + str(len(plaintext))
###    print "ciphertext: " + str(len(content[index].decode('hex')))
##    
##    keyi = strxor(plaintext, content[index].decode('hex'))
##    print "key: " + keyi.encode("hex")
##    print ""
#
#    print strxor(predict_key3.decode("hex"), content[index].decode("hex"))

file.close()