# SpOoKy~CaSe

# Given a string representing a variable name, convert it to "spooky case" using the following constraints:

#     Replace all underscores (_), and hyphens (-) with a tilde (~).
#     Capitalize the first letter of the string, and every other letter after that, ignore the tilde character when counting.

# For example, given hello_world, return HeLlO~wOrLd.
# Tests

# 1. spookify("hello_world") should return "HeLlO~wOrLd".
# 2. spookify("Spooky_Case") should return "SpOoKy~CaSe".
# 3. spookify("TRICK-or-TREAT") should return "TrIcK~oR~tReAt".
# 4. spookify("c_a-n_d-y_-b-o_w_l") should return "C~a~N~d~Y~~b~O~w~L".
# 5. spookify("thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts") should return "ThE~hAuNtEd~HoUsE~iS~fUlL~oF~gHoStS".

def spookify(boo):
    boo = boo.replace("_", "~").replace("-", "~")
    char_index = 1
    for i, char in enumerate(boo):
        if char.isalpha():
            char_index += 1
            if char_index % 2 == 0:
                boo = boo[:i] + char.upper() + boo[i + 1 :]
            else:
                boo = boo[:i] + char.lower() + boo[i + 1 :]
    return boo

spookify("hello_world")
spookify("Spooky_Case")
spookify("TRICK-or-TREAT")
spookify("c_a-n_d-y_-b-o_w_l")
spookify("thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts")

# Comments: not super difficult, although the syntax can be a bit finnicky
# The idea of having an external index counting up only when it finds a letter is a good way around the tildes
# Thinking of it was not the hard part - the issue was that I usually loop `for char in boo`, whereas the proper way of looping here is `for i, char in enumerate(boo)`