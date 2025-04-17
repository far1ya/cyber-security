def is_group(S, operation):
    # Closure check
    for a in S:
        for b in S:
            if operation(a, b) not in S:
                return False

    # Identity check
    identity = None
    for e in S:
        if all(operation(a, e) == a for a in S):
            identity = e
            break
    if identity is None:
        return False

    # Inverse check
    for a in S:
        if not any(operation(a, b) == identity for b in S):
            return False

    return True

def is_ring(S, add, mul):
    # Check if addition forms an abelian group
    if not is_group(S, add):
        return False

    # Check for closure under multiplication
    for a in S:
        for b in S:
            if mul(a, b) not in S:
                return False

    # Check for distributive property: a * (b + c) = a * b + a * c
    for a in S:
        for b in S:
            for c in S:
                if mul(a, add(b, c)) != add(mul(a, b), mul(a, c)):
                    return False

    return True

def is_field(S, add, mul):
    # Check if it's a ring
    if not is_ring(S, add, mul):
        return False

    # Check for multiplicative inverses for all non-zero elements
    for a in S:
        if a != 0:
            has_inverse = False
            for b in S:
                if mul(a, b) == 1:
                    has_inverse = True
                    break
            if not has_inverse:
                return False

    return True


# Example usage:
# Set and operations for checking group, ring, and field
S = {0, 1, 2, 3, 4}
add = lambda x, y: (x + y) % 5  # Addition modulo 5
mul = lambda x, y: (x * y) % 5  # Multiplication modulo 5

# Check if the set and operations form a group, ring, or field
print("Is group:", is_group(S, add))  # Should return True
print("Is ring:", is_ring(S, add, mul))  # Should return True
print("Is field:", is_field(S, add, mul))  # Should return True
