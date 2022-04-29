#assume that days in year = 365, months = 12 and weeks = 52
age = input("What is your current age?")


left_years = 90 - age
left_months = left_years * 12
left_weeks = left_years * 52
left_days = left_years * 365

print(f"You have {left_days} days, {left_weeks} weeks, and {left_months} months left.")