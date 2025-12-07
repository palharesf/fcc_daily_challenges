# String Compression

# Given a string sentence, return a compressed version of the sentence where consecutive duplicate words are replaced by the word followed with the number of times it repeats in parentheses.

#     Only consecutive duplicates are compressed.
#     Words are separated by single spaces.

# For example, given "yes yes yes please", return "yes(3) please".
# Tests

# 1. compress_string("yes yes yes please") should return "yes(3) please".
# 2. compress_string("I have have have apples") should return "I have(3) apples".
# 3. compress_string("one one three and to the the the the") should return "one(2) three and to the(4)".
# 4. compress_string("route route route route route route tee tee tee tee tee tee") should return "route(6) tee(6)".

def compress_string(sentence):
    words = sentence.split()
    compressed_words = []
    i = 0
    while i < len(words):
        count = 1
        while i + 1 < len(words) and words[i] == words[i + 1]:
            count += 1
            i += 1
        if count > 1:
            compressed_words.append(f"{words[i]}({count})")
        else:
            compressed_words.append(words[i])
        i += 1
    sentence = " ".join(compressed_words)
    return sentence

print(compress_string("yes yes yes please"))  # Expected: "yes(3) please"
print(compress_string("I have have have apples"))  # Expected: "I have(3) apples"
print(compress_string("one one three and to the the the the"))  # Expected: "one(2) three and to the(4)"
print(compress_string("route route route route route route tee tee tee tee tee tee"))  # Expected: "route(6) tee(6)"

# Comments - not super easy but AI handled it on the first try. Following the result and understanding the logic was straightforward