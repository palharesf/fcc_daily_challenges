# Letters-Numbers

# Given a string containing only letters and numbers, return a new string where a hyphen (-) is inserted every time the string switches from a letter to a number, or a number to a letter.
# Tests

# 1. separate_letters_and_numbers("ABC123") should return "ABC-123".
# 2. separate_letters_and_numbers("Route66") should return "Route-66.
# 3. separate_letters_and_numbers("H3LL0W0RLD") should return "H-3-LL-0-W-0-RLD".
# 4. separate_letters_and_numbers("a1b2c3d4") should return "a-1-b-2-c-3-d-4".

def separate_letters_and_numbers(s):
    result = ""
    last_was_char = False

    for index, char in enumerate(s):
        if index == 0:
            result += str(char)
            if str(char).isalpha():
                last_was_char = True
            else:
                last_was_char = False
        else:
            if str(char).isalpha() != last_was_char or str(char).isdigit() == last_was_char:
                result += "-"
            result += char
            if str(char).isalpha():
                last_was_char = True
            else:
                last_was_char = False
    
    return result

print(separate_letters_and_numbers("ABC123"))
print(separate_letters_and_numbers("Route66"))
print(separate_letters_and_numbers("H3LL0W0RLD"))
print(separate_letters_and_numbers("a1b2c3d4"))

# Comments - a bit more convoluted than previous examples. But by carefully tracking the last character type, it's not too hard