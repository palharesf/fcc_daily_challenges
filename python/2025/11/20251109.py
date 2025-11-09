# Word Search

# Given a matrix (an array of arrays) of single letters and a word to find, return the start and end indices of the word in the matrix.

#     The given matrix will be filled with all lowercase letters (a-z).
#     The word to find will always be in the matrix exactly once.
#     The word to find will always be in a straight line in one of these directions:
#         left to right
#         right to left
#         top to bottom
#         bottom to top

# For example, given the matrix:

# [
#   ["a", "c", "t"],
#   ["t", "a", "t"],
#   ["c", "t", "c"]
# ]

# And the word "cat", return:

# [[0, 1], [2, 1]]

# Where [0, 1] are the indices for the "c" (start of the word), and [2, 1] are the indices for the "t" (end of the word).
# Tests

# 1. find_word([["a", "c", "t"], ["t", "a", "t"], ["c", "t", "c"]], "cat") should return [[0, 1], [2, 1]].
# 2. find_word([["d", "o", "g"], ["o", "g", "d"], ["d", "g", "o"]], "dog") should return [[0, 0], [0, 2]].
# 3. find_word([["h", "i", "s", "h"], ["i", "s", "f", "s"], ["f", "s", "i", "i"], ["s", "h", "i", "f"]], "fish") should return [[3, 3], [0, 3]].
# 4. find_word([["f", "x", "o", "x"], ["o", "x", "o", "f"], ["f", "o", "f", "x"], ["f", "x", "x", "o"]], "fox") should return [[1, 3], [1, 1]].

def find_word(matrix, word):

    # Create helper variable: a directions array
    directions = [
        (0, 1),  # right
        (0, -1),  # left
        (1, 0),  # down
        (-1, 0),  # up
    ]
    
    # Create two for loops that ensure we will search all the elements of the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Check if the first letter of the word is the same as the letter in the matrix
            if matrix[i][j] == word[0]:
                # Once the first letter has been found, search the rest of the word around it
                # dr and dc are delta row and delta column, showing the direction of the vector we'll be searching
                # So we loop it four times, searching for the full word in each direction
                # e.g. if dr = 0, dc = 1, we're searching for the word "cat" in the left-to-right direction
                for dr, dc in directions:
                    result = search_from(i, j, dr, dc, word, matrix)
                    if result:
                        return result

def search_from(row, col, dr, dc, word, matrix):
        
        rows = len(matrix)
        cols = len(matrix[0])

        end_row = row + dr * (len(word) - 1)
        end_col = col + dc * (len(word) - 1)
        
        # Check if end position is within bounds
        if not (0 <= end_row < rows and 0 <= end_col < cols):
            return None
        
        # Check if all letters match
        for i, char in enumerate(word):
            r = row + dr * i
            c = col + dc * i
            if matrix[r][c] != char:
                return None
        
        return [[row, col], [end_row, end_col]]

find_word([["a", "c", "t"], ["t", "a", "t"], ["c", "t", "c"]], "cat")
find_word([["d", "o", "g"], ["o", "g", "d"], ["d", "g", "o"]], "dog")
find_word([["h", "i", "s", "h"], ["i", "s", "f", "s"], ["f", "s", "i", "i"], ["s", "h", "i", "f"]], "fish")
find_word([["f", "x", "o", "x"], ["o", "x", "o", "f"], ["f", "o", "f", "x"], ["f", "x", "x", "o"]], "fox")

# Comments - not too tricky once it's solved and one is able to visualize the problem, but thinking it through and translating it to code was pretty hard
# Had to resort to Claude for this one. The visual representation helped a lot: https://claude.ai/share/d51098b7-4023-487d-89d4-fbac0934e041

# **Visual representation:**
# ```
#      col: 0   1   2
# row 0:  [a] [c] [t]  ← start here (0,1), looking for 'c'
# row 1:  [t] [a] [t]  ← move down (1,1), looking for 'a'
# row 2:  [c] [t] [c]  ← move down (2,1), looking for 't'
# ```

# **What it does:**
# - `i` is the position in the word (0, 1, 2...)
# - `char` is the character we're looking for at that position
# - `r = row + dr * i` calculates which row to check (start + direction × steps)
# - `c = col + dc * i` calculates which column to check
# - If any character doesn't match, return `None` (word not found in this direction)