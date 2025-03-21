import hashlib

# Take user input
text = input("Enter the text to hash: ")

# Compute SHA-1 hash
sha1_hash = hashlib.sha1(text.encode()).hexdigest()

# Print the message digest
print(f"SHA-1 Digest: {sha1_hash}")
