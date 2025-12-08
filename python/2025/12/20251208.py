# Pounds to Kilograms

# Given a weight in pounds as a number, return the string "(lbs) pounds equals (kgs) kilograms.".

#     Replace "(lbs)" with the input number.
#     Replace "(kgs)" with the input converted to kilograms, rounded to two decimals and always include two decimal places in the value.
#     1 pound equals 0.453592 kilograms.
#     If the input is 1, use "pound" instead of "pounds".
#     If the converted value is 1, use "kilogram" instead of "kilograms".

# Tests

# 1. convert_to_kgs(1) should return "1 pound equals 0.45 kilograms.".
# 2. convert_to_kgs(0) should return "0 pounds equals 0.00 kilograms.".
# 3. convert_to_kgs(100) should return "100 pounds equals 45.36 kilograms.".
# 4. convert_to_kgs(2.5) should return "2.5 pounds equals 1.13 kilograms.".
# 5. convert_to_kgs(2.20462) should return "2.20462 pounds equals 1.00 kilogram.".

def convert_to_kgs(lbs):
    kgs = round(lbs * 0.453592, 2)
    lbs_unit = "pound" if lbs == 1 else "pounds"
    kgs_unit = "kilogram" if kgs == 1 else "kilograms"
    return f"{lbs} {lbs_unit} equals {kgs:.2f} {kgs_unit}."

print(convert_to_kgs(1))         # "1 pound equals 0.45 kilograms."
print(convert_to_kgs(0))         # "0 pounds equals 0.00 kilograms."
print(convert_to_kgs(100))       # "100 pounds equals 45.36 kilograms."
print(convert_to_kgs(2.5))       # "2.5 pounds equals 1.13 kilograms."
print(convert_to_kgs(2.20462))   # "2.20462 pounds equals 1.00 kilogram."

# Comments - very straightforward exercise. Simple calculations with rounding, and conditional pluralization.