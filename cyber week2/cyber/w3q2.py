import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_mersenne_prime(p):
    if not is_prime(p):
        return False
    k = math.log2(p + 1)
    return k.is_integer()

num = int(input("Enter a prime number: "))

if is_mersenne_prime(num):
    print(f"{num} is a Mersenne prime")
else:
    print(f"{num} is NOT Mersenne prime")
