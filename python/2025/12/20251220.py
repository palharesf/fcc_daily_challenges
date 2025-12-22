# Purge Most Frequent

# Given an array of values, remove all occurrences of the most frequently occurring element and return the resulting array.

#     If multiple values are tied for most frequent, remove all of them.
#     Do not change any of the other elements or their order.

# Tests

# 1. purge_most_frequent([1, 2, 2, 3]) should return [1, 3].
# 2. purge_most_frequent(["a", "b", "d", "b", "c", "d", "c", "d", "c", "d"]) should return ["a", "b", "b", "c", "c", "c"].
# 3. purge_most_frequent(["red", "blue", "green", "red", "blue", "green", "blue"]) should return ["red", "green", "red", "green"].
# 4. purge_most_frequent([5, 5, 5, 5]) should return [].

def purge_most_frequent(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    # print(freq)
    max_freq = max(freq.values())
    return [i for i in arr if freq[i] != max_freq]

print(purge_most_frequent([1, 2, 2, 3]))
print(purge_most_frequent(["a", "b", "d", "b", "c", "d", "c", "d", "c", "d"]))
print(purge_most_frequent(["red", "blue", "green", "red", "blue", "green", "blue"]))
print(purge_most_frequent([5, 5, 5, 5]))

# Comments - two step solution. First we find the frequency array, and we use it to calculate the item with max frequency, which is then removed from the original array during the return statement