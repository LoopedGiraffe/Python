# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

T = lower_case_name1.count("t") + lower_case_name2.count("t")
R = lower_case_name1.count("r") + lower_case_name2.count("r")
U = lower_case_name1.count("u") + lower_case_name2.count("u")
E = lower_case_name1.count("e") + lower_case_name2.count("e")

TRUE = T + R + U + E
T= str(TRUE)

L = lower_case_name1.count("l") + lower_case_name2.count("l")
O = lower_case_name1.count("o") + lower_case_name2.count("o")
V = lower_case_name1.count("v") + lower_case_name2.count("v")
E = lower_case_name1.count("e") + lower_case_name2.count("e")

LOVE = L + O + V + E
L = str(LOVE)

love_score_string = T + L

love_score = int(love_score_string)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")

elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")

else:
    print(f"Your score is {love_score}.")
