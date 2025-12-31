# Markdown Italic Parser

# Given a string that may include some italic text in Markdown, return the equivalent HTML string.

#     Italic text in Markdown is any text that starts and ends with a single asterisk (*) or a single underscore (_).
#     There cannot be any spaces between the text and the asterisk or underscore, but there can be spaces in the text itself.
#     Convert all italic occurrences to HTML i tags and return the string.

# For example, given "*This is italic*", return "<i>This is italic</i>".

# Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
# Tests

# 1. parse_italics("*This is italic*") should return "<i>This is italic</i>".
# 2. parse_italics("_This is also italic_") should return "<i>This is also italic</i>".
# 3. parse_italics("*This is not italic *") should return "*This is not italic *".
# 4. parse_italics("_ This is also not italic_") should return "_ This is also not italic_".
# 5. parse_italics("The *quick* brown fox _jumps_ over the *lazy* dog.") should return "The <i>quick</i> brown fox <i>jumps</i> over the <i>lazy</i> dog.".

def parse_italics(markdown):
    result = ""
    i = 0

    while i < len(markdown):
        char = markdown[i]

        # Check if current character is a potential opening delimiter
        if char in ("*", "_"):
            # Valid opening: no space after (and there must be a next char)
            if i + 1 < len(markdown) and markdown[i + 1] != " ":
                # Look ahead for a matching closing delimiter
                j = i + 1
                found_closing = False

                while j < len(markdown):
                    if markdown[j] == char:
                        # Check if valid closing (no space before)
                        if markdown[j - 1] != " ":
                            # Found valid closing delimiter
                            result += "<i>" + markdown[i + 1 : j] + "</i>"
                            i = j + 1
                            found_closing = True
                            break
                    j += 1

                if not found_closing:
                    # No valid closing found, treat as regular character
                    result += char
                    i += 1
            else:
                # Invalid opening, treat as regular character
                result += char
                i += 1
        else:
            # Regular character
            result += char
            i += 1

    return result
        

print(parse_italics("*This is italic*"))
print(parse_italics("_This is also italic_"))
print(parse_italics("*This is not italic *"))
print(parse_italics("_ This is also not italic_"))
print(parse_italics("The *quick* brown fox _jumps_ over the *lazy* dog."))

# Comments - on average, I hate string manipulation problems. This one, with markdown parser, makes it even more annoying
# Sincerely, I don't feel I learn a lot by doing something like this, since it's just chore/rote work. So I really didn't dedicate myself to do this properly