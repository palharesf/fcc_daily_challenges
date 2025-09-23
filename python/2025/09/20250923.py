# String Mirror

# Given two strings, determine if the second string is a mirror of the first.

#     A string is considered a mirror if it contains the same letters in reverse order.
#     Treat uppercase and lowercase letters as distinct.
#     Ignore all non-alphabetical characters.

# Tests

# 1. is_mirror("helloworld", "helloworld") should return False.
# 2. is_mirror("Hello World", "dlroW olleH") should return True.
# 3. is_mirror("RaceCar", "raCecaR") should return True.
# 4. is_mirror("RaceCar", "RaceCar") should return False.
# 5. is_mirror("Mirror", "rorrim") should return False.
# 6. is_mirror("Hello World", "dlroW-olleH") should return True.
# 7. is_mirror("Hello World", "!dlroW !olleH") should return True.

def is_mirror(str1, str2):

    # Remove non-alphabetical characters
    str1 = "".join([char for char in str1 if char.isalpha()])
    str2 = "".join([char for char in str2 if char.isalpha()])
    # print("Str1: ", str1, "Str2: ", str2)

    # Compare lengths
    if len(str1) != len(str2):
        print("False")
        return False
    
    # Compare char by char    
    for i in range(len(str1)):
        if str1[i] != str2[len(str2) - 1 - i]:
            print("False")
            return False
    print("True")
    return True


is_mirror("helloworld", "helloworld")
is_mirror("Hello World", "dlroW olleH")
is_mirror("RaceCar", "raCecaR")
is_mirror("RaceCar", "RaceCar")
is_mirror("Mirror", "rorrim")
is_mirror("Hello World", "dlroW-olleH")
is_mirror("Hello World", "!dlroW !olleH")

# Comments: not super difficult, but harder than the last few challenges.
# The good thing is that the boundary conditions are easy to match. It could be more complicated if it started incorporating numbers or punctuation, for instance
# My initial approach was iterating over `char, i` in `str1` but I could not make it work
# The AI suggestion of simply iterating `i` over `range(len(str1))` was actually simpler and more direct, which I appreciated
# That said, the AI made things wrong and more difficult when comparing str1[i].islower() with str2[len(str2) - 1 - i].islower()
# Ignoring the .islower() method simple fixed it, so we can't rely too much on AI after all
# There was some cleaning prior to the comparison, but that was also straightforward