rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
chosen = int(input("\nPrint: \n0 for rock \n1 for paper \n2 for scissors \nWhat is your choice? \n"))

if chosen == 0:
    print(f"Your choice: \n {rock}")
elif chosen == 1:
    print(f"Your choice: \n {paper}")
elif chosen == 2:
    print(f"Your choice: \n {scissors}")
else:
    print("Wrong options. Please choose: 0 or 1 or 2")


computer_choice = random.randint(0, 2)

if computer_choice == 0:
    print(f"Computer choice: \n {rock}")
elif computer_choice == 1:
    print(f"Computer choice: \n {paper}")
elif computer_choice == 2:
    print(f"Computer choice: \n {scissors}")

if chosen == computer_choice:
    print("Same signs! \nNo one wins.")
elif (chosen == 0  and computer_choice == 2) or (chosen == 2 and computer_choice == 1) or (chosen == 1 and computer_choice == 0):
    print("Congratulations !!! \n You won!!!")
else:
    print("sorry...\n You loose :(")

