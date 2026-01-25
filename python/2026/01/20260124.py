# Bingo! Letter

# Given a number, return the bingo letter associated with it (capitalized). Bingo numbers are grouped as follows:
# Letter 	Number Range
# "B" 	1-15
# "I" 	16-30
# "N" 	31-45
# "G" 	46-60
# "O" 	61-75
# Tests

# 1. get_bingo_letter(75) should return "O".
# 2. get_bingo_letter(54) should return "G".
# 3. get_bingo_letter(25) should return "I".
# 4. get_bingo_letter(38) should return "N".
# 5. get_bingo_letter(11) should return "11".

def get_bingo_letter(n):
    if n < 16:
        return "B"
    elif n < 31:
        return "I"
    elif n < 46:
        return "N"
    elif n < 61:
        return "G"
    elif n < 76:
        return "O"

print(get_bingo_letter(75))
print(get_bingo_letter(54))
print(get_bingo_letter(25))
print(get_bingo_letter(38))
print(get_bingo_letter(11))