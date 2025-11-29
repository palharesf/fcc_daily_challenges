# Ball Trajectory

# Today's challenge is inspired by the video game Pong, which was released November 29, 1972.

# Given a matrix (array of arrays) that includes the location of the ball (2), and the previous location of the ball (1), return the matrix indices for the next location of the ball.

#     The ball always moves in a straight line.
#     The movement direction is determined by how the ball moved from 1 to 2.
#     The edges of the matrix are considered walls. If the balls hits a:
#         top or bottom wall, it bounces by reversing its vertical direction.
#         left or right wall, it bounces by reversing its horizontal direction.
#         corner, it bounces by reversing both directions.

# Tests

# 1. get_next_location([[0,0,0,0], [0,0,0,0], [0,1,2,0], [0,0,0,0]]) should return [2, 3].
# 2. get_next_location([[0,0,0,0], [0,0,1,0], [0,2,0,0], [0,0,0,0]]) should return [3, 0].
# 3. get_next_location([[0,2,0,0], [1,0,0,0], [0,0,0,0], [0,0,0,0]]) should return [1, 2].
# 4. get_next_location([[0,0,0,0], [0,0,0,0], [2,0,0,0], [0,1,0,0]]) should return [1, 1].
# 5. get_next_location([[0,0,0,0], [0,0,0,0], [0,0,1,0], [0,0,0,2]]) should return [2, 2].

def get_next_location(matrix):
    
    # Get the size of the matrix as helper variables
    rows = len(matrix)
    cols = len(matrix[0])

    # Initialize the previous and current position tuples
    prev_pos = (0, 0)
    curr_pos = (0, 0)

    # Find the positions of 1 and 2 in the matrix
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                prev_pos = (i, j)
            elif matrix[i][j] == 2:
                curr_pos = (i, j)

    # Print the previous and current positions
    print(f'\nPrevious position: {prev_pos}')
    print(f'Current position: {curr_pos}')

    # Calculate the direction of movement
    dr, dc = curr_pos[0] - prev_pos[0], curr_pos[1] - prev_pos[1]
    print(f'Direction: ({dr}, {dc})')

    # Calculate boundary collisions and update direction if necessary
    if curr_pos[0] == 0 or curr_pos[0] == rows - 1 or curr_pos[1] == 0 or curr_pos[1] == cols - 1:
        if curr_pos[0] == 0 or curr_pos[0] == rows - 1:
            dr = -dr
        if curr_pos[1] == 0 or curr_pos[1] == cols - 1:
            dc = -dc

    # Handle corner case
    else:
        if curr_pos[0] + dr < 0 or curr_pos[0] + dr >= rows:
            dr = -dr
        if curr_pos[1] + dc < 0 or curr_pos[1] + dc >= cols:
            dc = -dc

    # Update the current position in the return statement
    return [curr_pos[0] + dr, curr_pos[1] + dc]

print(get_next_location([[0,0,0,0], [0,0,0,0], [0,1,2,0], [0,0,0,0]]))  # should return [2, 3]
print(get_next_location([[0,0,0,0], [0,0,1,0], [0,2,0,0], [0,0,0,0]]))  # should return [3, 0]
print(get_next_location([[0,2,0,0], [1,0,0,0], [0,0,0,0], [0,0,0,0]]))  # should return [1, 2]
print(get_next_location([[0,0,0,0], [0,0,0,0], [2,0,0,0], [0,1,0,0]]))  # should return [1, 1]
print(get_next_location([[0,0,0,0], [0,0,0,0], [0,0,1,0], [0,0,0,2]]))  # should return [2, 2]

# Comments: besides the corner case, all other collision and calculations are pretty straightforward, although having to work in a matrix fashion is always made more difficuly by nested loops