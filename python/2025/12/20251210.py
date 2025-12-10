# Markdown Bold Parser

# Given a string that may include some bold text in Markdown, return the equivalent HTML string.

#     Bold text in Markdown is any text that starts and ends with two asterisks (**) or two underscores (__).
#     There cannot be any spaces between the text and the asterisks or underscores, but there can be spaces in the text itself.
#     Convert all bold occurrences to HTML b tags and return the string.

# For example, given "**This is bold**", return "<b>This is bold</b>".

# Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
# Tests

# 1. parse_bold("**This is bold**") should return "<b>This is bold</b>".
# 2. parse_bold("__This is also bold__") should return "<b>This is also bold</b>".
# 3. parse_bold("**This is not bold **") should return "**This is not bold **".
# 4. parse_bold("__ This is also not bold__") should return "__ This is also not bold__".
# 5. parse_bold("The **quick** brown fox __jumps__ over the **lazy** dog.") should return "The <b>quick</b> brown fox <b>jumps</b> over the <b>lazy</b> dog.".

def parse_bold(markdown):
    result = []
    i = 0
    n = len(markdown)

    while i < n:

        # Check for ** delimiter
        if i + 1 < n and markdown[i : i + 2] == "**":
            # Try to find closing **
            j = i + 2
            found = False
            while j < n:
                if j + 1 < n and markdown[j : j + 2] == "**":
                    # Check for no space right after opening and right before closing
                    if markdown[i + 2] != " " and markdown[j - 1] != " ":
                        result.append("<b>")
                        result.append(markdown[i + 2 : j])
                        result.append("</b>")
                        i = j + 2
                        found = True
                        break
                j += 1
            if found:
                continue
            # If no proper closing, just add the ** as normal text
            result.append("**")
            i += 2

        # Check for __ delimiter (same logic)
        elif i + 1 < n and markdown[i : i + 2] == "__":
            j = i + 2
            found = False
            while j < n:
                if j + 1 < n and markdown[j : j + 2] == "__":
                    if markdown[i + 2] != " " and markdown[j - 1] != " ":
                        result.append("<b>")
                        result.append(markdown[i + 2 : j])
                        result.append("</b>")
                        i = j + 2
                        found = True
                        break
                j += 1
            if found:
                continue
            result.append("__")
            i += 2

        else:
            result.append(markdown[i])
            i += 1

    return "".join(result)


print(parse_bold("**This is bold**"))
print(parse_bold("__This is also bold__"))
print(parse_bold("**This is not bold **"))
print(parse_bold("__ This is also not bold__"))
print(parse_bold("The **quick** brown fox __jumps__ over the **lazy** dog."))

# Comments - very difficult challenge
# My initial idea was to split the input using the two demarcators
# My goal was to see whether we have any double asterisk or double underscore that would justify moving on with the logic
# If we had double asterisks or double underscores, I wanted to check each sequentially -- so if we notice asterisks[i] == **, then we need to check if asterisks[i+1] did not start or end with space, and asterisks [i+2] was also **
# Turns out implementing it was really challenging, and instead, the approach was to simply copy the original string char by char, acting to replace a ** if it fulfilled certain conditions (had a closing **, no space after the first ** or before the second **)
# The final result it much longer and hard to read, but works