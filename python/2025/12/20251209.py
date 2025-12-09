# Most Frequent

# Given an array of elements, return the element that appears most frequently.

#     There will always be a single most frequent element.

# Tests

# 1. most_frequent(["a", "b", "a", "c"]) should return "a".
# 2. most_frequent([2, 3, 5, 2, 6, 3, 2, 7, 2, 9]) should return 2.
# 3. most_frequent([True, False, "False", "True", False]) should return False.
# 4. most_frequent([40, 20, 70, 30, 10, 40, 10, 50, 40, 60]) should return 40.

def most_frequent(arr):
    frequency = {}
    for i in arr:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return [key for key, value in frequency.items() if value == max(frequency.values())][0]

print(most_frequent(["a", "b", "a", "c"]))  # should return "a"
print(most_frequent([2, 3, 5, 2, 6, 3, 2, 7, 2, 9]))  # should return 2
print(most_frequent([True, False, "False", "True", False]))  # should return False
print(most_frequent([40, 20, 70, 30, 10, 40, 10, 50, 40, 60]))  # should return 40

# Comments: quite simple challenge, using a dictionary is what cracks the case here