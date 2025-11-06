# Weekday Finder

# Given a string date in the format YYYY-MM-DD, return the day of the week.

# Valid return days are:

#     "Sunday"
#     "Monday"
#     "Tuesday"
#     "Wednesday"
#     "Thursday"
#     "Friday"
#     "Saturday"

# Be sure to ignore time zones.
# Tests

# 1. get_weekday("2025-11-06") should return Thursday.
# 2. get_weekday("1999-12-31") should return Friday.
# 3. get_weekday("1111-11-11") should return Saturday.
# 4. get_weekday("2112-12-21") should return Wednesday.
# 5. get_weekday("2345-10-01") should return Monday.

import datetime

def get_weekday(date_string):
    year = int(date_string[0:4])
    month = int(date_string[5:7])
    day = int(date_string[8:10])

    date_UTC = datetime.datetime(year, month, day)
    weekday = date_UTC.weekday()

    if weekday == 6:
        return "Sunday"
    elif weekday == 0:
        return "Monday"
    elif weekday == 1:
        return "Tuesday"
    elif weekday == 2:
        return "Wednesday"
    elif weekday == 3:
        return "Thursday"
    elif weekday == 4:
        return "Friday"
    elif weekday == 5:
        return "Saturday"

get_weekday("2025-11-06")
get_weekday("1999-12-31")
get_weekday("1111-11-11")
get_weekday("2112-12-21")
get_weekday("2345-10-01")

# Comments - working with dates is always a bit arcane, but it turns out two functions were enough to get the job done
# After that it was only a matter of checking the day of the week. This probably could be done more elegantly with a key:value dictionary or a case:switch statement, but it works