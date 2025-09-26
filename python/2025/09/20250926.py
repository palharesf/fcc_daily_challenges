# Caught Speeding

# Given an array of numbers representing the speed at which vehicles were observed traveling, and a number representing the speed limit, return an array with two items, the number of vehicles that were speeding, followed by the average amount beyond the speed limit of those vehicles.

#     If there were no vehicles speeding, return [0, 0].

# Tests

# 1. speeding([50, 60, 55], 60) should return [0, 0].
# 2. speeding([58, 50, 60, 55], 55) should return [2, 4].
# 3. speeding([61, 81, 74, 88, 65, 71, 68], 70) should return [4, 8.5].
# 4. speeding([100, 105, 95, 102], 100) should return [2, 3.5].
# 5. speeding([40, 45, 44, 50, 112, 39], 55) should return [1, 57].

def speeding(speeds, limit):
    count = 0
    speed_sum = 0

    for speed in speeds:
        if speed > limit:
            count += 1
            speed_sum += speed - limit

    if count == 0:
        # print([0,0])
        return [0, 0]
    else:
        # print([count, speed_sum / count])
        return [count, speed_sum / count]

speeding([50, 60, 55], 60)
speeding([58, 50, 60, 55], 55)
speeding([61, 81, 74, 88, 65, 71, 68], 70)
speeding([100, 105, 95, 102], 100)
speeding([40, 45, 44, 50, 112, 39], 55)

# Comments: Pretty straightforward. The hardest part is understanding the prompt, but looping over the array and updating the temporary variables was standard, routine programming