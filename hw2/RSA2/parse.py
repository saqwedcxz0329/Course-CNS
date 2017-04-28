from fractions import gcd
import random
import fractions

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

N = '54fe961727ecdac6b18584c811fabe147004072729e47ab1d41ec87afd708803109458c4e0727ada0af7a780aea28773e4eac42347efb0653967b9ec888a938b774c9655b29ef55023ad22423d6a8aee85e19615a475b73ae2ae35b9caff87805a5238861e01188ed78884fd331ee9687eabc22f11fd98fe7af7d9a7a59e9965d5b986271fb9cbb0f42a9bcc56352aff3891836d9ca37c7ca6864d81c46c13fc3d399ac456f6f5b87d68fa9991d5ccaf240e39eb32e04de4c717894b89278c445f3364ceece2dd22d09958a7b379c70c727571a3adc80898ececc1a94ab3e1b4823cb66d483606877c2c29ee5fa187307924ebaca1a7e3b9432edd79a1c3e62f'
E = '7'
D = '1848bd2b2ffa87a67bdd015dbbfe7f738db8020b308a6c32cee43947b62026dc4de13def1b8e6c3e4c46c224c42e6fd7f8431377cb690dd3c742351f0270bc70fd8398aac551fcf2535609c9c8679568b88998987821a210d30d33ebf0db4b493e60a26f764974bb19026f23c5768bd4b67a377b29b62bb66c46d0790abf998a7a688354cda66bd1fbaea8cb3f3054ab1d1f0bc9adea01e80388851c3044f31238b693df3c79e7b41d30db04c44d907e36d32c11fff4af884de043dcca5ed583563577d4ba8274a8778c52ad9140e9f834d0a5ae5d8436372dd320c97d41ccfe7d55b31fce98bb4aeca7ece05d2ce3c980694158e79d289248ab48066ae552f7'
Alice_E = '7a69'

N = int(N, 16)
E = int(E, 16)
D = int(D, 16)
Alice_E = int(Alice_E, 16)

print "n: " + str(N)
print "e: " + str(E)
print "d: " + str(D)
print "Alice's e: " + str(Alice_E)

# A valid keypair mod N
# e = 262139
# d = 9451846527955896036458759652560972624637617897909079398699

print("Factoring N...")
p, q = (factor_rsa(E, D, N))
print "p: " + str(p)
print "q: " + str(q)
print "r: " + str((p-1) * (q-1))