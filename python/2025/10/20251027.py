# Integer Sequence

# Given a positive integer, return a string with all of the integers from 1 up to, and including, the given number, in numerical order.

# For example, given 5, return "12345".
# Tests

# 1. sequence(5) should return "12345".
# 2. sequence(10) should return "12345678910".
# 3. sequence(1) should return "1".
# 4. sequence(27) should return "123456789101112131415161718192021222324252627".

def sequence(n):
    sequence = ""
    for i in range(1, n + 1):
        sequence += str(i)
    return sequence

sequence(5)
sequence(10)
sequence(1)
sequence(27)

# Comments - straightforward challenge, but one that I would probably struggle a month or so ago. 
# After seeing so many challenges that required initializing an empty string and appending elements on a loop, this one came naturally and I'm glad the approach worked from the get-go