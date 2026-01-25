# Scaled Image

# Given a string representing the width and height of an image, and a number to scale the image, return the scaled width and height.

#     The input string is in the format "WxH". For example, "800x600".
#     The scale is a number to multiply the width and height by.

# Return the scaled dimensions in the same "WxH" format.
# Tests

# 1. scale_image("800x600", 2) should return "1600x1200".
# 2. scale_image("100x100", 10) should return "1000x1000".
# 3. scale_image("1024x768", 0.5) should return "512x384".
# 4. scale_image("300x200", 1.5) should return "450x300".

def scale_image(size, scale):
    width, height = size.split("x")
    return f"{int(int(width) * scale)}x{int(int(height) * scale)}"

print(scale_image("800x600", 2))
print(scale_image("100x100", 10))
print(scale_image("1024x768", 0.5))
print(scale_image("300x200", 1.5))

# Trick here is to destructure the string into two variables, and nest the integer casting