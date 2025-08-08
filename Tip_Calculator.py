# Asking the user for input
meal = float(input("Enter the cost of meal: "))
tip_percent = float(input("Enter the tip percentage: "))
members = int(input("How many people will split the bill?: "))


# Calculation
tip = round(meal / 100 * tip_percent)
cost = (tip + meal)
meal_1 = (cost / members)


# Result/Output
print("------Your Bill------")
print("Tip to be paid: ", tip)
print("Total cost: ", cost)
print("Each member to pay: ", meal_1)