from Crypto.PublicKey import RSA
import fractions

def phi(n):
    amount = 0
    k = 1
    while k < n + 1:
        # print k
        if fractions.gcd(n, k) == 1:
            amount += 1
        k += 1
    return amount

kt = open("public.pem").read()
key = RSA.importKey(kt)
print key.exportKey()
print "n: " +  str(key.n)
print "e: " +  str(key.e)
# print phi(key.n)
