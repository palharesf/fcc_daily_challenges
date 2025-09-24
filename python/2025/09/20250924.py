# Perfect Square

# Given an integer, determine if it is a perfect square.

#     A number is a perfect square if you can multiply an integer by itself to achieve the number. For example, 9 is a perfect square because you can multiply 3 by itself to get it.

# Tests

# 1. is_perfect_square(9) should return True.
# 2. is_perfect_square(49) should return True.
# 3. is_perfect_square(1) should return True.
# 4. is_perfect_square(2) should return False.
# 5. is_perfect_square(99) should return False.
# 6. is_perfect_square(-9) should return False.
# 7. is_perfect_square(0) should return True.
# 8. is_perfect_square(25281) should return True.

def is_perfect_square(n):

    # Prevent negatives
    if n < 0:
        return False
    
    # Calculate square root
    sqrt_n = n ** 0.5

    # Check if it's an integer
    if sqrt_n % 1 == 0:
        return True
    else:
        return False

is_perfect_square(9)
is_perfect_square(49)
is_perfect_square(1)
is_perfect_square(2)
is_perfect_square(99)
is_perfect_square(-9)
is_perfect_square(0)
is_perfect_square(25281)

# Comments: pretty straightforward problem. I started thinking about using a sqrt() function or method, but powering n to 0.5 is simpler and more reliable
# Handling negative cases is the only boundary condition that needs to be addressed separarely, assuming inputs are integers