from Crypto.PublicKey import RSA
import fractions

p = 1122830395489501760925799210383299
q = 1232179875868643257203600345344573
r = (p-1) * (q-1)
kt = open("public.pem").read()
key = RSA.importKey(kt)
n = key.n
e = key.e
d = 446680355796085616328464905309110344309206844273229453296104513865
private_key = RSA.construct((n, e, d, p, q))
dsmg = private_key.decrypt(open('flag.enc').read())
print dsmg