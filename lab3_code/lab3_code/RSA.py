import random


# fnction for finding gcd of two numbers using euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# uses extened euclidean algorithm to get the d value
# for more info look here: https://crypto.stackexchange.com/questions/5889/calculating-rsa-private-exponent-when-given-public-exponent-and-the-modulus-fact
# will also be explained in class


def get_d(e, z):
    z1 = z

    d, x1, y0, y1 = 0, 1, 1, 0

    while e != 0:
        q, z, e = z // e, e, z % e
        y0, y1, = y1, y0 - q * y1
        d, x1, = x1, d - q * x1


    while d < 0:
        d = d + z1

    return d


def is_prime(num):
    if num > 1:

        # Iterate from 2 to n / 2
        for i in range(2, num // 2):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
                break
            else:
                return True

    else:
        return False


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    
    n = p * q
    z = (p - 1)*(q - 1)
    e = random.randrange(2, z)

    g = gcd(e, z)
    while g != 1:
        e = random.randrange(2, z)
        g = gcd(e, z)

    d = get_d(e, z)
    return (e, n), (d, n)


def encrypt(pk, plaintext):
    # plaintext is a single character
    # cipher is a decimal number which is the encrypted version of plaintext
    # the pow function is much faster in calculating power compared to the ** symbol !!!
    cipher = pow(ord(plaintext), int(pk[0]),  int(pk[1]))
    return cipher


def decrypt(pk, ciphertext):
    # ciphertext is a single decimal number
    # the returned value is a character that is the decryption of ciphertext
    plain = chr(pow(ciphertext, int(pk[0]),  int(pk[1])))
    return plain
