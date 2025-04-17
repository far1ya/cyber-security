def mod_inverse(a, p):
    # Using Fermat's Little Theorem to calculate a^(p-2) mod p
    return pow(a, p - 2, p)

# Example usage:
a=int(input("enter value of a"))
p=int(input("enter value of p"))
inverse = mod_inverse(a, p)
print(f"The inverse of {a} modulo {p} is: {inverse}")
