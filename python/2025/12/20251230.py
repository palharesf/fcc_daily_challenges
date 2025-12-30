# Sum the String

# Given a string containing digits and other characters, return the sum of all numbers in the string.

#     Treat consecutive digits as a single number. For example, "13" counts as 13, not 1 + 3.
#     Ignore any non-digit characters.

# Tests

# 1. string_sum("3apples2bananas") should return 5.
# 2. string_sum("10cats5dogs2birds") should return 17.
# 3. string_sum("125344") should return 125344.
# 4. string_sum("a1b20c300") should return 321.
# 5. string_sum("a12b34c56d78e90f123g456h789i0j1k2l3m4n5") should return 1653.

def string_sum(s):
    new_s = []
    for char in s:
        if char.isdigit():
            new_s.append(char)
        else:
            new_s.append(" ")
    new_s = "".join(new_s).split(" ")

    sum = 0
    for i in range(len(new_s)):
        if new_s[i].isdigit():
            sum += int(new_s[i])
    return sum


print(string_sum("3apples2bananas"))
print(string_sum("10cats5dogs2birds"))
print(string_sum("125344"))
print(string_sum("a1b20c300"))
print(string_sum("a12b34c56d78e90f123g456h789i0j1k2l3m4n5"))

# Comments - not easy. Treating consecutive digits as a single number was a bit tricky, requiring the use of an array to store the first pass results
# Line 23 ( new_s = "".join(new_s).split(" ") ) was really challenging. It collapses the array into a string and then opens it into a list again, but now collapsing multi-digit numbers into a single number
# Not simple at all but it works surprisingly well