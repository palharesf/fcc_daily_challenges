# Space Week Day 2: Exoplanet Search

# For the second day of Space Week, you are given a string where each character represents the luminosity reading of a star. Determine if the readings have detected an exoplanet using the transit method. The transit method is when a planet passes in front of a star, reducing its observed luminosity.

#     Luminosity readings only comprise of characters 0-9 and A-Z where each reading corresponds to the following numerical values:
#     Characters 0-9 correspond to luminosity levels 0-9.
#     Characters A-Z correspond to luminosity levels 10-35.

# A star is considered to have an exoplanet if any single reading is less than or equal to 80% of the average of all readings. For example, if the average luminosity of a star is 10, it would be considered to have a exoplanet if any single reading is 8 or less.
# Tests

# 1. has_exoplanet("665544554") should return False.
# 2. has_exoplanet("FGFFCFFGG") should return True.
# 3. has_exoplanet("MONOPLONOMONPLNOMPNOMP") should return False.
# 4. has_exoplanet("FREECODECAMP") should return True.
# 5. has_exoplanet("9AB98AB9BC98A") should return False.
# 6. has_exoplanet("ZXXWYZXYWYXZEGZXWYZXYGEE") should return True.

def has_exoplanet(readings):
    min_lum = 55
    total_lum = 0

    for reading in readings:
        if reading.isalpha():
            reading = ord(reading) - 55
        else:
            reading = int(reading)

        # print("Reading: ", reading)
        
        if reading < min_lum:
            min_lum = reading

        total_lum += reading

    avg_lum = total_lum / len(readings)
    # print("Avg Lum: ", avg_lum, "Min Lum: ", min_lum)

    if min_lum <= avg_lum * 0.8:
        print("True")
        return True
    else:
        print("False")
        return False

has_exoplanet("665544554")
has_exoplanet("FGFFCFFGG")
has_exoplanet("MONOPLONOMONPLNOMPNOMP")
has_exoplanet("FREECODECAMP")
has_exoplanet("9AB98AB9BC98A")
has_exoplanet("ZXXWYZXYWYXZEGZXWYZXYGEE")

# Comments: the prompt was a bit obtuse, but when it came to the implementation, it wasn't the most difficult.
# I lost a lot of time because I thought we had to compare the minimum lum reading with the maximum, when in reality it was compared against the average