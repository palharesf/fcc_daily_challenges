# Tic-Tac-Toe

# Given a 3×3 matrix (an array of arrays) representing a completed Tic-Tac-Toe game, determine the winner.

#     Each element in the given matrix is either an "X" or "O".

# A player wins if they have three of their characters in a row - horizontally, vertically, or diagonally.

# Return:

#     "X wins" if player X has three in a row.
#     "O wins" if player O has three in a row.
#     "Draw" if no player has three in a row.

# Tests

# 1. tic_tac_toe([["X", "X", "X"], ["O", "O", "X"], ["O", "X", "O"]]) should return "X wins".
# 2. tic_tac_toe([["X", "O", "X"], ["X", "O", "X"], ["O", "O", "X"]]) should return "O wins".
# 3. tic_tac_toe([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]) should return "Draw".
# 4. tic_tac_toe([["X", "X", "O"], ["X", "O", "X"], ["O", "X", "X"]]) should return "O wins".
# 5. tic_tac_toe([["X", "O", "O"], ["O", "X", "O"], ["O", "X", "X"]]) should return "X wins".
# 6. tic_tac_toe([["O", "X", "X"], ["X", "O", "O"], ["X", "O", "X"]]) should return "Draw".

def tic_tac_toe(board):
    if board[0][0] == board[0][1] == board[0][2]:
        if board[0][0] == "X":
            return "X wins"
        else:
            return "O wins"
    if board[1][0] == board[1][1] == board[1][2]:
        if board[1][0] == "X":
            return "X wins"
        else:
            return "O wins"
    if board[2][0] == board[2][1] == board[2][2]:
        if board[2][0] == "X":
            return "X wins"
        else:
            return "O wins"
    if board[0][0] == board[1][0] == board[2][0]:
        if board[0][0] == "X":
            return "X wins"
        else:
            return "O wins"
    if board[0][1] == board[1][1] == board[2][1]:
        if board[0][1] == "X":
            return "X wins"
        else:
            return "O wins"
    if board[0][2] == board[1][2] == board[2][2]:
        if board[0][2] == "X":
            return "X wins"
        else:
            return "O wins"
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "X":
            return "X wins"
        else:
            return "O wins"
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "X":
            return "X wins"
        else:
            return "O wins"
    else:
        return "Draw"

print(tic_tac_toe([["X", "X", "X"], ["O", "O", "X"], ["O", "X", "O"]]))
print(tic_tac_toe([["X", "O", "X"], ["X", "O", "X"], ["O", "O", "X"]]))
print(tic_tac_toe([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]))
print(tic_tac_toe([["X", "X", "O"], ["X", "O", "X"], ["O", "X", "X"]]))
print(tic_tac_toe([["X", "O", "O"], ["O", "X", "O"], ["O", "X", "X"]]))
print(tic_tac_toe([["O", "X", "X"], ["X", "O", "O"], ["X", "O", "X"]]))

# Comments - a trite challenge. Very little learning involved