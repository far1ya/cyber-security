import string

def create_playfair_matrix(key):
    matrix = []
    
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))  # remove duplicates
    key = key.replace('J', 'I')  # Combine I and J into one letter
    alphabet = string.ascii_uppercase.replace('J', '')  # Remove J from alphabet

    matrix.extend(list(key))

    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return matrix

def preprocess_text(text):
    text = text.upper().replace('J', 'I')  # Treat 'J' as 'I'
    processed_text = []

    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i+1]:
            processed_text.append(text[i] + 'X')  # Insert 'X' between duplicate letters
            i += 1
        else:
            processed_text.append(text[i:i+2])  # Add pair of characters
            i += 2
        if len(processed_text[-1]) == 1:
          processed_text[-1] += 'X'
    
    return processed_text


# Function to find the position of a letter in the Playfair matrix
def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None


# Encryption function using the Playfair cipher
def encrypt_playfair(plaintext, matrix):
    digraphs = preprocess_text(plaintext)  # Preprocess the text
    encrypted_text = []

    for digraph in digraphs:
        row1, col1 = find_position(matrix, digraph[0])
        row2, col2 = find_position(matrix, digraph[1])

        # Rule 1: If the letters are in the same row, replace them with the letters to the right
        if row1 == row2:
            encrypted_text.append(matrix[row1][(col1 + 1) % 5])
            encrypted_text.append(matrix[row2][(col2 + 1) % 5])

        # Rule 2: If the letters are in the same column, replace them with the letters below
        elif col1 == col2:
            encrypted_text.append(matrix[(row1 + 1) % 5][col1])
            encrypted_text.append(matrix[(row2 + 1) % 5][col2])

        # Rule 3: If the letters form a rectangle, replace them with the letters on the same row but in the opposite corners
        else:
            encrypted_text.append(matrix[row1][col2])
            encrypted_text.append(matrix[row2][col1])

    return ''.join(encrypted_text)

def decrypt_playfair(ciphertext, matrix):
    digraphs = preprocess_text(ciphertext)  # Preprocess the ciphertext
    decrypted_text = []

    for digraph in digraphs:
        row1, col1 = find_position(matrix, digraph[0])
        row2, col2 = find_position(matrix, digraph[1])

        # Rule 1: If the letters are in the same row, replace them with the letters to the left
        if row1 == row2:
            decrypted_text.append(matrix[row1][(col1 - 1) % 5])
            decrypted_text.append(matrix[row2][(col2 - 1) % 5])

        # Rule 2: If the letters are in the same column, replace them with the letters above
        elif col1 == col2:
            decrypted_text.append(matrix[(row1 - 1) % 5][col1])
            decrypted_text.append(matrix[(row2 - 1) % 5][col2])

        # Rule 3: If the letters form a rectangle, replace them with the letters on the same row but in the opposite corners
        else:
            decrypted_text.append(matrix[row1][col2])
            decrypted_text.append(matrix[row2][col1])

    return ''.join(decrypted_text)


# Example usage:
key = "KEYWORD"  # The key to create the Playfair matrix
matrix = create_playfair_matrix(key)

# Input text to encrypt and decrypt
plaintext = "HELLO"
ciphertext = encrypt_playfair(plaintext, matrix)
print(f"Encrypted Text: {ciphertext}")

decrypted_text = decrypt_playfair(ciphertext, matrix)
print(f"Decrypted Text: {decrypted_text}")
