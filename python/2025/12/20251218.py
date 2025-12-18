# Checkerboard

# Given an array with two numbers, the first being the number of rows and the second being the number of columns, return a matrix (an array of arrays) filled with "X" and "O" characters of the given size.

#     The characters should alternate like a checkerboard.
#     The top-left cell must always be "X".

# For example, given [3, 3], return:

# [
#   ["X", "O", "X"],
#   ["O", "X", "O"],
#   ["X", "O", "X"]
# ]

# Tests

# 1. create_board([3, 3]) should return [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]].
# 2. create_board([6, 1]) should return [["X"], ["O"], ["X"], ["O"], ["X"], ["O"]].
# 3. create_board([2, 10]) should return [["X", "O", "X", "O", "X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X", "O", "X", "O", "X"]].
# 4. create_board([5, 4]) should return [["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"]].

def create_board(dimensions):
    row, column = dimensions[0], dimensions[1]
    board = []
    for i in range(row):
        board.append([])
        for j in range(column):
            if (i + j) % 2 == 0:
                board[i].append("X")
            else:
                board[i].append("O")
    return board

print(create_board([3, 3]))
print(create_board([6, 1]))
print(create_board([2, 10]))
print(create_board([5, 4]))

# Comments - pretty straightforward. First we destructure the array into rows and columns. Then we iterate through the rows and columns and add the characters to the board
# The rule is quite easy, if it's an even position (row + column) we add an "X", else we add an "O"