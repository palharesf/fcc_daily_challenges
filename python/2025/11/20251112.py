# Email Signature Generator

# Given strings for a person's name, title, and company, return an email signature as a single string using the following rules:

#     The name should appear first, preceded by a prefix that depends on the first letter of the name. For names starting with (case-insensitive):
#         A-I: Use >> as the prefix.
#         J-R: Use -- as the prefix.
#         S-Z: Use :: as the prefix.
#     A comma and space (, ) should follow the name.
#     The title and company should follow the comma and space, separated by " at " (with spaces around it).

# For example, given "Quinn Waverly", "Founder and CEO", and "TechCo" return "--Quinn Waverly, Founder and CEO at TechCo".
# Tests

# 1. generate_signature("Quinn Waverly", "Founder and CEO", "TechCo") should return "--Quinn Waverly, Founder and CEO at TechCo".
# 2. generate_signature("Alice Reed", "Engineer", "TechCo") should return ">>Alice Reed, Engineer at TechCo".
# 3. generate_signature("Tina Vaughn", "Developer", "example.com") should return "::Tina Vaughn, Developer at example.com".
# 4. generate_signature("B. B.", "Product Tester", "AcmeCorp") should return ">>B. B., Product Tester at AcmeCorp".
# 5. generate_signature("windstorm", "Cloud Architect", "Atmospheronics") should return "::windstorm, Cloud Architect at Atmospheronics".

def generate_signature(name, title, company):
    signature = ""
    if name[0].lower() in ["a", "b", "c", "d", "e", "f", "g", "h", "i"]:
        signature += ">>"
    elif name[0].lower() in ["j", "k", "l", "m", "n", "o", "p", "q", "r"]:
        signature += "--"
    else:
        signature += "::"
    signature += name + ", " + title + " at " + company
    return signature

generate_signature("Quinn Waverly", "Founder and CEO", "TechCo")
generate_signature("Alice Reed", "Engineer", "TechCo")
generate_signature("Tina Vaughn", "Developer", "example.com")
generate_signature("B. B.", "Product Tester", "AcmeCorp")
generate_signature("windstorm", "Cloud Architect", "Atmospheronics")

# Comments: really easy challenge. There's some work to be done in determining the prefix to the name, the rest is simple string manipulation
# Could have been solved with a simple f-string