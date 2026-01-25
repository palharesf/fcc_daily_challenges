# Hex Validator

# Given a string, determine whether it is a valid CSS hex color. A valid CSS hex color must:

#     Start with a #, and
#     be followed by either 3 or 6 hexadecimal characters.

# Hexadecimal characters are numbers 0 through 9 and letters a through f (case-insensitive).
# Tests

# 1. is_valid_hex("#123") should return True.
# 2. is_valid_hex("#123abc") should return True.
# 3. is_valid_hex("#ABCDEF") should return True.
# 4. is_valid_hex("#0a1B2c") should return True.
# 5. is_valid_hex("#12G") should return False.
# 6. is_valid_hex("#1234567") should return False.
# 7. is_valid_hex("#12 3") should return False.
# 8. is_valid_hex("fff") should return False.

import re

def is_valid_hex(s):
    if s[0] != "#":
        return False
    if len(s) == 4 and re.match(r"^[0-9a-fA-F]+$", s[1:]):
        return True
    if len(s) == 7 and re.match(r"^[0-9a-fA-F]+$", s[1:]):
        return True
    else:
        return False

print(is_valid_hex("#123"))
print(is_valid_hex("#123abc"))
print(is_valid_hex("#ABCDEF"))
print(is_valid_hex("#0a1B2c"))
print(is_valid_hex("#12G"))
print(is_valid_hex("#1234567"))
print(is_valid_hex("#12 3"))
print(is_valid_hex("fff"))

# Simple regex, but a bit tricky