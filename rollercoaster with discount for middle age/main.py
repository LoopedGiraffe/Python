print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120: 
    print("Yoou can ride on rollercoaster")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        #bill = 0 - nie trzeba tego dodawać ponieważ bierze z "góry" - nie zmieniamy wartości
        print("Free ride")
    else:
        bill = 9
        print("Adult tickets are $9.")
    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        #add $3 to bill
        bill = bill + 3
        # shorter version: bill += 3
    print(f"Your final bill is {bill}")

else:
    print("You need to grow some more")