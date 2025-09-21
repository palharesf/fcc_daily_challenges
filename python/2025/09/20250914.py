# Word Frequency

# Given a paragraph, return an array of the three most frequently occurring words.

#     Words in the paragraph will be separated by spaces.
#     Ignore case in the given paragraph. For example, treat Hello and hello as the same word.
#     Ignore punctuation in the given paragraph. Punctuation consists of commas (,), periods (.), and exclamation points (!).
#     The returned array should have all lowercase words.
#     The returned array should be in descending order with the most frequently occurring word first.

# Tests

# Waiting: 1. get_words("Coding in Python is fun because coding Python allows for coding in Python easily while coding") should return ["coding", "python", "in"].
# Waiting: 2. get_words("I like coding. I like testing. I love debugging!") should return ["i", "like", "coding"].
# Waiting: 3. get_words("Debug, test, deploy. Debug, debug, test, deploy. Debug, test, test, deploy!") should return ["debug", "test", "deploy"].

def get_words(paragraph):

    # Separate paragraph into words
    words = paragraph.split(" ")
    # print("Splits by space:", words)

    # Remove punctuation
    words = [word.replace(",", "").replace(".", "").replace("!", "") for word in words]
    # print("Remove punctuation:", words)

    # Convert to lowercase
    words = [word.lower() for word in words]
    # print("Normalize case:", words)

    # Create dictionary to count words
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    # print("Word count:", word_count)

    # Sort dictionary by value
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    # print("Sorted word count:", sorted_word_count)

    # Get top 3 words
    top_3_words = [word for word, count in sorted_word_count[:3]]

    # Print top 3 words
    print(top_3_words)

    return top_3_words


get_words("Coding in Python is fun because coding Python allows for coding in Python easily while coding")
get_words("I like coding. I like testing. I love debugging!")
get_words("Debug, test, deploy. Debug, debug, test, deploy. Debug, test, test, deploy!")

# Comments: it's not an overly complex challenge. It probably can be done faster, but going step by step in a methodical way works really well here.
# The trickiest parts are creating the dictionary to count word frequency, and the sorter, although the sorter benefits from built-in Python functions