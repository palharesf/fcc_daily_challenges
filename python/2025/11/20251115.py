# GCD

# Given two positive integers, return their greatest common divisor (GCD).

#     The GCD of two integers is the largest number that divides evenly into both numbers without leaving a remainder.

# For example, the divisors of 4 are 1, 2, and 4. The divisors of 6 are 1, 2, 3, and 6. So given 4 and 6, return 2, the largest number that appears in both sets of divisors.
# Tests

# 1. gcd(4, 6) should return 2.
# 2. gcd(20, 15) should return 5.
# 3. gcd(13, 17) should return 1.
# 4. gcd(654, 456) should return 6.
# 5. gcd(3456, 4320) should return 864.

def gcd(x, y):
    small = min(x, y)
    large = max(x, y)
    small_divisors = find_divisors(small)
    large_divisors = find_divisors(large)

    print(range(len(large_divisors) - 1, -1, -1))
    for i in range(len(small_divisors) - 1, -1, -1):
        if small_divisors[i] in large_divisors:
            return small_divisors[i]
    return 1

def find_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    print(divisors)
    return divisors

gcd(4, 6)
gcd(20, 15)
gcd(13, 17)
gcd(654, 456)
gcd(3456, 4320)

# Comments - not super difficult problem, but I was still proud of being able to solve it without AI
# The first clear thing was that I needed a support function to find divisors of a number. While simple and easily googlable, I decided to get AI help here
# With that in tow, it became a matter of using the data already available in a way that made sense. Required a bit of finaggling but wasn't too difficult and I'm glad it worked out of the box