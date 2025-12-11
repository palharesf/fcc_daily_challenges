# Roman Numeral Builder

# Given an integer, return its equivalent value in Roman numerals.

# Roman numerals use these symbols:
# Symbol 	Value
# I 	1
# V 	5
# X 	10
# L 	50
# C 	100
# D 	500
# M 	1000

# Roman numerals are written from largest to smallest, left to right using the following rules:

#     Addition is used when a symbol is followed by one of equal or smaller value. For example, 18 is written as XVIII (10 + 5 + 1 + 1 + 1 = 18).
#     Subtraction is used when a smaller symbol appears before a larger one, to represent 4 or 9 in any place value. For example, 19 is written as XIX (10 + (10 - 1)).
#     No symbol may be repeated more than three times in a row. Subtraction is used when you would otherwise need to write a symbol more than three times in a row. So the largest number you can write is 3999.

# Here's one more example: given 1464, return "MCDLXIV" (1000 + (500 - 100) + 50 + 10 + (5 - 1)).
# Tests

# 1. to_roman(18) should return "XVIII".
# 2. to_roman(19) should return "XIX".
# 3. to_roman(1464) should return "MCDLXIV".
# 4. to_roman(2025) should return "MMXXV".
# 5. to_roman(3999) should return "MMMCMXCIX".

def to_roman(num):
    roman_numerals = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    output = ""
    for value, symbol in roman_numerals:
        while num >= value:
            output += symbol
            num -= value

    return output

print(to_roman(18))
print(to_roman(19))
print(to_roman(1464))
print(to_roman(2025))
print(to_roman(3999))

# Comments - very, very annoying exercise. Roman numerals were never fun in school, and they are still not fun when coding. Lookup table is the most straightforward way to code them, but I've initially tried the long handling like commented below, without proper implementing 4s and 9s
# def to_roman(num):
#     output = ""

#     # Handle 1000s
#     ms = num // 1000
#     num = num % 1000
#     output += "M" * ms

#     # Handle 900s and 500-800
#     if num >= 900:
#         output += "CM"
#         num -= 900
#     elif num >= 500:
#         output += "D"
#         num -= 500

#     # Handle 400s and 100-300
#     if num >= 400 and num < 500:
#         output += "CD"
#         num -= 400
#     else:
#         cs = num // 100
#         num = num % 100
#         output += "C" * cs

#     # Handle 90s and 50-80
#     if num >= 90:
#         output += "XC"
#         num -= 90
#     elif num >= 50:
#         output += "L"
#         num -= 50

#     # Handle 40s and 10-30
#     if num >= 40 and num < 50:
#         output += "XL"
#         num -= 40
#     else:
#         xs = num // 10
#         num = num % 10
#         output += "X" * xs

#     # Handle 9s and 5-8
#     if num == 9:
#         output += "IX"
#         num -= 9
#     elif num >= 5:
#         output += "V"
#         num -= 5

#     # Handle 4s and 1-3
#     if num == 4:
#         output += "IV"
#     else:
#         output += "I" * num

#     return output