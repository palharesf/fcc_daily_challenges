# Longest Word

# Given a sentence string, return the longest word in the sentence.

#     Words are separated by a single space.
#     Only letters (a-z, case-insensitive) count toward the word's length.
#     If there are multiple words with the same length, return the first one that appears.
#     Return the word as it appears in the given string, with punctuation removed.

# Tests

# 1. longest_word("The quick red fox") should return "quick".
# 2. longest_word("Hello coding challenge.") should return "challenge".
# 3. longest_word("Do Try This At Home.") should return "This".
# 4. longest_word("This sentence... has commas, ellipses, and an exlamation point!") should return "exlamation".
# 5. longest_word("A tie? No way!") should return "tie".
# 6. longest_word("Wouldn't you like to know.") should return "Wouldnt".

import re

def longest_word(sentence):
    words = sentence.split(" ")
    longest = 0
    longest_word = ""
    for word in words:
        print(word)
        word = re.sub(r"[.!?,\']", "", word)
        print(word)
        if len(word) > longest:
            longest = len(word)
            longest_word = word
            print(longest_word)
    return longest_word

longest_word("The quick red fox")
longest_word("Hello coding challenge.")
longest_word("Do Try This At Home.")
longest_word("This sentence... has commas, ellipses, and an exlamation point!")
longest_word("A tie? No way!")
longest_word("Wouldn't you like to know.")

# Comments - interesting challenge. Required some small RegEx which wasn't too bad, and the logic itself is pretty straightforward
# Interesting challenge to remove non-word characters, althought I'm not sure it is completely reliable. Instead of removing external symbols, it would be better to only keep aA-z