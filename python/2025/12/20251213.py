# Game of Life

# Given a matrix (array of arrays) representing the current state in Conway's Game of Life, return the next state of the matrix using these rules:

#     Each cell is either 1 (alive) or 0 (dead).
#     A cell's neighbors are the up to eight surrounding cells (vertically, horizontally, and diagonally).
#     Cells on the edges have fewer than eight neighbors.

# Rules for updating each cell:

#     Any live cell with fewer than two live neighbors dies (underpopulation).
#     Any live cell with two or three live neighbors lives on.
#     Any live cell with more than three live neighbors dies (overpopulation).
#     Any dead cell with exactly three live neighbors becomes alive (reproduction).

# For example, given:

# [
#   [0, 1, 0],
#   [0, 1, 1],
#   [1, 1, 0]
# ]

# return:

# [
#   [0, 1, 1],
#   [0, 0, 1],
#   [1, 1, 1]
# ]

# Each cell updates according to the number of live neighbors. For instance, [0][0] stays dead (2 live neighbors), [0][1] stays alive (2 live neighbors), [0][2] dies (3 live neighbors), and so on.
# Tests

# 1. game_of_life([[0, 1, 0], [0, 1, 1], [1, 1, 0]]) should return [[0, 1, 1], [0, 0, 1], [1, 1, 1]].
# 2. game_of_life([[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 1, 0]]) should return [[1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 1, 1, 1]].
# 3. game_of_life([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) should return [[0, 0, 0], [0, 1, 0], [0, 0, 0]].
# 4. game_of_life([[0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0]]) should return [[1, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]].

def game_of_life(grid):
    # Initialize the new grid
    new_grid = []
    for row in range(len(grid)):
        new_row = []
        for col in range(len(grid[0])):

            # Calculate the number of live neighbors for each cell
            neighbors = find_neighbors(grid, row, col)

            # If it's alive, kills it from overpopulation or underpopulation, or stays alive
            if grid[row][col] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_row.append(0)
                else:
                    new_row.append(1)

            # If it's dead, becomes alive from reproduction, or stays dead
            else:
                if neighbors == 3:
                    new_row.append(1)
                else:
                    new_row.append(0)
        new_grid.append(new_row)
    return new_grid

def find_neighbors(grid, row, col):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    count = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            # Skip the cell itself
            if i == 0 and j == 0:
                continue

            # Calculate neighbor coordinates
            neighbor_row = row + i
            neighbor_col = col + j

            # Check if neighbor is within grid boundaries
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                if grid[neighbor_row][neighbor_col] == 1:
                    count += 1

    return count

print(game_of_life([[0, 1, 0], [0, 1, 1], [1, 1, 0]]))
print(game_of_life([[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 1, 0]]))
print(game_of_life([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
print(game_of_life([[0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0]]))

# Comments: tricky challenge. The hardest part is defining the neighbors function, which required a bit of extra work to calculate boundaries correctly
# Once that's done, the main function is pretty straightforward, just checking for logical conditions