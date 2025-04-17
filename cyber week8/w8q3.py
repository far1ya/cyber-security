import random

# Function to perform modular exponentiation (base^exp mod mod)
def power(base, exp, mod):
    return pow(base, exp, mod)

# Prime number (p) and primitive root (g)
# In real applications, p should be a large prime number
p = 23    # Prime number
g = 5     # Primitive root modulo p

# Alice's private key (a)
a = random.randint(1, p - 1)
# Alice's public key (A = g^a mod p)
A = power(g, a, p)

# Bob's private key (b)
b = random.randint(1, p - 1)
# Bob's public key (B = g^b mod p)
B = power(g, b, p)

# Exchange public keys and compute shared secret
# Alice computes shared secret: s = B^a mod p
s_alice = power(B, a, p)
# Bob computes shared secret: s = A^b mod p
s_bob = power(A, b, p)

print("Public prime (p):", p)
print("Primitive root (g):", g)

print("\n--- Key Exchange ---")
print("Alice's private key:", a)
print("Alice's public key (A):", A)
print("Bob's private key:", b)
print("Bob's public key (B):", B)

print("\n--- Shared Secret ---")
print("Shared secret computed by Alice:", s_alice)
print("Shared secret computed by Bob:  ", s_bob)

# Check if shared secrets match
if s_alice == s_bob:
    print("\n✅ Key exchange successful!")
else:
    print("\n❌ Key exchange failed!")
