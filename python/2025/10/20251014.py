# String Count

# Given two strings, determine how many times the second string appears in the first.

#     The pattern string can overlap in the first string. For example, "aaa" contains "aa" twice. The first two a's and the second two.

# Tests

# 1. count('abcdefg', 'def') should return 1.
# 2. count('hello', 'world') should return 0.
# 3. count('mississippi', 'iss') should return 2.
# 4. count('she sells seashells by the seashore', 'sh') should return 3.
# 5. count('101010101010101010101', '101') should return 10.

def count(text, parameter):
    count = 0

    segment_length = len(parameter)
    segments = [text[i:i+segment_length] for i in range(len(text) - segment_length + 1)]
    # print(segments)

    for segment in segments:
        if segment == parameter:
            count += 1

    return count

count("abcdefg", "def")
count("hello", "world")
count("mississippi", "iss")
count("she sells seashells by the seashore", "sh")
count("101010101010101010101", "101")

# Comments - the tricky part of this exercise is row 19. Creating the segments is not a straightforward operations
# Without AI, I would probably do it in multiple steps instead of consolidating it into one line. It's not difficult per se, just easy to get wrong