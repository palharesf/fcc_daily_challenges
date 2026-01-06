# vOwElcAsE

# Given a string, return a new string where all vowels are converted to uppercase and all other alphabetical characters are converted to lowercase.

#     Vowels are "a", "e", "i", "o", and "u" in any case.
#     Non-alphabetical characters should remain unchanged.

# Tests

# 1. vowel_case("vowelcase") should return "vOwElcAsE".
# 2. vowel_case("coding is fun") should return "cOdIng Is fUn".
# 3. vowel_case("HELLO, world!") should return "hEllO, wOrld!".
# 4. vowel_case("git cherry-pick") should return "gIt chErry-pIck".
# 5. vowel_case("HEAD~1") should return "hEAd~1".

def vowel_case(s):
    return ''.join([c.upper() if c.lower() in 'aeiou' else c.lower() for c in s])

print(vowel_case("vowelcase"))
print(vowel_case("coding is fun"))
print(vowel_case("HELLO, world!"))
print(vowel_case("git cherry-pick"))
print(vowel_case("HEAD~1"))

# Comments - pretty elegant solution. All inline, loop through chars in s, tell them to be upper if their lower version is a vowel, lower otherwise, joined by an initialized blank space