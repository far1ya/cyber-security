def xor_encrypt_decrypt(plaintext, key):
    # Convert the plaintext to a list of ASCII values
    plaintext_bytes = [ord(c) for c in plaintext]
    
    # Perform XOR operation on each byte with the key
    encrypted_decrypted_bytes = [byte ^ key for byte in plaintext_bytes]
    
    # Convert the result back to characters
    result = ''.join(chr(byte) for byte in encrypted_decrypted_bytes)
    
    return result

plaintext = "Cyber Security"

print("Original Text:", plaintext)

encrypted_0 = xor_encrypt_decrypt(plaintext, 0)
encrypted_1 = xor_encrypt_decrypt(plaintext, 1)
encrypted_5 = xor_encrypt_decrypt(plaintext, 5)

print("\nEncrypted with key 0:", encrypted_0)
print("Encrypted with key 1:", encrypted_1)
print("Encrypted with key 5:", encrypted_5)

decrypted_0 = xor_encrypt_decrypt(encrypted_0, 0)
decrypted_1 = xor_encrypt_decrypt(encrypted_1, 1)
decrypted_5 = xor_encrypt_decrypt(encrypted_5, 5)

print("\nDecrypted with key 0:", decrypted_0)
print("Decrypted with key 1:", decrypted_1)
print("Decrypted with key 5:", decrypted_5)
