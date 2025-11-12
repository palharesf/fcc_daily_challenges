# Extension Extractor

# Given a string representing a filename, return the extension of the file.

#     The extension is the part of the filename that comes after the last period (.).
#     If the filename does not contain a period or ends with a period, return "none".
#     The extension should be returned as-is, preserving case.

# Tests

# 1. get_extension("document.txt") should return "txt".
# 2. get_extension("README") should return "none".
# 3. get_extension("image.PNG") should return "PNG".
# 4. get_extension(".gitignore") should return "gitignore".
# 5. get_extension("archive.tar.gz") should return "gz".
# 6. get_extension("final.draft.") should return "none".

def get_extension(filename):
    extension = ""
    splits = filename.split(".")
    print(splits)
    if len(splits) > 1:
        if splits[-1] == "":
            extension = "none"
        else:
            extension = splits[-1]
    else:
        extension = "none"
    return extension

get_extension("document.txt")
get_extension("README")
get_extension("image.PNG")
get_extension(".gitignore")
get_extension("archive.tar.gz")
get_extension("final.draft.")

# Comments - not super difficult. The main extraction / split loop is quite straightforward, then it becomes an exercise of finding edge cases and categorizing them effectively