# Digits vs Letters

# Given a string, return "digits" if the string has more digits than letters, "letters" if it has more letters than digits, and "tie" if it has the same amount of digits and letters.

#     Digits consist of 0-9.
#     Letters consist of a-z in upper or lower case.
#     Ignore any other characters.

# Tests

# 1. digits_or_letters("abc123") should return "tie".
# 2. digits_or_letters("a1b2c3d") should return "letters".
# 3. digits_or_letters("1a2b3c4") should return "digits".
# 4. digits_or_letters("abc123!@#DEF") should return "letters".
# 5. digits_or_letters("H3110 W0R1D") should return "digits".
# 6. digits_or_letters("P455W0RD") should return "tie".

def digits_or_letters(s):

    letters = 0
    digits = 0

    for char in s:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1

    if digits > letters:
        result = "digits"
    elif digits < letters:
        result = "letters"
    else:
        result = "tie"

    print(result)
    return result

digits_or_letters("abc123")
digits_or_letters("a1b2c3d")
digits_or_letters("1a2b3c4")
digits_or_letters("abc123!@#DEF")
digits_or_letters("H3110 W0R1D")
digits_or_letters("P455W0RD")

# Comments - very straightforward implementation. There could be more elegant ways to accomplish that, but it is moot for this challenge