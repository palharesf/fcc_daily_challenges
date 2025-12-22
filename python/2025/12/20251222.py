# Traveling Shopper

# Given an amount of money you have, and an array of items you want to buy, determine how many of them you can afford.

#     The given amount will be in the format ["Amount", "Currency Code"]. For example: ["150.00", "USD"] or ["6000", "JPY"].
#     Each array item you want to purchase will be in the same format.

# Use the following exchange rates to convert values:
# Currency 	1 Unit Equals
# USD 	1.00 USD
# EUR 	1.10 USD
# GBP 	1.25 USD
# JPY 	0.0070 USD
# CAD 	0.75 USD

#     If you can afford all the items in the list, return "Buy them all!".
#     Otherwise, return "Buy the first X items.", where X is the number of items you can afford when purchased in the order given.

# Tests

# 1. buy_items(["150.00", "USD"], [["50.00", "USD"], ["75.00", "USD"], ["30.00", "USD"]]) should return "Buy the first 2 items.".
# 2. buy_items(["200.00", "EUR"], [["50.00", "USD"], ["50.00", "USD"]]) should return "Buy them all!".
# 3. buy_items(["100.00", "CAD"], [["20.00", "USD"], ["15.00", "EUR"], ["10.00", "GBP"], ["6000", "JPY"], ["5.00", "CAD"], ["10.00", "USD"]]) should return "Buy the first 3 items.".
# 4. buy_items(["5000", "JPY"], [["3.00", "USD"], ["1000", "JPY"], ["5.00", "CAD"], ["2.00", "EUR"], ["4.00", "USD"], ["2000", "JPY"]]) should return "Buy them all!".
# 5. buy_items(["200.00", "USD"], [["50.00", "USD"], ["40.00", "EUR"], ["30.00", "GBP"], ["5000", "JPY"], ["25.00", "CAD"], ["20.00", "USD"]]) should return "Buy the first 5 items.".

def buy_items(funds, items):
    currency = {"USD": 1.00, "EUR": 1.10, "GBP": 1.25, "JPY": 0.0070, "CAD": 0.75}
    budget_usd = float(funds[0]) * currency[funds[1]]
    total = 0
    count = 0

    for item in items:
        item_usd = float(item[0]) * currency[item[1]]
        total += item_usd
        count += 1
        if total > budget_usd:
            return "Buy the first {} items.".format(count - 1)
    return "Buy them all!"

print(buy_items(["150.00", "USD"], [["50.00", "USD"], ["75.00", "USD"], ["30.00", "USD"]]))
print(buy_items(["200.00", "EUR"], [["50.00", "USD"], ["50.00", "USD"]]))
print(buy_items(["100.00", "CAD"], [["20.00", "USD"], ["15.00", "EUR"], ["10.00", "GBP"], ["6000", "JPY"], ["5.00", "CAD"], ["10.00", "USD"]]))
print(buy_items(["5000", "JPY"], [["3.00", "USD"], ["1000", "JPY"], ["5.00", "CAD"], ["2.00", "EUR"], ["4.00", "USD"], ["2000", "JPY"]]))
print(buy_items(["200.00", "USD"], [["50.00", "USD"], ["40.00", "EUR"], ["30.00", "GBP"], ["5000", "JPY"], ["25.00", "CAD"], ["20.00", "USD"]]))

# Comments - a challenge that tripped me for a while. The trick here is to work with everything in USD, and for a while I was using the budget in a separate currency
# Once you normalize everything to USD, it becomes pretty straightforward