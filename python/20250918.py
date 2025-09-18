# Fill The Tank

# Given the size of a fuel tank, the current fuel level, and the price per gallon, return the cost to fill the tank all the way.

#     tankSize is the total capacity of the tank in gallons.
#     fuelLevel is the current amount of fuel in the tank in gallons.
#     pricePerGallon is the cost of one gallon of fuel.
#     The returned value should be rounded to two decimal places in the format: "$d.dd".

# 1. cost_to_fill(20, 0, 4.00) should return "$80.00".
# 2. cost_to_fill(15, 10, 3.50) should return "$17.50".
# 3. cost_to_fill(18, 9, 3.25) should return "$29.25".
# 4. cost_to_fill(12, 12, 4.99) should return "$0.00".
# 5. cost_to_fill(15, 9.5, 3.98) should return "$21.89".

def cost_to_fill(tank_size, fuel_level, price_per_gallon):

    amount_to_fill = tank_size - fuel_level
    total_cost = amount_to_fill * price_per_gallon
    cost_string = f"${total_cost:.2f}"
    # print(cost_string)
    return cost_string

cost_to_fill(20, 0, 4.00)
cost_to_fill(15, 10, 3.50)
cost_to_fill(18, 9, 3.25)
cost_to_fill(12, 12, 4.99)
cost_to_fill(15, 9.5, 3.98)

# Comments: extremely easy challenge. The only slightly more challenging variation was adjusting the output format, which I accomplished using f-string