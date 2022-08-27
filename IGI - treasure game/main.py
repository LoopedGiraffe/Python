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
print("Adventure begins wright now.\n")
print('''
                              __    __    __
                             |==|  |==|  |==|
                           __|__|__|__|__|__|_
                        __|___________________|___
                     __|__[]__[]__[]__[]__[]__[]__|___
                    |............................o.../
                    \.............................../
               hjw_,~')_,~')_,~')_,~')_,~')_,~')_,~')/,~')_
''')
print("you are ona ship and you go to search for treasure on the island")
print("Your ship has hit a rock - and it looks like there is a hole!!! \n Water goes into the ship")
first_choice = input("Now it is time for your first choice:\n Are you try to swim to the island - 'S' ? \n Are you trying to repair the ship - 'R' ?\n")
first = first_choice.lower()
if first == "r":
    print("     !!!You loose!!!\nGiant squid swallows whole ship with everyone on board !!!")
    print('''
             ^
          /   |
          \   /
          |   |
          |   |
          | 0 |            (`-,-,
         // ||//         ('(_,( )
        (( // ||          _   `_'
         ||))  ||      __|_|__|_|_
       //||    ))    _|___________|__
       ( ))   //    |o o o o o o o o/
        //   ((     ~'`~'`~'`~'`~'`~'`~
    ''')
elif first == "s":
    print("Good choice! It seems you are lucky one.")
    print("You are swimming to the island and reaching the destination in one piece!")
    print('''
    
    
                                                   .       .
                                                    \     /
                                                 ._  '   '  _.
                                                   '  o@o  '
                                                     o@@@o
                                                 .-'  o@o  '-.
                                                     .   .
                                                    /     |
                                                   .       .

                             'Xx  xX*,
                          ,*xXXx_xXx
                            _xXXXXXxx*,
                          ,*XXx@x@Xx
                            X @|@@ `x
                            '  ||    '
                               ||
                               ||
                               ||
                               ||
                            /ssssssss.
                      /sssssssSSSSssssssssss.
        /\         /sssssSSSSSSSSSSSSSSSssssssssssss.                  
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~''')
    second_choice = input("It is time for second choice.\nWhere will you go? \n L - left\n S - straight ahead\n R - right\n")
    second = second_choice.lower()

    if second == "l":
        print("Bad move!!!\nHyena eats you for breakfast!\n\n")
        print('''
        
                 _,     _,
                /)|    /)|
                \_'-"`/(_/```",,
                  /   <        ``--._
                  |. _ )     `    *  ',
                  ^  ^/_,     *     (\*|
                  (#_/  `\)  /'  * - ))_|
                   U      \  \*   _,//_ *
                           ) >\_* ((|\_/
                           \ | \  | # (
                            \#  \#\ \ #
                             ||  \(  )/
                             _)> _))/(_
                   .-||,, , /\||//\//\||/),, ,,)/
                     ,\.        .-    -'-,)\/.'))\n
                     ''')
        print("   !!! you loose !!!")
    elif second == "s":
        print("You are lost in wild forest.\nSnakes eats you for lunch!!!")
        print('''
        
            ____
      _,.-'`_ o `;__,                
       _.-'` '---'  '
                    ____
                 .'`_ o `;__,
       .       .'.'` '---'  '            
       .`-...-'.'
        `-...-'
                        _,.--.
    --..,_           .'`__ o  `;__,
       `'.'.       .'.'`  '---'`  '          
          '.`-...-'.'
            `-...-'

    --..,_                     _,.--.
       `'.'.                .'`__ o  `;__.      
          '.'.            .'.'`  '---'`  `
            '.`'--....--'`.'
              `'--....--'`


        ''')
        print("      !!! You loose !!!")

    elif second == "r":
        print("Great! \n You are continue your journey!\n\n After few hours of walking you are meeteing a lizard.\n Three eyed lizard")
        print('''
                                           ^.     ^.    ^.
                                           ) '.   ) '.  ) '.   ^.
                                     ^.   / _..;--"""""---..;  ) '.
                                )\   ) ';-""                 "-""--.._
                            )\_/..'-""                                ".
                   __...---"""                                     ()   "
        ___...---""                                        .             )
 .--""""                      .     ,                       )       _..-"
(_______________________."".  "-.     _________..--".      /___r".""______
                        `,  \  .    '               L     (   '  ;  
                          ,  \/   .'                 '.    '."  ,'
                          .      /                     `,      <_
                       _-'      <_                     "         '-_
                    .-'   .       '-_                   '     _.._  )
                  .'  _.-";   *-.._  )                 ' .\   \   ""
                   '-'    '  '     ""                .'  , `
                        .' .'                        ; .'   '  '.
                       '_.'                           "      '._'
        
        ''')

        print("Three-eyed Lizard leeds you to the mountain with four entrances in it.\nWith way will you choose?\nIt is time for next choice!\n")
        third_choice = input("With entrance will you choose? \n Left entrance - 'L'\n Second from the left - 'SL'\n Second from the right - 'SR'\n Right entrance - 'R'\n ")
        third = third_choice.lower()
        if third == "l":
            print("Swamp monster and bones monsters catch you!\n You are a prisoner on a swamp!")
            print('''
                                            ,---._
                                         ,~~,-._  `._
                                          v'~   `-.  `.
                                               _,- ~.  |
                                             .'  ,--`.  `\_
                                             V-'~ ,'~~~`-. `-.
                                 ___             /_/~~~) ` `. `._
                        ____,---'   ;            V     `.__ `--, `;
                         `-._    ;  `.                ____)       :
                             `.;  ; .'              ,'        _    |
                              ; |   ;              ,';'~~~`--' `;  :
                             ,': .-'               `,'  __ __   :  |
                             )_  `-, ___     __        (__:__)   ; ;
                        _,---. \___,'` ~`---;  `-.       |||    ;  ;
                    _,-/   :;     !   `     `|    `-.   |~~~~|   ; :
                _,-' /~   .,'  ;  !!  `..    ``.    `.  :    ;  | :
              ,'  ,-'    .;   `; !!   _,'-' ,--._    ====\__/===: `.
            .'  ,-'   ,--.  ~~`-. !!  ~    ,'    `     `./  \   |  |
           .'  :;   ,'    \        !: .   ;--.__   `;.  |. ~.|   : ;
          .'  ,;    ' ,-'~~`-.     ,!  ;-'     #;   `;. \____/  : `.
         .'  ,;      /__      `-._,'!!( _(0'~~`-'    `;.  `.     ; ;
        .'  ,;    ,'    `---._(0))  !! ~   _,-,        `;  `.   ;  :
        ;  ,;    ,' ;;-.__,-._~~~   !!__,--::::|.      `;:  :   `; )
        ;  :|   ,'  ;/;;; :::;;;;----'|:: |::;\/#.      `;  |    ) ;
        :  |:  ,'  ,' :/  :;; \/))):;;::/  ::' ##:      ;;  ;    ; |
        |  :|  :;  :      `'    \/ \/ `'   `'  ##;      ;  .'  ,'  ;
        :  |;  || .'        ;\.   ____ __,--._ ##;     ;' .'--'   ;
    _,--`. `.  :: `./;   /\/;:;,-'    `-.     `--.__     .'~   ,'~
   /     ;. `; ``. :::;\;.-'~~`./~~\/\ ..    _  :::  --. ' ,-'~
  /    .  `. `; `   ~~~ ;~      ~~~~~~`--.__~~`-. :::   ) ~
 /'    ;`--`. `. `.    :;      `;       ;   `---`._    ,'
 `.  \/      `-.` `_,_ `:,-'-. `.      :_,_    ;   `--'
  `.  `.        ` (___)-: ( ) :--,-'- -(___),'~~~`.
   {_  `.               `.___.' ( ; ;)      :((:)):
     `.  `                       `--'       `.___.'
       `. `.                 ;;:::;
        `-  `.              ;;;. .;
          `-. `.__        ||\;;; - ;; //
             `. ` `--..___ ||,--v-, //     
               `--._   ~~~~~`)____(//
                    )    ~~   ~~~~~~;
                    `.    ~~  ------;
                     `.~~_   ______,' 
                      `. `.--';: |:
                       ;  `. Cc; Cc
                       `.  ;  __
                        `. `-'  ~|
                         `-.__,--'~
            
            ''')
            print("You stay there forever!\n   !!!   You loose   !!!")
        elif third == "sl":
            print("There is a big hole!\n You are falling into the water where big sharks lives!\n Sharks eats you for dinner!")
            print('''
                    ^`.                     o
     ^_              \  \                  o  o
     \ \             {   \                 o
     {  \           /     `~~~--__
     {   \___----~~'              `~~-_     ______          _____
      \                         /// a  `~._(_||___)________/___
      / /~~~~-, ,__.    ,      ///  __,,,,)      o  ______/    |
      \/      \/    `~~~;   ,---~~-_`~= \ \------o-'            |
                       /   /            / /
                      '._.'           _/_/
                                      ';||
            
            ''')
            print("     !!!   You loose   !!!")
        elif third == "r":
            print("You have found laughing skeletons!\n They follow you, captures you and keep you in cage made from bones!")
            print('''
                       ______
                    .-"      "-.
                   /            |
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/   jgs                              \_)

            
            ''')
            print("   !!!   You loose   !!!")
        elif third == "SR":
            print("You have found a hole with water, but you are brave one so you manage to go through it")
            print("You can see a statue with place like for coin")
            print('''
               ||||////
                |.)(.|
                | || |
                \(__)/
                |-..-|
                |o\/o|
           .----\    /----.
          / / / |~~~~| \ \ |
         / / / /|::::|\ \ \ |
        '-'-'-'-|::::|-'-'-'-'
               (((^^)))
                >>><<<
                ||||||
                (o)(o)
                | /\ |
                (====)
                |_/\_|
                (_/\_)
               _|_,__|_
              (___\____)
            
            ''')
            print("On the ground in front of the statue you can see three 'X' marks\n You need to choose where you will dig" )
            fourth_choice = input("Which 'X' mark do you choose?\n L - left\n M - middle\n R - right")
            fourth = fourth_choice.lower()
            if fourth == "l":
                print(""" !!! YOU WON !!! \n Congratulations!!! \n You have found treasure chest !!!\n\n Inside this chest you have found delicious magical ice cream (never melting)!!! \n ENJOY
                
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           |'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'

                """)
            elif fourth == "m":
                print(" You have found:\n \n Bone")
                print("You loose")
                print("""
                      .-.               .-.
                     (   `-._________.-'   )
                      >=     _______     =<
                     (   ,-'`       `'-,   )
                      `-'               `-'
                """)

            elif fourth == "r":
                print(" !!! YOU LOOSE !!!\n\n You have notfound treasure\n You just found old alien skull !!!")
                print("""
                         .AMMMMMMMMMMA.
                       .AV. :::.:.:.::MA.
                      A' :..        : .:`A
                     A'..              . `A.
                    A' :.    :::::::::  : :`A
                    M  .    :::.:.:.:::  . .M
                    M  :   ::.:.....::.:   .M
                    V : :.::.:........:.:  :V
                   A  A:    ..:...:...:.   A A
                  .V  MA:.....:M.::.::. .:AM.M
                 A'  .VMMMMMMMMM:.:AMMMMMMMV: A
                :M .  .`VMMMMMMV.:A `VMMMMV .:M:
                 V.:.  ..`VMMMV.:AM..`VMV' .: V
                 V.  .:. .....:AMMA. . .:. .V
                  VMM...: ...:.MMMM.: .: MMV
                      `VM: . ..M.:M..:::M'
                       `M::. .:.... .::M
                        M:.  :. .... ..M
                        V:  M:. M. :M .V
                        `V.:M.. M. :M.V'
                              """)

            else:
              print("Plese select walid option!")



        else:
            print("Wrong choice! \n Try Again and follow instructions!")



    else:
        print("Wrong choice! \n Try Again and give valid option!")


else:
    print("Wrong choice! \n Try Again!")

