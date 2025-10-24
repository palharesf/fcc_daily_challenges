# Hidden Treasure

# Given a 2D array representing a map of the ocean floor that includes a hidden treasure, and an array with the coordinates ([row, column]) for the next dive of your treasure search, return "Empty", "Found", or "Recovered" using the following rules:

#     The given 2D array will contain exactly one unrecovered treasure, which will occupy multiple cells.

#     Each cell in the 2D array will contain one of the following values:
#         "-": No treasure.
#         "O": A part of the treasure that has not been found.
#         "X": A part of the treasure that has already been found.

#     If the dive location has no treasure, return "Empty".

#     If the dive location finds treasure, but at least one other part of the treasure remains unfound, return "Found".

#     If the dive location finds the last unfound part of the treasure, return "Recovered".

# For example, given:

# [
#   [ "-", "X"],
#   [ "-", "X"],
#   [ "-", "O"]
# ]

# And [2, 1] for the coordinates of the dive location, return "Recovered" because the dive found the last unfound part of the treasure.
# Tests

# 1. dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 1]) should return "Recovered".
# 2. dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 0]) should return "Empty".
# 3. dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1]) should return "Found".
# 4. dive([[ "-", "-", "-"], [ "X", "O", "X"], [ "-", "-", "-"]], [1, 2]) should return "Found".
# 5. dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [2, 0]) should return "Recovered".
# 6. dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [1, 2]) should return "Empty".

def dive(map, coordinates):
    missing_parts = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "O":
                missing_parts += 1

    if map[coordinates[0]][coordinates[1]] == "O":
        if missing_parts == 1:
            print("Recovered")
            return "Recovered"
        else:
            print("Found")
            return "Found"
    elif map[coordinates[0]][coordinates[1]] == "X":
        print("Found")
        return "Found"
    else:
        print("Empty")
        return "Empty"

dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 1])
dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 0])
dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1])
dive([[ "-", "-", "-"], [ "X", "O", "X"], [ "-", "-", "-"]], [1, 2])
dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [2, 0])
dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [1, 2])

# Comments - somewhat straightforward exercise. Looking at the map is not too difficult. The snag was in checking if there were more than 1 treasure left in the map to define whether to display "Recovered" or "Found"