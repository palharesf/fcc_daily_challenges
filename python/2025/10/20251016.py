# Email Validator

# Given a string, determine if it is a valid email address using the following constraints:

#     It must contain exactly one @ symbol.
#     The local part (before the @):
#         Can only contain letters (a-z, A-Z), digits (0-9), dots (.), underscores (_), or hyphens (-).
#         Cannot start or end with a dot.
#     The domain part (after the @):
#         Must contain at least one dot.
#         Must end with a dot followed by at least two letters.
#     Neither the local or domain part can have two dots in a row.

# Tests

# 1. validate("a@b.cd") should return True.
# 2. validate("hell.-w.rld@example.com") should return True.
# 3. validate(".b@sh.rc") should return False.
# 4. validate("example@test.c0") should return False.
# 5. validate("freecodecamp.org") should return False.
# 6. validate("develop.ment_user@c0D!NG.R.CKS") should return True.
# 7. validate("hello.@wo.rld") should return False.
# 8. validate("hello@world..com") should return False.
# 9. validate("git@commit@push.io") should return False.

def validate(email):
    print("")
    print(email)

    # At Part
    if email.count("@") != 1:
        print("FAILED: Multiple (or none) @ symbols")
        return False

    # Local Part
    dot_index = email.index("@") + 1
    if email[0] == "." or email[email.find("@") - 1] == ".":
        print("FAILED: Dot at start or end of local part")
        return False
    
    for char in email[0:email.index("@")]:
        if not char.isalpha() and not char.isdigit() and not char == "_" and not char == "-" and not char == ".":
            print("FAILED: Invalid character in local part")
            return False

    # Domain Part
    if email[dot_index:].count(".") < 1:
        print("FAILED: Less than one dot in the domain part")
        return False
    
    last_dot_index = email[dot_index:].rfind(".")
    if (
        len(email[dot_index + last_dot_index + 1 :]) < 2 or
        not email[dot_index + last_dot_index + 1 :].isalpha()
    ):
        print("FAILED: Less than two letters after the last dot in the domain part")
        return False
            
    # Two Dots
    for i in range(len(email) - 1):
        if email[i] == "." and email[i+1] == ".":
            print("FAILED: Two dots in a row")
            return False
        
    print("PASSED")
    return True

validate("a@b.cd")
validate("hell.-w.rld@example.com")
validate(".b@sh.rc")
validate("example@test.c0")
validate("freecodecamp.org")
validate("develop.ment_user@c0D!NG.R.CKS")
validate("hello.@wo.rld")
validate("hello@world..com")
validate("git@commit@push.io")

# Comments: really tough challenge. There are multiple rules to follow.
# The good thing about it is that we can check each rule individually
# The tricky part is that some of those rules are tricky to check, even individually
# I pretty much gave up on the rule "Less than two letters after the last dot in the domain part" since it was consuming too much time
# I don't think this is a tight exercise and that it works so well as a learning tool. It's hard to point at what I do better now that I've done it versus before doing it