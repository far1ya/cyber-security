import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def order_of_r_mod_n(r, n):
    if gcd(r, n) != 1:
        return "NOT defined"
    
    power = 1
    k = 1
    while power != 1:
        power = (power * r) % n
        k += 1
        if k > n:  
            return "NOT defined"
    
    return k

r, n = map(int, input("Enter value of r and n: ").split())

result = order_of_r_mod_n(r, n)
print(f"Order of {r} % ({n}) is {result}")
