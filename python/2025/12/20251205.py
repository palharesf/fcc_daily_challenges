# Symmetric Difference

# Given two arrays, return a new array containing the symmetric difference of them.

#     The symmetric difference between two sets is the set of values that appear in either set, but not both.
#     Return the values in the order they first appear in the input arrays.

# Tests

# 1. difference([1, 2, 3], [3, 4, 5]) should return [1, 2, 4, 5].
# 2. difference(["a", "b"], ["c", "b"]) should return ["a", "c"].
# 3. difference([1, "a", 2], [2, "b", "a"]) should return [1, "b"].
# 4. difference([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]) should return [2, 4, 6, 8].

def difference(arr1, arr2):

    for item in arr1[:]:
        if item in arr2:
            arr1.remove(item)
            arr2.remove(item)
    arr1.extend(arr2)
    return arr1

print(difference([1, 2, 3], [3, 4, 5]))  # should return [1, 2, 4, 5]
print(difference(["a", "b"], ["c", "b"]))  # should return ["a", "c"]
print(difference([1, "a", 2], [2, "b", "a"]))  # should return [1, "b"] 
print(difference([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]))  # should return [2, 4, 6, 8]

# Comments - fun challenge. Not overly difficult, but fun to think about, to develop, and to test
# Array extension was a new skill, but the loop through the first array while simultaneously removing matching items from both is quite easy