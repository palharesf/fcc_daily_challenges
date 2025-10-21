# Tip Calculator

# Given the price of your meal and a custom tip percent, return an array with three tip values; 15%, 20%, and the custom amount.

#     Prices will be given in the format: "$N.NN".
#     Custom tip percents will be given in this format: "25%".
#     Return amounts in the same "$N.NN" format, rounded to two decimal places.

# For example, given a "$10.00" meal price, and a "25%" custom tip value, return ["$1.50", "$2.00", "$2.50"].
# Tests

# 1. calculate_tips("$10.00", "25%") should return ["$1.50", "$2.00", "$2.50"].
# 2. calculate_tips("$89.67", "26%") should return ["$13.45", "$17.93", "$23.31"].
# 3. calculate_tips("$19.85", "9%") should return ["$2.98", "$3.97", "$1.79"].

def calculate_tips(meal_price, custom_tip):
    numeric_meal_price = float(meal_price[1:])
    numeric_custom_tip = float(custom_tip[:-1])/100

    output = [
        f"${numeric_meal_price * 0.15:.2f}",
        f"${numeric_meal_price * 0.2:.2f}",
        f"${numeric_meal_price * numeric_custom_tip:.2f}",
    ]
    return output

calculate_tips("$10.00", "25%")
calculate_tips("$89.67", "26%")
calculate_tips("$19.85", "9%")

# Comments - straightforward challenge. Definitely made longer in order to be more readable, but it's a tradeoff I'm happy with
# Using the [1:] and [:-1] slices to remove the '$' and the '%' from the inputs was very helpful, and knowing about specific formatting options such as the :.2f was necessary. Bless Python