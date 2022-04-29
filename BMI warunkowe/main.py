# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round(weight / height ** 2)

# \033[1m  tu idzie text do pogrubienia  \033[0m

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are \033[1munderweight\033[0m.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have \033[1ma normal weight\033[0m.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are \033[1mslightly overweight\033[0m.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are \033[1mobese\033[0m.")
else:
    print(f"Your BMI is {BMI}, you are \033[1mclinically obese\033[0m.")