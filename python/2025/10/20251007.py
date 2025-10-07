# Space Week Day 4: Landing Spot

# In day four of Space Week, you are given a matrix of numbers (an array of arrays), representing potential landing spots for your rover.
# Find the safest landing spot based on the following rules:

#     Each spot in the matrix will contain a number from 0-9, inclusive.
#     Any 0 represents a potential landing spot.
#     Any number other than 0 is too dangerous to land. The higher the number, the more dangerous.
#     The safest spot is defined as the 0 cell whose surrounding cells (up to 4 neighbors, ignore diagonals) have the lowest total danger.
#     Ignore out-of-bounds neighbors (corners and edges just have fewer neighbors).
#     Return the indices of the safest landing spot. There will always only be one safest spot.

# For instance, given:

# [
#   [1, 0],
#   [2, 0]
# ]

# Return [0, 1], the indices for the 0 in the first array.
# Tests

# 1. find_landing_spot([[1, 0], [2, 0]]) should return [0, 1].
# 2. find_landing_spot([[9, 0, 3], [7, 0, 4], [8, 0, 5]]) should return [1, 1].
# 3. find_landing_spot([[1, 2, 1], [0, 0, 2], [3, 0, 0]]) should return [2, 2].
# 4. find_landing_spot([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]]) should return [2, 1].

def find_landing_spot(matrix):
    safest_position = None
    safest_risk_factor = float("inf")

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == 0:
                risk_factor = calculate_risk_factor(matrix, i, j)
                if risk_factor < safest_risk_factor:
                    safest_position = [i, j]
                    safest_risk_factor = risk_factor

    print(safest_position)
    return safest_position

def calculate_risk_factor(matrix, i, j):
    # Calculate the risk factor by summing up the values of its neighbors (up, down, left, right)
    risk_factor = 0
    if i > 0:
        risk_factor += matrix[i - 1][j]
    if i < len(matrix) - 1:
        risk_factor += matrix[i + 1][j]
    if j > 0:
        risk_factor += matrix[i][j - 1]
    if j < len(matrix[0]) - 1:
        risk_factor += matrix[i][j + 1]

    return risk_factor

find_landing_spot([[1, 0], [2, 0]])
find_landing_spot([[9, 0, 3], [7, 0, 4], [8, 0, 5]])
find_landing_spot([[1, 2, 1], [0, 0, 2], [3, 0, 0]])
find_landing_spot([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]])

# Comments - theoretically, the challenge is much harder than the previous ones. Understanding what needs to be done takes a while, but is mostly doable
# Where I really struggled was in properly looping through the matrix. I struggled with the `i, row in enumarate(matrix)` and the following `j, value in enumerate(row)`
# It makes sense, but is challenging to write properly in the first go
# The risk calculation was something I also considered moving to a separate function, but still, checking whether each addition is valid before performing it is something I failed to execute on my own
# Difficult to come up with the solution on my own, but explaining to the AI what I wanted took me all the way to the solution quite easily