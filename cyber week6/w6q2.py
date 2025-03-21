def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    
    for char in plaintext:
        if char.isalpha():  
           start = ord('A') if char.isupper() else ord('a')
           encrypted_char = chr((ord(char) - start + shift) % 26 + start)
           encrypted_text += encrypted_char
        else:
            encrypted_text += char
    
    return encrypted_text


def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    
    for char in ciphertext:
        if char.isalpha():  
            # Shift based on the case (uppercase or lowercase)
            start = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - start - shift) % 26 + start)
            decrypted_text += decrypted_char
        else:
           
            decrypted_text += char
    
    return decrypted_text

plaintext = "Hello, World!"
shift = 3

encrypted_text = caesar_encrypt(plaintext, shift)
print("Encrypted Text:", encrypted_text)

decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Decrypted Text:", decrypted_text)
