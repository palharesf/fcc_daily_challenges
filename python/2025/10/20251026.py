# Duration Formatter

# Given an integer number of seconds, return a string representing the same duration in the format "H:MM:SS", where "H" is the number of hours, "MM" is the number of minutes, and "SS" is the number of seconds. Return the time using the following rules:

#     Seconds: Should always be two digits.
#     Minutes: Should omit leading zeros when they aren't needed. Use "0" if the duration is less than one minute.
#     Hours: Should be included only if they're greater than zero.

# Tests

# 1. format(500) should return "8:20".
# 2. format(4000) should return "1:06:40".
# 3. format(1) should return "0:01".
# 4. format(5555) should return "1:32:35".
# 5. format(99999) should return "27:46:39".

def format(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 3600) % 60
    if hours == 0:
        print(f"{minutes}:{seconds:02}")
        return f"{minutes}:{seconds:02}"
    else:
        print(f"{hours}:{minutes:02}:{seconds:02}")
        return f"{hours}:{minutes:02}:{seconds:02}"

format(500)
format(4000)
format(1)
format(5555)
format(99999)

# Comments - breaking down the time components was straightforward
# The formatting is what I would have spent more time on if I didn't have AI help 
# The 'hours' conditional was the only thing I had to add after the first run