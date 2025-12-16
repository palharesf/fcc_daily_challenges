# Consonant Count

# Given a string and a target number, determine whether the string contains exactly the target number of consonants.

#     Consonants are all alphabetic characters except "a", "e", "i", "o", and "u" in any case.
#     Ignore digits, punctuation, spaces, and other non-letter characters when counting.

# Tests

# 1. has_consonant_count("helloworld", 7) should return True.
# 2. has_consonant_count("eieio", 5) should return False.
# 3. has_consonant_count("freeCodeCamp Rocks!", 11) should return True.
# 4. has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 24) should return False.
# 5. has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 23) should return True.

def has_consonant_count(text, target):
    count = 0
    for char in text:
        if char.isalpha() and char.lower() not in "aeiou":
            count += 1
    return count == target

print(has_consonant_count("helloworld", 7))
print(has_consonant_count("eieio", 5))
print(has_consonant_count("freeCodeCamp Rocks!", 11))
print(has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 24))
print(has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 23))

# Comments - standard implementation. Checking if it's alpha and not a vowel, followed by a simple check against the target