import random

class SimpleTwofish:
    def __init__(self, key):
        self.key = self.expand_key(key)

    def expand_key(self, key):
        """Expands the key into a pseudo-random sequence."""
        random.seed(sum(bytearray(key.encode())))  # Seed based on key
        return [random.randint(0, 255) for _ in range(16)]  # Generate key schedule

    def encrypt(self, plaintext):
        """Encrypts the plaintext using a simple XOR cipher."""
        encrypted = [chr(ord(c) ^ self.key[i % len(self.key)]) for i, c in enumerate(plaintext)]
        return "".join(encrypted)

    def decrypt(self, ciphertext):
        """Decrypts the ciphertext by applying the same XOR operation."""
        decrypted = [chr(ord(c) ^ self.key[i % len(self.key)]) for i, c in enumerate(ciphertext)]
        return "".join(decrypted)

# Take user input
key = input("Enter a secret key (8-16 characters): ")
plaintext = input("Enter text to encrypt: ")

# Encrypt and Decrypt
cipher = SimpleTwofish(key)
ciphertext = cipher.encrypt(plaintext)
print("Encrypted:", ciphertext)

decrypted_text = cipher.decrypt(ciphertext)
print("Decrypted:", decrypted_text)
