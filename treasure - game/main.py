print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______
*******************************************************************************
''')
print("welcome to Treasure Hounting Game !")
print("Your mission is to find a treasure... and stay alive !")
print("Adventure begins wright now. You need to make your first choice. Which direction you will chose?")
first_direction_given = input("Which path you want to go? Left (L) or right (R) ?")

first_direction = first_direction_given.lower()

if first_direction != "l":
    print("GAME OVER! Dragon killed you!")
    print('''                      ,-,-      
                     / / |      
   ,-'             _/ / /       
  (-_          _,-' `Z_/        
   "#:      ,-'_,-.    \  _     
    #'    _(_-'_()\     // |    
  ,--_,--'                 |    
 / ""                      L-'\ 
 \,--^---v--v-._        /   \ | 
   \_________________,-'      | 
                    \           
                     \          
                      \         
       ''')

else:
    print("Good choice! It seems you are lucky one.")
    print("You can see a river in fornt of you.")
    river_given = input("Do you want to swim (S), wait for boat (W)?")

    river = river_given.lower()

    if river == "w":
        print("GAME OVER !\n You have been waiting for 89 years.\n You are a bag of bones now...")
        print('''
        
     _.--""--._
    /  _    _  /
 _  ( (_\  /_) )  _
{ \._\   /\   /_./ }
/_"=-.}______{.-="_/
 _  _.=("""")=._  _
(_'"_.-"`~~`"-._"'_)L.
 {_"            "_}

        ''')
    else:
        print("You have reached the shore.\n You can see a hole in the ground.\n Inside you can see 3 ways")
        print("Which way do you want to go, Mr. Lucky?")
        way_given = input("Left (L), Middle (M), Right (R)?")

        way = way_given.lower()

        if way == "l":
            print("You WON !!! \n Here is the treasure !!!")
            print("And big icecream !!!\n Just for You Mr. Lucky !!!")
            print('''
            
                     _
       ,' `,.
       >-.(__)
      (_,-' |
        `.  |
          `.| 

            `''')
        elif way == "r":
            print("GAME OVER!\n You have been eaten by giant hamster!")
            print('''
            
                    _           
      (`-`;-"```"-;`-`)
       \.'         './
       /             /
       ;   0     0   ;
      /| =         = |/
     ; \   '._Y_.'   / ;
    ;   `-._ \|/ _.-'   ;
   ;        `"""`        ;
   ;    `""-.   .-""`    ;
   /;  '--._ \ / _.--   ;/
  :  `.   `/|| ||\`   .'  :
   '.  '-._       _.-'   .'        
   (((-'`  `"""""`   `'-)))
   
   ''')
        else:
            print("GAME OVER! \n You were killed by Zomie Roaster !!!")
            print('''
            
      .".".".
    (`       `)               _.-=-.
     '._.--.-;             .-`  -'  '.
    .-'`.o )  \           /  .-_.--'  `/
   `;---) \    ;         /  / ;' _-_.-' `
     `;"`  ;    \        ; .  .'   _-' /
      (    )    |        |  / .-.-'    -`
       '-.-'     \       | .' ` '.-'-\`
        /_./\_.|\_\      ;  ' .'-'.-.
        /         '-._    \` /  _;-,
       |         .-=-.;-._ \  -'-,
       \        /      `";`-`,-"`)
        \       \     '-- `\./
         '.      '._ '-- '--'/
           `-._     `'----'`;
               `"""--.____,/
                      //  /
                      // /`
                  ___// /__
                (`(`(---"-`)
            ''')
