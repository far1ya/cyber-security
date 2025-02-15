def is_power_of_2(n):
    # A number is in the form of 2^k if it's greater than 0 and is a power of 2
    return n > 0 and (n & (n - 1)) == 0


num = int(input("Enter a number: "))

if is_power_of_2(num):
    print(f"{num} is in the form of 2^k")
else:
    print(f"{num} is NOT in the form of 2^k")
