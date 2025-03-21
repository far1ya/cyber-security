import random

def generate_private_key(p):
    """Generate a private key (random integer) less than p"""
    return random.randint(2, p-2)

def compute_public_key(g, private_key, p):
    """Compute the public key using (g^private_key) % p"""
    return pow(g, private_key, p)

def compute_shared_secret(received_public_key, private_key, p):
    """Compute the shared secret key using (received_public_key^private_key) % p"""
    return pow(received_public_key, private_key, p)

# Step 1: Publicly agreed prime (p) and base (g)
p = 23  # Small prime number for simplicity
g = 5   # Primitive root of p

print(f"Public values: Prime (p) = {p}, Base (g) = {g}")

# Step 2: Alice and Bob generate their private keys
alice_private = generate_private_key(p)
bob_private = generate_private_key(p)

print(f"Alice's Private Key: {alice_private}")
print(f"Bob's Private Key: {bob_private}")

# Step 3: Compute public keys
alice_public = compute_public_key(g, alice_private, p)
bob_public = compute_public_key(g, bob_private, p)

print(f"Alice's Public Key: {alice_public}")
print(f"Bob's Public Key: {bob_public}")

# Step 4: Exchange public keys and compute shared secret
alice_shared_secret = compute_shared_secret(bob_public, alice_private, p)
bob_shared_secret = compute_shared_secret(alice_public, bob_private, p)

print(f"Alice's Shared Secret: {alice_shared_secret}")
print(f"Bob's Shared Secret: {bob_shared_secret}")

# The shared secret keys should be the same!
assert alice_shared_secret == bob_shared_secret, "Key exchange failed!"
print("✅ Diffie-Hellman Key Exchange Successful!")

