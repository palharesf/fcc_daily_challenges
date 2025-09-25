# 2nd Largest

# Given an array, return the second largest distinct number.
# Tests

# 1. second_largest([1, 2, 3, 4]) should return 3.
# 2. second_largest([20, 139, 94, 67, 31]) should return 94.
# 3. second_largest([2, 3, 4, 6, 6]) should return 4.
# 4. second_largest([10, -17, 55.5, 44, 91, 0]) should return 55.5.
# 5. second_largest([1, 0, -1, 0, 1, 0, -1, 1, 0]) should return 0.

def second_largest(arr):

    arr = sorted(arr)
    
    while(arr[-1] == arr[-2]):
        arr.pop()

    # print(arr[-2])
    return arr[-2]

second_largest([1, 2, 3, 4])
second_largest([20, 139, 94, 67, 31])
second_largest([2, 3, 4, 6, 6])
second_largest([10, -17, 55.5, 44, 91, 0])
second_largest([1, 0, -1, 0, 1, 0, -1, 1, 0])

# Comments: the AI suggested using the sorted method on the array immediately, which pretty much solves the challenge. I had originally intended to sort the array manually with a for statement comparing element by element, but this is much better
# The main concern I had was creating an infinite loop on the while statement to keep only distinct numbers at the end of the array, but I was convinced by the AI that the way the loop was crafted won't risk an infinite