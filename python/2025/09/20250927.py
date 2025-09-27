# Spam Detector

# Given a phone number in the format "+A (BBB) CCC-DDDD", where each letter represents a digit as follows:

#     A represents the country code and can be any number of digits.
#     BBB represents the area code and will always be three digits.
#     CCC and DDDD represent the local number and will always be three and four digits long, respectively.

# Determine if it's a spam number based on the following criteria:

#     The country code is greater than 2 digits long or doesn't begin with a zero (0).
#     The area code is greater than 900 or less than 200.
#     The sum of first three digits of the local number appears within last four digits of the local number.
#     The number has the same digit four or more times in a row (ignoring the formatting characters).

# Tests

# 1. is_spam("+0 (200) 234-0182") should return False.
# 2. is_spam("+091 (555) 309-1922") should return True.
# 3. is_spam("+1 (555) 435-4792") should return True.
# 4. is_spam("+0 (955) 234-4364") should return True.
# 5. is_spam("+0 (155) 131-6943") should return True.
# 6. is_spam("+0 (555) 135-0192") should return True.
# 7. is_spam("+0 (555) 564-1987") should return True.
# 8. is_spam("+00 (555) 234-0182") should return False.

def is_spam(number):

    # Split the number into parts
    number = number.replace("-", " ")
    parts = number.split()

    # Remove unwanted characters
    parts[0] = parts[0].replace("+", "")
    parts[1] = parts[1].replace("(", "")
    parts[1] = parts[1].replace(")", "")
    # print(parts)

    # Check if the country code is greater than 2 digits long or doesn't begin with a zero
    if len(parts[0]) > 2 or parts[0][0] != '0':
        print("True - Country Code")
        return True

    # Check if the area code is greater than 900 or less than 200
    if int(parts[1][0:3]) > 900 or int(parts[1][0:3]) < 200:
        print("True - Area Code Outside Range")
        return True

    # Check if the sum of first three digits of the local number appears within last four digits of the local number
    local_sum = sum(int(digit) for digit in parts[2][0:3])
    for digit in parts[3]:
        if int(digit) == local_sum:
            print("True - Local Sum in Last Four Digits")
            return True
    
    # Check if the number has the same digit four or more times in a row
    long_number = parts[0] + parts[1] + parts[2] + parts[3]
    # print(long_number)
    for i in range(len(long_number) - 3):
        if int(long_number[i]) == int(long_number[i+1]) == int(long_number[i+2]) == int(long_number[i+3]):
            print("True - Same Digit 4 or More Times in a Row")
            return True

    print(False)
    return False

is_spam("+0 (200) 234-0182")
is_spam("+091 (555) 309-1922")
is_spam("+1 (555) 435-4792")
is_spam("+0 (955) 234-4364")
is_spam("+0 (155) 131-6943")
is_spam("+0 (555) 135-0192")
is_spam("+0 (555) 564-1987")
is_spam("+00 (555) 234-0182")

# Comments - slightly more difficult than previous challenges, but still very doable
# I assumed I would have to use Regex at some point, but gladly the verifications were simple enough that it was not necessary
# It was actually interesting to manipulate the numbers for each verification, nad breaking down the problems into smaller chunks made it more manageable
# Iterating over the long number and manipulating whether it was a string or int was a good wrench in the works