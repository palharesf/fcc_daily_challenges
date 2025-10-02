# Decimal to Binary

# Given a non-negative integer, return its binary representation as a string.

# A binary number uses only the digits 0 and 1 to represent any number. To convert a decimal number to binary, repeatedly divide the number by 2 and record the remainder. Repeat until the number is zero. Read the remainders last recorded to first. For example, to convert 12 to binary:

# 12 ÷ 2 = 6 remainder 0
# 6 ÷ 2 = 3 remainder 0
# 3 ÷ 2 = 1 remainder 1
# 1 ÷ 2 = 0 remainder 1

# 12 in binary is 1100.
# Tests

# 1. to_binary(5) should return "101".
# 2. to_binary(12) should return "1100".
# 3. to_binary(50) should return "110010".
# 4. to_binary(99) should return "1100011".

def to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    
    # print(binary)    
    return binary

to_binary(5)
to_binary(12)
to_binary(50)
to_binary(99)

# Comments - the logic is quite straightforward and well explained in the example, so the AI had no issue suggesting a correct answer in the first try
# It was still helpful to familiarize myself with integer division and remember remainder division