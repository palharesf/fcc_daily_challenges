# Credit Card Masker

# Given a string of credit card numbers, return a masked version of it using the following constraints:

#     The string will contain four sets of four digits (0-9), with all sets being separated by a single space, or a single hyphen (-).
#     Replace all numbers, except the last four, with an asterisk (*).
#     Leave the remaining characters unchanged.

# For example, given "4012-8888-8888-1881" return "****-****-****-1881".
# Tests

# 1. mask("4012-8888-8888-1881") should return "****-****-****-1881".
# 2. mask("5105 1051 0510 5100") should return "**** **** **** 5100".
# 3. mask("6011 1111 1111 1117") should return "**** **** **** 1117".
# 4. mask("2223-0000-4845-0010") should return "****-****-****-0010".

def mask(card):
    for digit in card[:-4]:
        if digit.isdigit():
            card = card.replace(digit, '*', 1)
    return card

mask("4012-8888-8888-1881")
mask("5105 1051 0510 5100")
mask("6011 1111 1111 1117")
mask("2223-0000-4845-0010")

# Comments: it was quite easy, as long as you keep in mind that you don't need to iterate through the whole string, just until the last 4 characters, and that you only need to replace the numbers, nothing else
# Luckily the built-in methods in Python makes this kind of stuff quite easy