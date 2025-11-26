# BuzzFizz

# Given an array, determine if it is a correct FizzBuzz sequence from 1 to the last item in the array. A sequence is correct if:

#     Numbers that are multiples of 3 are replaced with "Fizz"
#     Numbers that are multiples of 5 are replaced with "Buzz"
#     Numbers that are multiples of both 3 and 5 are replaced with "FizzBuzz"
#     All other numbers remain as integers in ascending order, starting from 1.
#     The array must start at 1 and have no missing or extra elements.

# Tests

# 1. is_fizz_buzz([1, 2, "Fizz", 4]) should return True.
# 2. is_fizz_buzz([1, 2, 3, 4]) should return False.
# 3. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", 7]) should return False.
# 4. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "FizzBuzz"]) should return False.
# 5. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Fizz"]) should return False.
# 6. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Buzz"]) should return False.
# 7. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"]) should return True.

def is_fizz_buzz(sequence):
    for i, num in enumerate(sequence):
        expected = ""
        index = i + 1
        if index % 3 == 0:
            expected += "Fizz"
        if index % 5 == 0:
            expected += "Buzz"
        if expected == "":
            expected = index
        if num != expected:
            return False
    return True

print(is_fizz_buzz([1, 2, "Fizz", 4]))  # True
print(is_fizz_buzz([1, 2, 3, 4]))  # False
print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", 7]))  # False
print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "FizzBuzz"]))  # False
print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Fizz"]))  # False
print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Buzz"]))  # False
print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"]))  # True

# Comments - Pretty straightforward. It's the reverse from yesterday.
# As long as you keep track of where you are in the sequence and what the expected value is, it's just a matter of comparing
# Not too tricky, enjoyable to implement