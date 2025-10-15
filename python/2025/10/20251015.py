# HTML Tag Stripper

# Given a string of HTML code, remove the tags and return the plain text content.

#     The input string will contain only valid HTML.
#     HTML tags may be nested.
#     Remove the tags and any attributes.

# For example, '<a href="#">Click here</a>' should return "Click here".
# Tests

# 1. strip_tags('<a href="#">Click here</a>') should return "Click here".
# 2. strip_tags('<p class="center">Hello <b>World</b>!</p>') should return "Hello World!".
# 3. strip_tags('<img src="cat.jpg" alt="Cat">') should return an empty string ("").
# 4. strip_tags('<main id="main"><section class="section">section</section><section class="section">section</section></main>') should return sectionsection.

import re

def strip_tags(html):
    html = re.sub(r'<.*?>', '', html)
    return html

strip_tags('<a href="#">Click here</a>')
strip_tags('<p class="center">Hello <b>World</b>!</p>')
strip_tags('<img src="cat.jpg" alt="Cat">')
strip_tags('<main id="main"><section class="section">section</section><section class="section">section</section></main>')

# Comments - this is an exercise that can either be very difficult or very simple, depending on the tools one decides to use
# I know of Regex and thought it would be a good approach, and alas, it was a straightforward solution
# But I could also see this exercise being very difficult without it, or if the rules required some other type of nuance