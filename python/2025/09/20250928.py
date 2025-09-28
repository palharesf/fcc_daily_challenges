# CSV Header Parser

# Given the first line of a comma-separated values (CSV) file, return an array containing the headings.

#     The first line of a CSV file contains headings separated by commas.
#     Remove any leading or trailing whitespace from each heading.

# Tests

# 1. get_headings("name,age,city") should return ["name", "age", "city"].
# 2. get_headings("first name,last name,phone") should return ["first name", "last name", "phone"].
# 3. get_headings("username , email , signup date ") should return ["username", "email", "signup date"].

def get_headings(csv):
    csv = csv.split(",")
    csv = [csv[i].strip() for i in range(len(csv))]
    # print(csv)
    return csv

get_headings("name,age,city")
get_headings("first name,last name,phone")
get_headings("username , email , signup date ")

# Comments: very straightforward. Aided by AI, but the steps to solve it were very simple
# Handling strings is the kind of thing that tends to be simple if you know the few important commands such as split and strip here