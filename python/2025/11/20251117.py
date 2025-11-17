# Fingerprint Test

# Given two strings representing fingerprints, determine if they are a match using the following rules:

#     Each fingerprint will consist only of lowercase letters (a-z).
#     Two fingerprints are considered a match if:
#         They are the same length.
#         The number of differing characters does not exceed 10% of the fingerprint length.

# Tests

# 1. is_match("helloworld", "helloworld") should return True.
# 2. is_match("helloworld", "helloworlds") should return False.
# 3. is_match("helloworld", "jelloworld") should return True.
# 4. is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthelazydog") should return True.
# 5. is_match("theslickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazydog") should return True.
# 6. is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazycat") should return False.

def is_match(fingerprint_a, fingerprint_b):
    if (len(fingerprint_a) != len(fingerprint_b)):
        return False
    
    diff = 0
    for i in range(len(fingerprint_a)):
        if (fingerprint_a[i] != fingerprint_b[i]):
            diff += 1
        if (diff > len(fingerprint_a) * 0.1):
            return False
        
    return True

is_match("helloworld", "helloworld")
is_match("helloworld", "helloworlds")
is_match("helloworld", "jelloworld")
is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthelazydog")
is_match("theslickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazydog")
is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazycat")

# Comments: straighforward but enjoyable exercise
# The two checks are easy to implement individually and not super difficult to think about, making implementation straightforward and fun to write