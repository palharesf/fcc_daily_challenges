# Miles to Kilometers

# Given a distance in miles as a number, return the equivalent distance in kilometers.

#     The input will always be a non-negative number.
#     1 mile equals 1.60934 kilometers.
#     Round the result to two decimal places.

# Tests

# 1. convert_to_km(1) should return 1.61.
# 2. convert_to_km(21) should return 33.8.
# 3. convert_to_km(3.5) should return 5.63.
# 4. convert_to_km(0) should return 0.
# 5. convert_to_km(0.621371) should return 1.

def convert_to_km(miles):
    km = round(miles * 1.60934, 2)
    if km == int(km):
        return int(km)
    else:
        return km

print(convert_to_km(1))         # Expected output: 1.61
print(convert_to_km(21))        # Expected output: 33.8
print(convert_to_km(3.5))       # Expected output: 5.63
print(convert_to_km(0))         # Expected output: 0
print(convert_to_km(0.621371))  # Expected output: 1

# Comments: extremely easy exercise, with the only caveat being the handling of rounding to avoid trailing zeros, which became easy after a challenge a few weeks ago where I learned to handle that