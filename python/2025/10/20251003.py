# P@ssw0rd Str3ngth!

# Given a password string, return "weak", "medium", or "strong" based on the strength of the password.

# A password is evaluated according to the following rules:

#     It is at least 8 characters long.
#     It contains both uppercase and lowercase letters.
#     It contains at least one number.
#     It contains at least one special character from this set: !, @, #, $, %, ^, &, or *.

# Return "weak" if the password meets fewer than two of the rules. Return "medium" if the password meets 2 or 3 of the rules. Return "strong" if the password meets all 4 rules.
# Tests

# 1. check_strength("123456") should return "weak".
# 2. check_strength("pass!!!") should return "weak".
# 3. check_strength("Qwerty") should return "weak".
# 4. check_strength("PASSWORD") should return "weak".
# 5. check_strength("PASSWORD!") should return "medium".
# 6. check_strength("PassWord%^!") should return "medium".
# 7. check_strength("qwerty12345") should return "medium".
# 8. check_strength("PASSWORD!") should return "medium".
# 9. check_strength("PASSWORD!") should return "medium".
# 10. check_strength("S3cur3P@ssw0rd") should return "strong".
# 11. check_strength("C0d3&Fun!") should return "strong".

def check_strength(password):
    rating = 0
    result = ""

    if len(password) >= 8:
        rating += 1
    if any(char.isupper() for char in password):
        if any(char.islower() for char in password):
            rating += 1
    if any(char.isdigit() for char in password):
        rating += 1
    if any(char in "!@#$%^&*" for char in password):
        rating += 1

    if rating < 2:
        # print("weak")
        result = "weak"
    elif rating < 4:
        # print("medium")
        result = "medium"
    else:
        # print("strong")
        result = "strong"
    return result

check_strength("123456")
check_strength("pass!!!")
check_strength("Qwerty")
check_strength("PASSWORD")
check_strength("PASSWORD!")
check_strength("PassWord%^!")
check_strength("qwerty12345")
check_strength("PASSWORD!")
check_strength("PASSWORD!")
check_strength("S3cur3P@ssw0rd")
check_strength("C0d3&Fun!")

# Comments - straighforward yet enjoyable exercise. Two key tricks here were using empty variables at the beginning to track the password rating and it's final result, and using the 'any' function to check for multiple conditions
# We loop to define a rating, then loop to attribute that rating to a final result