from fractions import gcd
import random
import fractions
try:
    import gmpy
except ImportError as e:
    try:
        import gmpy2 as gmpy
    except ImportError:
        raise e

# Returns a tuple (r, t) | n = r*2^t
# Complexity O(lg n)*
def remove_even(n):
    if n == 0:
        return (0, 0)
    r = n
    t = 0
    while (r & 1) == 0:
        t = t + 1
        r = r >> 1
    return (r, t)

# Returns a non-trivial sqrt(1) mod N, or None
# Arguments:
#     x: random integer 2 <= x < N
#     k: multiple of lambda(N)
#     N: modulus
# Complexity O((lg n)^3)
def get_root_one(x, k, N):
    (r, t) = remove_even(k)
    oldi = None
    i = pow(x, r, N)
    while i != 1:
        oldi = i
        i = (i*i) % N
    if oldi == N-1:
        return None #trivial
    return oldi

# Returns a tuple (p, q) that are 
# the prime factors of N, given an
# RSA key (e, d, N)
def factor_rsa(e, d, N):
    k = e*d - 1
    y = None
    while not y:
        x = random.randrange(2, N)
        y = get_root_one(x, k, N)
    p = fractions.gcd(y-1, N)
    q = N // p
    return (p, q)

def calc_values(p, q, e):
    n = p * q

    if p != q:
        phi = (p - 1) * (q - 1)
    else:
        phi = (p ** 2) - p

    d = gmpy.invert(e, phi)
    return d


N = '54fe961727ecdac6b18584c811fabe147004072729e47ab1d41ec87afd708803109458c4e0727ada0af7a780aea28773e4eac42347efb0653967b9ec888a938b774c9655b29ef55023ad22423d6a8aee85e19615a475b73ae2ae35b9caff87805a5238861e01188ed78884fd331ee9687eabc22f11fd98fe7af7d9a7a59e9965d5b986271fb9cbb0f42a9bcc56352aff3891836d9ca37c7ca6864d81c46c13fc3d399ac456f6f5b87d68fa9991d5ccaf240e39eb32e04de4c717894b89278c445f3364ceece2dd22d09958a7b379c70c727571a3adc80898ececc1a94ab3e1b4823cb66d483606877c2c29ee5fa187307924ebaca1a7e3b9432edd79a1c3e62f'
E = '7'
D = '1848bd2b2ffa87a67bdd015dbbfe7f738db8020b308a6c32cee43947b62026dc4de13def1b8e6c3e4c46c224c42e6fd7f8431377cb690dd3c742351f0270bc70fd8398aac551fcf2535609c9c8679568b88998987821a210d30d33ebf0db4b493e60a26f764974bb19026f23c5768bd4b67a377b29b62bb66c46d0790abf998a7a688354cda66bd1fbaea8cb3f3054ab1d1f0bc9adea01e80388851c3044f31238b693df3c79e7b41d30db04c44d907e36d32c11fff4af884de043dcca5ed583563577d4ba8274a8778c52ad9140e9f834d0a5ae5d8436372dd320c97d41ccfe7d55b31fce98bb4aeca7ece05d2ce3c980694158e79d289248ab48066ae552f7'
Alice_E = '7a69'

N = int(N, 16)
E = int(E, 16)
D = int(D, 16)
Alice_E = int(Alice_E, 16)

p, q = (factor_rsa(E, D, N))

Alice_D = calc_values(p, q, Alice_E)
cipher = '1689fe593e82bb93135e34cbb8b85b0cd3378c663320a06d2968b310dd5b82ae8488708a9bce8377b327fb88a298acf03488d89917561124fba352562c6c0c51081187c2cc0f6e8abe899035a8a985e36e010f55b4e5fced70ac07187ea369a2b4b4257c3086b6aceca2dc63c9b7f2e4c3af1b778074b9fb66997c7fbbdee6c1155f553b33a61d496412dfd3cf85104955b1eee5dc7ce48f3ef212996629521094a29c5fa703c66eef714e4114e7349c78477519b6bac54baa8297f75f517ac4a2b4c5e8e91df9db38f9fb85b566c837653a6f8eae8a754473288bd4eb2576929b8d036403f7777d08543ccac551183a705182c12c9d9afc0c087318581b451f'
cipher = int(cipher, 16)
print (hex(pow(cipher, Alice_D, N))[2:]).decode('hex')