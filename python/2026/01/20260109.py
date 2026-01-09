# Circular Prime

# Given an integer, determine if it is a circular prime.

# A circular prime is an integer where all rotations of its digits are themselves prime.

# For example, 197 is a circular prime because all rotations of its digits: 197, 971, and 719, are prime numbers.
# Tests

# 1. is_circular_prime(197) should return True.
# 2. is_circular_prime(23) should return False.
# 3. is_circular_prime(13) should return True.
# 4. is_circular_prime(89) should return False.
# 5. is_circular_prime(1193) should return True.

import math

def is_circular_prime(n):
    rotations = []
    for i in range(len(str(n))):
        rotations.append(int(str(n)[i:] + str(n)[:i]))
    for rotation in rotations:
        if not is_prime(rotation):
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print(is_circular_prime(197))
print(is_circular_prime(23))
print(is_circular_prime(13))
print(is_circular_prime(89))
print(is_circular_prime(1193))

# Comments - not super difficult once the is_prime function is defined
# The main trick here is creating the rotations. The concept of rotations is not immediately obvious, but the partial slicing and concatenation makes sense once you understand how rotation works