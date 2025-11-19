# Markdown Heading Converter

# Given a string representing a Markdown heading, return the equivalent HTML heading.

# A valid Markdown heading must:

#     Start with zero or more spaces, followed by
#     1 to 6 hash characters (#) in a row, then
#     At least one space. And finally,
#     The heading text.

# The number of hash symbols determines the heading level. For example, one hash symbol corresponds to an h1 tag, and six hash symbols correspond to an h6 tag.

# If the given string doesn't have the exact format above, return "Invalid format".

# For example, given "# My level 1 heading", return "<h1>My level 1 heading</h1>".

# Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
# Tests

# 1. convert("# My level 1 heading") should return "<h1>My level 1 heading</h1>".
# 2. convert("My heading") should return "Invalid format".
# 3. convert("##### My level 5 heading") should return "<h5>My level 5 heading</h5>".
# 4. convert("#My heading") should return "Invalid format".
# 5. convert("  ###  My level 3 heading") should return "<h3>My level 3 heading</h3>".
# 6. convert("####### My level 7 heading") should return "Invalid format".
# 7. convert("## My #2 heading") should return "<h2>My #2 heading</h2>".

import re

def count_adjacent_hashes(heading):
    # Remove non-hash characters from the heading
    heading = re.sub(r"[^\s#]", "", heading)

    # Find all sequences of adjacent hash signs
    match = re.search(r"#+", heading)
    if match is None:
        return 0
    else:
        return len(match.group())

def convert(heading):
    heading = heading.strip()
    level = count_adjacent_hashes(heading)
    print(level)
    if level == 0 or level > 6:
        return "Invalid format"
    elif heading[0] != "#":
        return "Invalid format"
    else:
        heading = heading.strip("#")
        if heading[0] != " ":
            return "Invalid format"
        while heading[0] == " ":
            heading = heading[1:]
        return "<h" + str(level) + ">" + heading + "</h" + str(level) + ">"
    
convert("# My level 1 heading")
convert("My heading")
convert("##### My level 5 heading")
convert("#My heading")
convert("  ###  My level 3 heading")
convert("####### My level 7 heading")
convert("## My #2 heading")

# Comments - an annoying exercise
# First because it relies a lot on RegEx, which is never fun to use, develop or debug
# Second because there are a lot of edge cases that need to be treated, and it's never immediately clear if the solution works for edge cases not tested as well (e.g. like checking if heading[0] is not a space before trimming all spaces)
# The complexity is such that it requires a helper function and a library import in such a small challenge
# It works, but it's not super satisfying