# SCREAMING_SNAKE_CASE

# Given a string representing a variable name, return the variable name converted to SCREAMING_SNAKE_CASE.

# The given variable names will be written in one of the following formats:

#     camelCase
#     PascalCase
#     snake_case
#     kebab-case

# In the above formats, words are separated by an underscore (_), a hyphen (-), or a new word starts with a capital letter.

# To convert to SCREAMING_SNAKE_CASE:

#     Make all letters uppercase
#     Separate words with an underscore (_)

# Tests

# 1. to_screaming_snake_case("userEmail") should return "USER_EMAIL".
# 2. to_screaming_snake_case("UserPassword") should return "USER_PASSWORD".
# 3. to_screaming_snake_case("user_id") should return "USER_ID".
# 4. to_screaming_snake_case("user-address") should return "USER_ADDRESS".
# 5. to_screaming_snake_case("username") should return "USERNAME".

def to_screaming_snake_case(variable_name):
    result = ""
    for char, i in zip(variable_name, range(len(variable_name))):
        if i == 0:
            result += char.upper()
        elif char.islower():
            result += char.upper()
        elif char.isupper():
            result += "_" + char
        else:
            result += "_"
    return result

print(to_screaming_snake_case("userEmail"))
print(to_screaming_snake_case("UserPassword"))
print(to_screaming_snake_case("user_id"))
print(to_screaming_snake_case("user-address"))
print(to_screaming_snake_case("username"))

# Comments - more annoying than difficult