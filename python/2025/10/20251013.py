# 24 to 12

# Given a string representing a time of the day in the 24-hour format of "HHMM", return the time in its equivalent 12-hour format of "H:MM AM" or "H:MM PM".

#     The given input will always be a four-digit string in 24-hour time format, from "0000" to "2359".

# Tests

# 1. to_12("1124") should return "11:24 AM".
# 2. to_12("0900") should return "9:00 AM".
# 3. to_12("1455") should return "2:55 PM".
# 4. to_12("2346") should return "11:46 PM".
# 5. to_12("0030") should return "12:30 AM".

def to_12(time):
    if int(time[:2]) > 12:
        time = str(int(time[:2]) - 12) + ":" + time[2:]
        time += " PM"
        return time
    if int(time[:2]) == 0:
        time = "12:" + time[2:]
        time += " AM"
        return time
    else:
        time = str(int(time[:2])) + ":" + time[2:]
        time += " AM"
        return time

to_12("1124")
to_12("0900")
to_12("1455")
to_12("2346")
to_12("0030")

# Comments: straightforward but enjoyable exercise. Thinking about the scenarios was enjoyable, and composing each return statement was not immediate but not overly challenging
# The biggest challenge was deciding to include a return statement in each loop, instead of letting the function return the value at the end, since it caused a few bugs