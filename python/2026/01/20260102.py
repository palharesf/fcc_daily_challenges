# Nth Fibonacci Number

# Given an integer n, return the nth number in the fibonacci sequence.

# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
# Tests

# 1. nth_fibonacci(4) should return 2.
# 2. nth_fibonacci(10) should return 34.
# 3. nth_fibonacci(15) should return 377.
# 4. nth_fibonacci(40) should return 63245986.
# 5. nth_fibonacci(75) should return 1304969544928657.

def nth_fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    nminus2 = 0  # F(1)
    nminus1 = 1  # F(2)

    for i in range(3, n + 1):
        current = nminus1 + nminus2
        nminus2 = nminus1
        nminus1 = current

    return nminus1

print(nth_fibonacci(4))
print(nth_fibonacci(10))
print(nth_fibonacci(15))
print(nth_fibonacci(40))
print(nth_fibonacci(75))

# Comments - confusing. Easy to implement once you got the calculation clear in your head, but it is a confusing problem when you first look into it. Or maybe I'm just tired
# I think what tripped me off was using two accumulators instead of one, I ended up exponentially adding both to the existing sum instead of replacing the current sum by the new sum