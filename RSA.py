
import random
from fractions import gcd

# TODO: Mathematical proof in a python notebook


def extendedEuclidean(num1, num2):
    """
    This is an extension of euclid's algorithm to find gcd of two numbers
    It solves for x, y in the following equation
    num1 * x + num2 * y = gcd(num1, num2)
    Refer wikipedia's page or section 31.2 in CLRS
    """
    if num2 == 0:
        return (num1, 1, 0)

    d, temp_x, temp_y = extendedEuclidean(num2, num1 % num2)

    # TODO: see python notebook for explanation
    x, y = temp_y, temp_x - int(num1 / num2) * temp_y

    return (d, x, y)

################################################
# Well turns out this naive primality test is
# pathetically slow in actual practical cases
# such as checking primality of a 512 bit number
# (should have judged as this number can reach
# 10^100 easily, not an easy number to check
# for primality)
###############################################
# def isPrime(num):
#     """
#     Checking for the primality of the number
#     """
#     if num % 2 == 0 and num > 2:
#         return False
#     i = 3
#     num_sqrt = num**0.5
#     while i <= num_sqrt:
#         if num % i == 0:
#             return False
#         i += 2
#     return True


# The way it is done is using probabilistic methods
# One such is Rabin-Miller primality test
def rabinMillerTest(p, iteration):
    """
    :param n: is the number to be tested
    :param a: is the randomly chosen number
    :return: boolean that the number is prime or not
    """
    # Many texts and videos describe these such as section 31.8 CLRS
    # https://www.youtube.com/watch?v=p5S0C8oKpsM But topcoder's
    # "primality test" page describes this in sufficient details
    # So that is what we are going to use
    if p < 2:
        return False
    if p != 2 and p % 2 == 0:
        return False
    s = p-1
    while s % 2 == 0:
        s //= 2
    for i in range(iteration):
        a = random.randint(1, p-1)
        temp = s
        mod = pow(a, temp, p)  # Computes (a^temp)%p
        while temp != p-1 and mod != 1 and mod != p-1:
            mod = pow(mod, mod, p)
            temp *= 2

        if mod != p-1 and temp % 2 == 0:
            return False

    return True


def multiplicativeInverse(a, b, n):
    """
    Generating multiplicative inverse of given numbers (a,b modulo n)
    Refer Section 31.4 CLRS
    """
    d, x, y = extendedEuclidean(a, n)
    if b % d == 0:
        temp_x = (x * (b/d)) % n
        result = []
        for i in range(d):
            result.append((temp_x + i*(n/d)) % n)
        return result
    return []


def generateRandomPrime(bits):
    """
    Generate <bits> bit random prime number
    """
    num = random.getrandbits(bits - 1)
    if num % 2 == 0:
        num -= 1
    num += (1 << (bits - 1))
    while(not rabinMillerTest(num, 40)):
        num += 2

    return num


def generate(bits=512):
    p = generateRandomPrime(bits//2)
    q = p
    while q == p:
        q = generateRandomPrime(bits//2)
    n = p*q
    phi = (p-1) * (q-1)
    e = random.randint(1, 50000)
    e = 2*e + 1
    while not (gcd(phi, e) == 1):
        e = random.randint(1, 50000)
        e = 2*e + 1

    # It returns a list with only one item
    d = multiplicativeInverse(e, 1, phi)[0]
    return {
        "public": (e, n),
        "private": (int(d), n)
    }


def encrypt(keys, text):
    """
    :param
    """
    key, n = keys
    result = [pow(ord(c), key, n) for c in text]
    return result


def decrypt(keys, text):
    # NOTE: The mathematical function implemented by both the encrypt
    # and decrypt functions are exactly the same. We can call encrypt
    # again to decrypt our ciphertext. But the problem is encrypt converts
    # text from characters to extremely large numbers which can not be
    # encoded in characters. So calling chr(on_extremely_large_number)
    # will throw some kind of error
    key, n = keys
    result = [chr(pow(int(c), int(key), int(n) )) for c in text]
    return ''.join(result)

