# Thermostat Adjuster

# Given the current temperature of a room and a target temperature, return a string indicating how to adjust the room temperature based on these constraints:

#     Return "heat" if the current temperature is below the target.
#     Return "cool" if the current temperature is above the target.
#     Return "hold" if the current temperature is equal to the target.

# Tests

# Waiting: 1. adjust_thermostat(68, 72) should return "heat".
# Waiting: 2. adjust_thermostat(75, 72) should return "cool".
# Waiting: 3. adjust_thermostat(72, 72) should return "hold".
# Waiting: 4. adjust_thermostat(-20.5, -10.1) should return "heat".
# Waiting: 5. adjust_thermostat(100, 99.9) should return "cool".
# Waiting: 6. adjust_thermostat(0.0, 0.0) should return "hold".

def adjust_thermostat(temp, target):

    # Determine action
    temp_diff = temp - target

    # Implement case switch
    match temp_diff:
        case x if x < 0:
            action = "heat"
        case x if x > 0:
            action = "cool"
        case _:
            action = "hold" # Default case
    
    # print(action)
    return action

adjust_thermostat(68, 72)
adjust_thermostat(75, 72)
adjust_thermostat(72, 72)
adjust_thermostat(-20.5, -10.1)
adjust_thermostat(100, 99.9)
adjust_thermostat(0.0, 0.0)

# Comments: Case:switch is surprisingly finnicky to implement in Python.
# Most AI Agents suggest I use simple if/elif/else statements, but I wanted to try out case:switch here regardless
# The solution was to use match, which is a powerful pattern matching function
# Once that has been setup, it was straightforward to destructure our cases by evaluating expressions instead of simple variable values
# Good reminder that what seems easier in my mind coming from JS might not always be the best solution in Python