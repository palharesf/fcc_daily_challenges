# Space Week Day 6: Moon Phase

# For day six of Space Week, you will be given a date in the format "YYYY-MM-DD" and need to determine the phase of the moon for that day using the following rules:

# Use a simplified lunar cycle of 28 days, divided into four equal phases:

#     "New": days 1 - 7
#     "Waxing": days 8 - 14
#     "Full": days 15 - 21
#     "Waning": days 22 - 28

# After day 28, the cycle repeats with day 1, a new moon.

#     Use "2000-01-06" as a reference new moon (day 1 of the cycle) to determine the phase of the given day.
#     You will not be given any dates before the reference date.
#     Return the correct phase as a string.

# Tests

# 1. moon_phase("2000-01-12") should return "New".
# 2. moon_phase("2000-01-13") should return "Waxing".
# 3. moon_phase("2014-10-15") should return "Full".
# 4. moon_phase("2012-10-21") should return "Waning".
# 5. moon_phase("2022-12-14") should return "New".

from datetime import datetime

def moon_phase(date_string):
    # reference_year = 2000
    # reference_month = 1
    # reference_day = 6

    # date_year = int(date_string[0:4])
    # date_month = int(date_string[5:7])
    # date_day = int(date_string[8:10])

    # years_since_reference = date_year - reference_year
    # months_since_reference = date_month - reference_month + years_since_reference * 12
    # days_since_reference = date_day - reference_day + months_since_reference * 28

    reference_date = datetime(2000, 1, 6)
    given_date = datetime.strptime(date_string, "%Y-%m-%d")
    days_since_reference = (given_date - reference_date).days

    # print(days_since_reference)

    reference_index = days_since_reference % 28
    # print(reference_index)
    
    if reference_index < 7:
        date_string = "New"
    elif reference_index < 14:
        date_string = "Waxing"
    elif reference_index < 21:
        date_string = "Full"
    else:
        date_string = "Waning"

    print(date_string)
    return date_string

moon_phase("2000-01-12")
moon_phase("2000-01-13")
moon_phase("2014-10-15")
moon_phase("2012-10-21")
moon_phase("2022-12-14")

# Comments: very tricky and annoying challenge, if only because it required the use of the datetime module instead of relying solely on calculations performed within the code
# I kept my original approach commented out, but the prompt should be clearer about this requirement. Since this is a training challenge, I assumed it would be reasonable to consider all months having 28 days, which was not the case