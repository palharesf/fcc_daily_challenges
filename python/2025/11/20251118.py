# 100 Characters

# Welcome to the 100th Daily Coding Challenge!

# Given a string, repeat its characters until the result is exactly 100 characters long. If your repetitions go over 100 characters, trim the extra so it's exactly 100.
# Tests

# 1. one_hundred("One hundred ") should return "One hundred One hundred One hundred One hundred One hundred One hundred One hundred One hundred One ".
# 2. one_hundred("freeCodeCamp ") should return "freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeC".
# 3. one_hundred("daily challenges ") should return "daily challenges daily challenges daily challenges daily challenges daily challenges daily challenge".
# 4. one_hundred("!") should return "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!".

def one_hundred(chars):
    string = ""
    while len(string) < 100:
        string += chars
    string = string[:100]
    return string

one_hundred("One hundred ")
one_hundred("freeCodeCamp ")
one_hundred("daily challenges ")
one_hundred("!")

# Comments - very elegant exercise
# Initializing an empty string, looping and appending characters and finally trimming the result sounds easy, but I doubt it's something I would have thought when I started programming