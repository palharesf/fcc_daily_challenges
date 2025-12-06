# Date Formatter

# Given a date in the format "Month day, year", return the date in the format "YYYY-MM-DD".

#     The given month will be the full English month name. For example: "January", "February", etc.
#     In the return value, pad the month and day with leading zeros if necessary to ensure two digits.

# For example, given "December 6, 2025", return "2025-12-06".
# Tests

# 1. format_date("December 6, 2025") should return "2025-12-06".
# 2. format_date("January 1, 2000") should return "2000-01-01".
# 3. format_date("November 11, 1111") should return "1111-11-11".
# 4. format_date("September 7, 512") should return "512-09-07".
# 5. format_date("May 4, 1950") should return "1950-05-04".
# 6. format_date("February 29, 1992") should return "1992-02-29".

from datetime import datetime

def format_date(date_string):
    date_string = date_string.split(" ")

    year = date_string[2]

    dt = datetime.strptime(date_string[0], "%B")
    month = dt.strftime("%m")

    day = date_string[1].replace(",", "").zfill(2)

    return year + "-" + month + "-" + day

print(format_date("December 6, 2025"))  # Expected: "2025-12-06"
print(format_date("January 1, 2000"))    # Expected: "2000-01-01"
print(format_date("November 11, 1111"))  # Expected: "1111-11-11"
print(format_date("September 7, 512"))   # Expected: "512-09-07"
print(format_date("May 4, 1950"))        # Expected: "1950-05-04"
print(format_date("February 29, 1992"))  # Expected: "1992-02-29"

# Comments: not too tricky, but date manipulation is never obvious