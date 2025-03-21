import binascii
import random

def random_key(p):
   key = ""
   p = int(p)
   for _ in range(p):
      temp = random.randint(0, 1)
      temp = str(temp)
      key = key + temp
   return key

def exor_func(a, b):
   temp = ""
   for i in range(len(a)):
      if a[i] == b[i]:
         temp += "0"
      else:
         temp += "1"
   return temp

def convert_bin_to_dec(binary):
   string = int(binary, 2)
   return string

plaintext = "Hello Everyone"
print("Plain Text is:", plaintext)

plaintext_Ascii = [ord(x) for x in plaintext]
plaintext_Bin = [format(y, '08b') for y in plaintext_Ascii]
plaintext_Bin = "".join(plaintext_Bin)

n = len(plaintext_Bin) // 2
L1 = plaintext_Bin[0:n]
R1 = plaintext_Bin[n::]
m = len(R1)

K1 = random_key(m)
K2 = random_key(m)

f1 = exor_func(R1, K1)
R2 = exor_func(f1, L1)
L2 = R1

f2 = exor_func(R2, K2)
R3 = exor_func(f2, L2)
L3 = R2

bin_data = L3 + R3
str_data = ''

for i in range(0, len(bin_data), 7):
   temp_data = bin_data[i:i + 7]
   decimal_data = convert_bin_to_dec(temp_data)
   str_data = str_data + chr(decimal_data)

print("Cipher Text:", str_data)

L4 = L3
R4 = R3

f3 = exor_func(L4, K2)
L5 = exor_func(R4, f3)
R5 = L4

f4 = exor_func(L5, K1)
L6 = exor_func(R5, f4)
R6 = L5
plaintext1 = L6 + R6

plaintext1 = int(plaintext1, 2)
Rplaintext = binascii.unhexlify('%x' % plaintext1)
print("Decrypted Plain Text is: ", Rplaintext)
