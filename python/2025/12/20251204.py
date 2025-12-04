# Permutation Count

# Given a string, return the number of distinct permutations that can be formed from its characters.

#     A permutation is any reordering of the characters in the string.
#     Do not count duplicate permutations.
#     If the string contains repeated characters, repeated arrangements should only be counted once.
#     The string will contain only letters (A-Z, a-z).

# For example, given "abb", return 3 because there's three unique ways to arrange the letters: "abb", "bab", and "bba".
# Tests

# 1. count_permutations("abb") should return 3.
# 2. count_permutations("abc") should return 6.
# 3. count_permutations("racecar") should return 630.
# 4. count_permutations("freecodecamp") should return 39916800.

def count_permutations(s):
    set_perms = set(s)
    from math import factorial
    numerator = factorial(len(s))
    denominator = 1
    for char in set_perms:
        count = s.count(char)
        denominator *= factorial(count)
    return numerator // denominator

print(count_permutations("abb"))  # should return 3
print(count_permutations("abc"))  # should return 6 
print(count_permutations("racecar"))  # should return 630
print(count_permutations("freecodecamp"))  # should return 39916800

# Comments - the math is harder than the code
# The first part is somewhat easy - we create a set with the unique chars in the string, and calculate the factorial combinations assuming all characters are different
# The for loop then handles repeated chars, as they reduce the number of potential combinations possible based on how many times they repeat on the string
# We finally take the division between the case assuming all chars are different by the combinations of repeating chars (which is 1 if no chars repeat)