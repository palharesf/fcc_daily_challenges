# Vowels and Consonants

# Given a string, return an array with the number of vowels and number of consonants in the string.

#     Vowels consist of a, e, i, o, u in any case.
#     Consonants consist of all other letters in any case.
#     Ignore any non-letter characters.

# For example, given "Hello World", return [3, 7].
# Tests

# 1. count("Hello World") should return [3, 7].
# 2. count("JavaScript") should return [3, 7].
# 3. count("Python") should return [1, 5].
# 4. count("freeCodeCamp") should return [5, 7].
# 5. count("Hello, World!") should return [3, 7].
# 6. count("The quick brown fox jumps over the lazy dog.") should return [11, 24].

def count(s):
    count_array = [0, 0]
    for char in s:
        if char in "aeiouAEIOU":
            count_array[0] += 1
        elif char.isalpha():
            count_array[1] += 1
    return count_array

count("Hello World")
count("JavaScript")
count("Python")
count("freeCodeCamp")
count("Hello, World!")
count("The quick brown fox jumps over the lazy dog.")

# Comments - AI almost solved it in one go, but messed up variable names
# It's not elegant but it works. My original plan was having arrays with consonants and vowels and checking if each char is included in each array, but in this case the solution is probably even simpler than that (although less robuts)