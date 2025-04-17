import hashlib

def compute_md5(message):
    print("Original Message:", message)

    # Convert message to bytes
    message_bytes = message.encode('utf-8')

    # Create MD5 hash object and get the digest
    md5_hash = hashlib.md5(message_bytes).hexdigest()

    print("MD5 Hash:         ", md5_hash)

# Example usage
compute_md5("Hello from Python!")
