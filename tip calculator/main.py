print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_to_give = int(input("How much tip would you like to give? 10, 12, or 15? $"))
how_many_people = int(input("How many people to split the bill? "))

tip_to_add = total_bill / 100 * tip_to_give
whole_cost = total_bill + tip_to_add
cost_for_one = whole_cost / how_many_people
rounded = "{:.2f}".format(cost_for_one)


print(f"Each person should pay: ${rounded}")