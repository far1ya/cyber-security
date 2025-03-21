import numpy as np

key_matrix = np.zeros((3, 3), dtype=int)
message_vector = np.zeros((3, 1), dtype=int)
cipher_matrix = np.zeros((3, 1), dtype=int)

def get_key_matrix(key):
   k = 0
   for i in range(3):
      for j in range(3):
         key_matrix[i][j] = ord(key[k]) % 65
         k += 1

def encrypt(message_vector):
   for i in range(3):
      cipher_matrix[i][0] = 0
      for x in range(3):
         cipher_matrix[i][0] += (key_matrix[i][x] * message_vector[x][0])
      cipher_matrix[i][0] = cipher_matrix[i][0] % 26

def hill_cipher(message, key):
   get_key_matrix(key)
   for i in range(3):
      message_vector[i][0] = ord(message[i]) % 65
   encrypt(message_vector)
   ciphertext = [chr(cipher_matrix[i][0] + 65) for i in range(3)]
   print("The Ciphertext:", "".join(ciphertext))

message = "DOG"
key = "YHGINUKER"
hill_cipher(message, key)
