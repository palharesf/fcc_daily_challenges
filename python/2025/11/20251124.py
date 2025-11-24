# Message Validator

# Given a message string and a validation string, determine if the message is valid.

#     A message is valid if each word in the message starts with the corresponding letter in the validation string, in order.
#     Letters are case-insensitive.
#     Words in the message are separated by single spaces.

# Tests

# 1. is_valid_message("hello world", "hw") should return True.
# 2. is_valid_message("ALL CAPITAL LETTERS", "acl") should return True.
# 3. is_valid_message("Coding challenge are boring.", "cca") should return False.
# 4. is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLD") should return True.
# 5. is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLDT") should return False.

def is_valid_message(message, validation):

    message = message.lower().split()
    validation = validation.lower()

    if len(message) != len(validation):
        return False

    for i in range(len(message)):
        if message[i][0] != validation[i]:
            return False
        
    return True

print(is_valid_message("hello world", "hw"))
print(is_valid_message("ALL CAPITAL LETTERS", "acl"))
print(is_valid_message("Coding challenge are boring.", "cca"))
print(is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLD"))
print(is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLDT"))

# Comments - kind of an okay challenge. Not too tough but also not too obvious
# The logical answer is kind of clear but takes some effort to implement and test. I enjoyed it