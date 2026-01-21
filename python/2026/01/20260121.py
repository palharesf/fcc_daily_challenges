# Markdown Inline Code Parser

# Given a string of Markdown that includes one or more inline code blocks, return the equivalent HTML string.

# Inline code blocks in Markdown use a single backtick (`) at the start and end of the code block text.

# Return the given string with all code blocks converted to HTML code tags.

# For example, given the string "Use `let` to declare the variable.", return "Use <code>let</code> to declare the variable.".

# Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
# Tests

# 1. parse_inline_code("Use `let` to declare the variable.") should return "Use <code>let</code> to declare the variable.".
# 2. parse_inline_code("Use `let` or `const` to declare a variable.") should return "Use <code>let</code> or <code>const</code> to declare a variable.".
# 3. parse_inline_code("Run `npm install` then `npm start`.") should return "Run <code>npm install</code> then <code>npm start</code>.".

def parse_inline_code(markdown):
    while markdown.find("`") > 0:
        start_index = markdown.find("`")
        end_index = markdown.find("`", start_index + 1)
        markdown = markdown[:start_index] + "<code>" + markdown[start_index+1:end_index] + "</code>" + markdown[end_index+1:]
    return markdown

print(parse_inline_code("Use `let` to declare the variable."))
print(parse_inline_code("Use `let` or `const` to declare a variable."))
print(parse_inline_code("Run `npm install` then `npm start`."))

# The trick here is to define end_index in a way it starts searching for the next backtick after the first one. Having solved that, the rest is straightforward