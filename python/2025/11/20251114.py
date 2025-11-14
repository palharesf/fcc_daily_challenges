# Is It the Weekend?

# Given a date in the format "YYYY-MM-DD", return the number of days left until the weekend.

#     The weekend starts on Saturday.
#     If the given date is Saturday or Sunday, return "It's the weekend!".
#     Otherwise, return "X days until the weekend.", where X is the number of days until Saturday.
#     If X is 1, use "day" (singular) instead of "days" (plural).
#     Make sure the calculation ignores your local timezone.

# Tests

# 1. days_until_weekend("2025-11-14") should return "1 day until the weekend.".
# 2. days_until_weekend("2025-01-01") should return "3 days until the weekend.".
# 3. days_until_weekend("2025-12-06") should return "It's the weekend!".
# 4. days_until_weekend("2026-01-27") should return "4 days until the weekend.".
# 5. days_until_weekend("2026-09-07") should return "5 days until the weekend.".
# 6. days_until_weekend("2026-11-29") should return "It's the weekend!".

import datetime

def days_until_weekend(date_string):
    weekday = datetime.datetime.strptime(date_string, "%Y-%m-%d").weekday()
    print(weekday)
    if weekday == 5 or weekday == 6:
        return "It's the weekend!"
    else:
        if weekday == 4:
            return "1 day until the weekend."
        else:
            return str(5 - weekday) + " days until the weekend." 

days_until_weekend("2025-11-14")
days_until_weekend("2025-01-01")
days_until_weekend("2025-12-06")
days_until_weekend("2026-01-27")
days_until_weekend("2026-09-07")
days_until_weekend("2026-11-29")

# Comments: simplistic challenge, the trickiest part is knowing about the datetime functions
# Once we found `weekday`, the rest is just a matter of categorization