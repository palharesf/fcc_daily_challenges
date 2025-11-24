# LCM

# Given two integers, return the least common multiple (LCM) of the two numbers.

# The LCM of two numbers is the smallest positive integer that is a multiple of both numbers. For example, given 4 and 6, return 12 because:

#     Multiples of 4 are 4, 8, 12 and so on.
#     Multiples of 6 are 6, 12, 18 and so on.
#     12 is the smallest number that is a multiple of both.

# Tests

# 1. lcm(4, 6) should return 12.
# 2. lcm(9, 6) should return 18.
# 3. lcm(10, 100) should return 100.
# 4. lcm(13, 17) should return 221.
# 5. lcm(45, 70) should return 630.

def lcm(a, b):
    start = max(a, b)
    while start % a != 0 or start % b != 0:
        start += 1
    return start

lcm(4, 6)
lcm(9, 6)
lcm(10, 100)
lcm(13, 17)
lcm(45, 70)

# Comments - pretty straightforward problem, AI gave me the problem almost immediately but it was along the lines I had imagined and would implement anyway