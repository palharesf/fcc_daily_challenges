# FizzBuzz

# Given an integer (n), return an array of integers from 1 to n (inclusive), replacing numbers that are multiple of:

#     3 with "Fizz".
#     5 with "Buzz".
#     3 and 5 with "FizzBuzz".

# Tests

# 1. fizz_buzz(2) should return [1, 2].
# 2. fizz_buzz(4) should return [1, 2, "Fizz", 4].
# 3. fizz_buzz(8) should return [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8].
# 4. fizz_buzz(20) should return [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz"].
# 5. fizz_buzz(50) should return [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"].

def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result

print(fizz_buzz(2))  # [1, 2]
print(fizz_buzz(4))  # [1, 2, "Fizz", 4]
print(fizz_buzz(8))  # [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8]
print(fizz_buzz(20)) # [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz"]

# Comments - not super difficult but very interesting problem.
# Modulus division and creating a range are both very useful techniques that show up all the time