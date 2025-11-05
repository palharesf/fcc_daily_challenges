# Matrix Builder

# Given two integers (a number of rows and a number of columns), return a matrix (an array of arrays) filled with zeros (0) of the given size.

# For example, given 2 and 3, return:

# [
#   [0, 0, 0],
#   [0, 0, 0]
# ]

# Tests

# 1. build_matrix(2, 3) should return [[0, 0, 0], [0, 0, 0]].
# 2. build_matrix(3, 2) should return [[0, 0], [0, 0], [0, 0]].
# 3. build_matrix(4, 3) should return [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]].
# 4. build_matrix(9, 1) should return [[0], [0], [0], [0], [0], [0], [0], [0], [0]].

def build_matrix(rows, cols):
    return rows * [[0] * cols]

build_matrix(2, 3)
build_matrix(3, 2)
build_matrix(4, 3)
build_matrix(9, 1)

# Comments - one line solution. Actually zero line solution, since the return is implicit
# I would probably complicate it and get to the same result, but it's at least fascinating to see how simple the solution can be if done properly