from Crypto.PublicKey import RSA
import fractions

p = 1122830395489501760925799210383299
q = 1232179875868643257203600345344573
r = (p-1) * (q-1)
kt = open("public.pem").read()
key = RSA.importKey(kt)
n = key.n
e = key.e
print "n: " +  str(n)
print "e: " +  str(e)
print key
d = '43dd1de2b05639352cd9a663b39389abbdbd0dcba43771badfe2149'
d = int(d, 16)
print 'd: ' + str(d)

cipher = open('flag.enc').read()
# print cipher
cipher =  cipher.encode('hex')
cipher = int(cipher, 16)
print (d*e) % r
# plaintext = pow(cipher, d, n)
# print (hex(plaintext)[2:-1]).decode('hex')

# msg = "abc"
# msg = msg.encode('hex')
# msg = int(msg, 16)
# print msg
# code = pow(msg, e, n)
# plaintext = pow(code, d, n)
# print (hex(plaintext)[2:-1]).decode('hex')
