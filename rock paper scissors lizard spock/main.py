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

lizard = '''

     .                  .            .
 .             _.--._       /|
        .    .'()..()`.    / /
            ( `-.__.-' )  ( (    .
   .         \        /    \ |
       .      \      /      ) )        .
            .' -.__.- `.-.-'_.'
 .        .'  /-____-\  `.-'       .
          \  /-.____.-\  /-.
           \ \`-.__.-'/ /\|\|           .
          .'  `.    .'  `.
          |/\/\|    |/\/\|
'''
spock = '''
                      _    
                     | |   
 ___ _ __   ___   ___| | __
/ __| '_ \ / _ \ / __| |/ /
\__ \ |_) | (_) | (__|   < 
|___/ .__/ \___/ \___|_|\_\
    | |                    
    |_|                    
'''

import random
chosen = int(input("\nPrint: \n0 for rock \n1 for paper \n2 for scissors \n3 for lizard \n4 for Spock \nWhat is your choice? \n"))

if chosen == 0:
    print(f"Your choice: \n {rock}")
elif chosen == 1:
    print(f"Your choice: \n {paper}")
elif chosen == 2:
    print(f"Your choice: \n {scissors}")
elif chosen == 3:
    print(f"Your choice: \n {lizard}")
elif chosen == 4:
    print(f"Your choice: \n {spock}")
else:
    print("Wrong options. Please choose: 0 or 1 or 2 or 3 or 4.")


computer_choice = random.randint(0, 2)

if computer_choice == 0:
    print(f"Computer choice: \n {rock}")
elif computer_choice == 1:
    print(f"Computer choice: \n {paper}")
elif computer_choice == 2:
    print(f"Computer choice: \n {scissors}")
elif computer_choice == 3:
    print(f"Computer choice: \n {lizard}")
elif computer_choice == 4:
    print(f"Computer choice: \n {spock}")

if chosen == computer_choice:
    print("Same signs! \nNo one wins.")
elif (chosen == 0  and computer_choice == 2) or (chosen == 2 and computer_choice == 1) or (chosen == 1 and computer_choice == 0) or (chosen == 0  and computer_choice == 3) or (chosen == 3  and computer_choice == 4) or (chosen == 4  and computer_choice == 2) or (chosen == 2  and computer_choice == 3) or (chosen == 3  and computer_choice == 1) or (chosen == 1  and computer_choice == 4) or (chosen == 4  and computer_choice == 0):
    print("Congratulations !!! \n You won!!!")
else:
    print("sorry...\n You loose :(")
