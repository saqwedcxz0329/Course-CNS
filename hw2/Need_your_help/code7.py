from base64 import b64encode
from base64 import b64decode
from Crypto.PublicKey import RSA
import fractions

try:
    import gmpy
except ImportError as e:
    try:
        import gmpy2 as gmpy
    except ImportError:
        raise e

target_private_key = 'gYEA4G91UgXRBjUCrIBEEn9K6tqKxa34gwxh9eoMcXFMjqGoEGoqaUmAfS0PfcA4d/NSIbaXJs3C5qs1EVLbq1R9UsFxm355dqstWuZiot/i5XFR7x/O3Kfo6JR8NG0ytm52TESTy3H1SKTdwHuNY+L+jYv8qsvgUpoi+4rNj3vfySMCgYEA0IAJQyC+8WwM1FU40RNrEyimismQ8zjTB33hjgNnGLOaF0eElvv/2JNB+zmDigA1DENr8xp7wHO7bMHe7/SwN5h4tUOjxsGQBSSJclsCRvERYVLLFBvGehe97/rnEI3FXqkvK+D6dqSrpyybixLWoD61W1c3hwbH7qyoYmjcpHsCgYEAyqz8ppCoHVHb00mVr5qSXhnzPecIR9fz0u6ERCHLv/ZOXlxxZllBFkmN9sKSfAgYwGcygpFIE6TCrJ1F0Kfg8M3OOVxyde7Ja5AnvOwv64F1O1tfJLbhRr9olrOSG1sPq3o2eX+0wOBZfQxWN8DynYKwLtEkB5Q4SS4kyhFUmz8CgYAKA9xuCQii+Bm1qVJNWK1wAifdysjXpgcc+QL4m1k8aoQgUiMgTYKAmLI2qxCSdGgX6rUovEDtgaGjG7zlsc81HHHP4yvexDVyycqAX7bASZwYHK38jUj/XFyXRmoK9YRhg6bsaKYfRNGp+g6Oo50DnX+An7PfHIhGAq0j7P2MOQKBgQCYYsAvKd0smloD4Rf5yD8dbutHW4iu/l1CowG1Jzx4ulg4MPrSLbYO9xZHQoh7qukVrZeoePbOqftYvIw55OnBhN3TCgvicoHXLgn8DhQf5y8IOOEhV5Qm/Eo7524jv7+N9kyR7VOqMgp6sD59gMNz7Rzzh+BAwUdPQuYNskzyMA=='

target_key_set = b64decode(target_private_key).encode('hex').split('028181')
target_key_set[0] = target_key_set[0][4:]
target_key_set[2] = target_key_set[2].split('028180')
p = int(target_key_set[0], 16)
q = int(target_key_set[1], 16)
dP = int(target_key_set[2][0], 16)
dQ = int(target_key_set[2][1], 16)
qInv = int(target_key_set[3], 16)

print "p: %d" %p
print "q: %d" %q
print "d mod (p - 1): %d" %dP
print "d mod (q - 1): %d" %dQ
print "(inverse of q) mod p: %d" %qInv

n = p * q
r = (p-1) * (q-1)

e = 1
while e < r:
    print e
    if fractions.gcd(e, r) == 1:
        d = gmpy.invert(e, r)
        if d % (p-1) == dP and d % (q-1) == dQ:
            print 'n: %d' % n 
            print 'e: %d' % e
            print 'd: %d' % d
            print 'p: %d' % p
            print 'q: %d' % q
            break
    e += 1

private_key = RSA.construct((n, long(e), long(d), p, q))
print private_key.exportKey()
dsmg = private_key.decrypt(open('flag.enc').read())
print dsmg