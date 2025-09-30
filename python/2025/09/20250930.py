# Phone Number Formatter

# Given a string of ten digits, return the string as a phone number in this format: "+D (DDD) DDD-DDDD".
# Tests

# 1. format_number("05552340182") should return "+0 (555) 234-0182".
# 2. format_number("15554354792") should return "+1 (555) 435-4792".

def format_number(number):
    formatted_number = f"+{number[0]} ({number[1:4]}) {number[4:7]}-{number[7:]}"
    # print(formatted_number)
    return formatted_number

format_number("05552340182")
format_number("15554354792")

# Comments - one line solution. Not challenging at all but always good to practice some f-string