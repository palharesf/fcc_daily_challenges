# Longest Word

# Given a sentence, return the longest word in the sentence.

#     Ignore periods (.) when determining word length.
#     If multiple words are ties for the longest, return the first one that occurs.

# Tests

# 1. get_longest_word("coding is fun") should return "coding".
# 2. get_longest_word("Coding challenges are fun and educational.") should return "educational".
# 3. get_longest_word("This sentence has multiple long words.") should return "sentence".

def get_longest_word(sentence):

    words = sentence.split(" ")

    longest = 0
    longest_word = ""

    for word in words:
        word = word.replace(".", "")
        if len(word) > longest:
            longest = len(word)
            longest_word = word

    # print(longest_word)
    return longest_word

get_longest_word("coding is fun")
get_longest_word("Coding challenges are fun and educational.")
get_longest_word("This sentence has multiple long words.")

# Comments - pretty straightfoward challenge. There is some initial setup, with splitting the sentence into words and initializing variables, and very quickly we go into the main loop
# The logic is pretty simple, where we remove periods and then keep updating our result by comparing the current word with the previously longest one