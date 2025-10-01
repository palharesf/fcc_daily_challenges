# Binary to Decimal

# Given a string representing a binary number, return its decimal equivalent as a number.

# A binary number uses only the digits 0 and 1 to represent any number. To convert binary to decimal, multiply each digit by a power of 2 and add them together. Start by multiplying the rightmost digit by 2^0, the next digit to the left by 2^1, and so on. Once all digits have been multiplied by a power of 2, add the result together.

# For example, the binary number 101 equals 5 in decimal because:

# 1 * 2^2 + 0 * 2^1 + 1 * 2^0 = 4 + 0 + 1 = 5

# Tests

# 1. to_decimal("101") should return 5.
# 2. to_decimal("1010") should return 10.
# 3. to_decimal("10010") should return 18.
# 4. to_decimal("1010101") should return 85.

def to_decimal(binary):

    num_digits = len(binary)
    decimal = 0

    for digit in range(num_digits):
        decimal += int(binary[num_digits - 1 - digit]) * 2 ** digit
    
    # print(decimal)
    return decimal

to_decimal("101")
to_decimal("1010")
to_decimal("10010")
to_decimal("1010101")

# Comments: quite straightforward challenge. Knowing how to convert manually indicates a loop you can use here
# The loop consists of checking digit by digit, and for those that are not zero, powering it to 2^digit