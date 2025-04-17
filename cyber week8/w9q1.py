import hashlib

def compute_hashes(message):
    print("Original Message:", message)

    # Encode the message to bytes
    message_bytes = message.encode()

    # SHA1
    sha1_hash = hashlib.sha1(message_bytes).hexdigest()
    print("SHA1:      ", sha1_hash)

    # SHA2 (SHA256)
    sha256_hash = hashlib.sha256(message_bytes).hexdigest()
    print("SHA256:    ", sha256_hash)

    # SHA3 (SHA3-256)
    sha3_256_hash = hashlib.sha3_256(message_bytes).hexdigest()
    print("SHA3-256:  ", sha3_256_hash)

# Example usage
compute_hashes("Hello from SageMath!")
