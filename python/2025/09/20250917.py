# Slug Generator

# Given a string, return a URL-friendly version of the string using the following constraints:

#     All letters should be lowercase.
#     All characters that are not letters, numbers, or spaces should be removed.
#     All spaces should be replaced with the URL-encoded space code %20.
#     Consecutive spaces should be replaced with a single %20.
#     The returned string should not have leading or trailing %20.

# Tests

# 1. generate_slug("helloWorld") should return "helloworld".
# 2. generate_slug("hello world!") should return "hello%20world".
# 3. generate_slug(" hello-world ") should return "helloworld".
# 4. generate_slug("hello  world") should return "hello%20world".
# 5. generate_slug("  ?H^3-1*1]0! W[0%R#1]D  ") should return "h3110%20w0r1d".

def generate_slug(str):
    join = ""
    new_str = []

    # Trim leading and tailing whitespaces
    strip = str.strip()
    # print(strip)

    # Separate string into characters
    str_list = list(strip)
    print("Str_list: ", str_list)

    for i, char in enumerate(str_list):

        # Replace all spaces with %20
        if char == " ":
            if (i > 0 and str_list[i - 1] == " "): # If the previous character is already a space, collapse all consecutive spaces into a single one
                pass
            else:
                new_str.append("%20")

        # Remove everything not a letter, number or space
        elif not char.isalnum():
            pass

        # Lowercase all letters
        else:
            new_str.append(char.lower())


    print(new_str)

    join = "".join(new_str)
    print(join)

    return join

generate_slug("helloWorld")
generate_slug("hello world!")
generate_slug(" hello-world ")
generate_slug("hello  world")
generate_slug("  ?H^3-1*1]0! W[0%R#1]D  ")

# Comments: interesting and enjoyable challenge. It's possible to break it down into several smaller tasks and debug them one by one
# An interesting approach was the suggestion of using 'enumerate' when looping through the characters in the string. This allowed me to keep track of the index, which was useful when dealing with consecutive spaces
# Not something I would have thought of, but I'm glad I was exposed to it
# The order of the operations is also important - starting with the leading and trailing white-spaces simplify the loop further on