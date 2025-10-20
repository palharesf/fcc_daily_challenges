# HTML Attribute Extractor

# Given a string of a valid HTML element, return the attributes of the element using the following criteria:

#     You will only be given one element.
#     Attributes will be in the format: attribute="value".
#     Return an array of strings with each attribute property and value, separated by a comma, in this format: ["attribute1, value1", "attribute2, value2"].
#     Return attributes in the order they are given.
#     If no attributes are found, return an empty array.

# Tests

# 1. extract_attributes('<span class="red"></span>') should return ["class, red"].
# 2. extract_attributes('<meta charset="UTF-8" />') should return ["charset, UTF-8"].
# 3. extract_attributes("<p>Lorem ipsum dolor sit amet</p>") should return [].
# 4. extract_attributes('<input name="email" type="email" required="true" />') should return ["name, email", "type, email", "required, true"].
# 5. extract_attributes('<button id="submit" class="btn btn-primary">Submit</button>') should return ["id, submit", "class, btn btn-primary"].

def extract_attributes(element):
    opening = element.find('<') + 1
    closing = element.find('>')

    tag_content = element[opening:closing].strip()
    # print(tag_content)

    tag_array = tag_content.split()
    tag_array.pop(0)  # Remove the tag name
    # print("Original array:", tag_array)
       
    for i in range(len(tag_array)):
        if '=' in tag_array[i]:
            attr, value = tag_array[i].split("=", 1)
            value = value.strip('"')
            tag_array[i] = f"{attr}, {value}"
        elif tag_array[i] == '/' or tag_array[i] == '/>':
            tag_array.pop(i)
            break
        else:
            value = tag_array[i].strip('"')
            tag_array[i - 1] = f"{tag_array[i - 1]} {value}"
            tag_array.pop(i)

    print("Modified array:", tag_array)
    return tag_array

extract_attributes('<span class="red"></span>')
extract_attributes('<meta charset="UTF-8" />')
extract_attributes("<p>Lorem ipsum dolor sit amet</p>")
extract_attributes('<input name="email" type="email" required="true" />')
extract_attributes('<button id="submit" class="btn btn-primary">Submit</button>')

# Comments - really annoying exercise. String-manipulation exercises tend to be a hassle, since they rely on heuristics like what we see here or on Regex, which sucks
# This works, but I don't love it. It takes a lot of edge-case testing to get right, and even then, right is not super flexible
# To be effective, the input has to be very strict, which is not always the case