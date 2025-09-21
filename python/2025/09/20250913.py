# Missing Numbers

# Given an array of integers from 1 to n, inclusive, return an array of all the missing integers between 1 and n (where n is the largest number in the given array).

#     The given array may be unsorted and may contain duplicates.
#     The returned array should be in ascending order.
#     If no integers are missing, return an empty array.

# Tests

# 1. find_missing_numbers([1, 3, 5]) should return [2, 4].
# 2. find_missing_numbers([1, 2, 3, 4, 5]) should return [].
# 3. find_missing_numbers([1, 10]) should return [2, 3, 4, 5, 6, 7, 8, 9].
# 4. find_missing_numbers([10, 1, 10, 1, 10, 1]) should return [2, 3, 4, 5, 6, 7, 8, 9].
# 5. find_missing_numbers([3, 1, 4, 1, 5, 9]) should return [2, 6, 7, 8].
# 6. find_missing_numbers([1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 6, 8, 9, 3, 2, 10, 7, 4]) should return [11].


def find_missing_numbers(arr):
    # Initial setup
    smallest = min(arr)
    largest = max(arr)
    # print(smallest, largest)

    # Creating key sets
    full_set = set(range(smallest, largest + 1))
    given_set = set(arr)

    # Sort and remove duplicates
    arr = sorted(list(full_set - given_set))

    return arr


find_missing_numbers([1, 3, 5])
find_missing_numbers([1, 2, 3, 4, 5])
find_missing_numbers([1, 10])
find_missing_numbers([10, 1, 10, 1, 10, 1])
find_missing_numbers([3, 1, 4, 1, 5, 9])
find_missing_numbers([1, 2, 3, 4, 5, 7, 8])

# Comments: initial approach was more iterative, thinking about how to create a full list of numbers, sort the original list, remove duplicates, and then compare the two lists.
# But a set basically already does the sorting and removes duplicates for me, so the original approach was redundant and overly complicated. 
# The updated approach jumps straight into the key sets, and in one fell swoop finds the missing numbers. We then just need to place it in an array. Good reminder on the importance of sets.