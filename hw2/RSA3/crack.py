import fractions
import sys
try:
    import gmpy
except ImportError as e:
    try:
        import gmpy2 as gmpy
    except ImportError:
        raise e

sys.setrecursionlimit(1000000)  # long type,32bit OS 4B,64bit OS 8B(1bit for sign)

# return (g, x, y) a*x + b*y = gcd(x, y)
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

n = '86e9c7020404c51bc1658056ccc12ac9ed2b8384eacf20f9b07483e88c8febca7f5cfa8f114e31a41fc59fbc34a576b3ee8965247a8a0a01e9f35b7fb3626869a459067f72e3e2bb2870027413fb2187ebe987fe14884a73f8bd74b7877a035879f116ee7ded572f2d9b9f0ec005088fe41fe9c83d54384367e4978318531a5331cb8d172c3757ed531f2c212f308488df0c81f9d3f1dd6d4010ee154d0f49cbfb5b9fc1badb17754c6934ada13dd4f0e2c7dead11d60b5aabb1a3e87a26421e87a7a8f67038f6c807a0649ff49e4859c359cddb8bf6a0be171ce0dd947a050df5ee87f6f90ec80a0120d31e9e0a8271b41799731bbed91abb00e7e5b827091f'
a_e = '7a69'
b_e = '3419'
a_cipher = '76286f21485c99d33c9b13e3c2a46fd7448a1677d7f970b5a2904537d2404231b01fa2843a582d5d052b6d213abd883a13e9c7033df87ef508f569b03346423642a78b6041744838113b3584a3325294582ce96a6598797c60b983229f937bf16492e6f006edfd9615da946118cb3aa44a575fa5a784631808feca03510a5d148403c845b675a9855f538317e4ac19116df4db9c19174c1cbd17e871b89190f45c3dd4a8df0c69499a9e4b904b10b0ad504ca34a11af61fad3228214deffc5bcd8b8d3e969b8e7c8694e53127f8233375402d6ae98949339c05c5c7e1879526784d16834337e57ec8f586351b950aec87533b16a4e4bc168d80d36425de16afe'
b_cipher = '38845905daedb2390232d0c4fc0c646c21a3115473e70e5b6568c86ac8b23435eb6aa99a2a3c7a9dd5ab3172767c3383d978e21c527daedc90e65ac4c3b81062c1a03905d0821b4b4d4ae7f2738fea2023f53d239bc0d580d951d5429ab2d286d71c6d50f185a93e67df6dd5348e815f817557d28f7a91a8d7742c20fd756b59211ec3cebd72e7cc5f329484b895b145156055eb456d151a2afa8854bd12365c5e9b36fd2a250992ee1da6828348a08292323b10743c1454039d978ef36f0d875d01d43dd2999e84e0d313eaf549c25e148ad8e35b235fd192fc3cd2f7e1a301d8678f665d17d3b228596d800e1e10923c3329ab346ab5639e5b71a3666ba55c'

n = int(n, 16)
a_e = int(a_e, 16)
b_e = int(b_e, 16)
a_cipher = int(a_cipher, 16)
b_cipher = int(b_cipher, 16)

g, a, b = egcd(a_e, b_e)
print 'a: ' + str(a)
print 'b: ' + str(b)
i = gmpy.invert(a_cipher, n)
# plaintext = (i**(-a) * b_cipher ** b) % n
plaintext = (pow(i, -a, n) * pow(b_cipher, b, n)) % n
plaintext = hex(plaintext)[2:].decode('hex')
print plaintext