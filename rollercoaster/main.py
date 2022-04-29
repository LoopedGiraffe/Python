print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
    
if height >= 120: 
    print("Yoou can ride on rollercoaster")
    age = int(input("What is your age?"))
    if age < 12:
        print("price $5")
    elif age <= 18:
        print("price: $7")
    else:
        print("price $9")
else:
    print("You need to grow some more")