# Par for the Hole

# Given two integers, the par for a golf hole and the number of strokes a golfer took on that hole, return the golfer's score using golf terms.

# Return:

#     "Hole in one!" if it took one stroke.
#     "Eagle" if it took two strokes less than par.
#     "Birdie" if it took one stroke less than par.
#     "Par" if it took the same number of strokes as par.
#     "Bogey" if it took one stroke more than par.
#     "Double bogey" if took two strokes more than par.

# Tests

# 1. golf_score(3, 3) should return "Par".
# 2. golf_score(4, 3) should return "Birdie".
# 3. golf_score(3, 1) should return "Hole in one!".
# 4. golf_score(5, 7) should return "Double bogey".
# 5. golf_score(4, 5) should return "Bogey".
# 6. golf_score(5, 3) should return "Eagle".

def golf_score(par, strokes):
    if strokes == 1:
        return "Hole in one!"
    elif strokes == par - 2:
        return "Eagle"
    elif strokes == par - 1:
        return "Birdie"
    elif strokes == par:
        return "Par"
    elif strokes == par + 1:
        return "Bogey"
    elif strokes == par + 2:
        return "Double bogey"

print(golf_score(3, 3))
print(golf_score(4, 3))
print(golf_score(3, 1))
print(golf_score(5, 7))
print(golf_score(4, 5))
print(golf_score(5, 3))

# Extremely simple conditional