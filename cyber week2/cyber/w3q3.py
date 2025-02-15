import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def euler_totient(n):
    count = 0
    for i in range(1, n):
        if gcd(n, i) == 1:
            count += 1
    return count

num = int(input("Enter a number: "))
result = euler_totient(num)
print(f"Euler Totients of {num} is {result}")
