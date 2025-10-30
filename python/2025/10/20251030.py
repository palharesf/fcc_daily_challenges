# Nth Prime

# A prime number is a positive integer greater than 1 that is divisible only by 1 and itself. The first five prime numbers are 2, 3, 5, 7, and 11.

# Given a positive integer n, return the nth prime number. For example, given 5 return the 5th prime number: 11.
# Tests

# 1. nth_prime(5) should return 11.
# 2. nth_prime(10) should return 29.
# 3. nth_prime(16) should return 53.
# 4. nth_prime(99) should return 523.
# 5. nth_prime(1000) should return 7919.

def nth_prime(n):
    primes = []
    i = 2
    while len(primes) < n:
        if all(i % j != 0 for j in range(2, i)):
            primes.append(i)
        i += 1

    return primes[n - 1]

nth_prime(5)
nth_prime(10)
nth_prime(16)
nth_prime(99)
nth_prime(1000)

# Comments - entirely AI generated. It's an interesting challenge to read after it's solved, the implementation makes a lot of sense, but the syntax is a bit confusing to come up on my own