# Signature Validation

# Given a message string, a secret key string, and a signature number, determine if the signature is valid using this encoding method:

#     Letters in the message and secret key have these values:
#         a to z have values 1 to 26 respectively.
#         A to Z have values 27 to 52 respectively.
#     All other characters have no value.
#     Compute the signature by taking the sum of the message plus the sum of the secret key.

# For example, given the message "foo" and the secret key "bar", the signature would be 57:

# f (6) + o (15) + o (15) = 36
# b (2) + a (1) + r (18) = 21
# 36 + 21 = 57

# Check if the computed signature matches the provided signature.
# Tests

# 1. verify("foo", "bar", 57) should return True.
# 2. verify("foo", "bar", 54) should return False.
# 3. verify("freeCodeCamp", "Rocks", 238) should return True.
# 4. verify("Is this valid?", "No", 210) should return False.
# 5. verify("Is this valid?", "Yes", 233) should return True.
# 6. verify("Check out the freeCodeCamp podcast,", "in the mobile app", 514) should return True.

def verify(message, key, signature):
    message_sum = 0
    key_sum = 0

    for char in message:
        if char.isalpha():
            if char.islower():
                value = ord(char) - 96
            else:
                value = ord(char) - 64 + 26
            message_sum += value
        else:
            message_sum += 0

    for char in key:
        if char.isalpha():
            if char.islower():
                value = ord(char) - 96
            else:
                value = ord(char) - 64 + 26
            key_sum += value
        else:
            key_sum += 0

    if message_sum + key_sum == signature:
        return True
    else:
        return False

verify("foo", "bar", 57)
verify("foo", "bar", 54)
verify("freeCodeCamp", "Rocks", 238)
verify("Is this valid?", "No", 210)
verify("Is this valid?", "Yes", 233)
verify("Check out the freeCodeCamp podcast,", "in the mobile app", 514)

# Comments - the trick here is knowing about ASCII subtraction, which I didn't. With these values readily available, it's not a difficult challenge