import random

# Function to find greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find multiplicative inverse
def multiplicative_inverse(e, phi):
    d = 0
    x1, x2, y1 = 0, 1, 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi, e = e, temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2, x1 = x1, x
        d, y1 = y1, y

    if temp_phi == 1:
        return d + phi

# Check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True

# Generate key pair
def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be the same.')

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))

# Encrypt
def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

# Decrypt
def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

# Example usage
if __name__ == '__main__':
    print("RSA Encrypter/Decrypter")
    p = 61
    q = 53
    public, private = generate_keypair(p, q)
    print("Public key:", public)
    print("Private key:", private)

    message = "hello"
    encrypted_msg = encrypt(public, message)
    print("Encrypted:", encrypted_msg)

    decrypted_msg = decrypt(private, encrypted_msg)
    print("Decrypted:", decrypted_msg)
