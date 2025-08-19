print('''                                       ___.-----.______
                                   ___.-----'::::::::::::::::`---.___
                _.--._            (:::;,-----'~~~~~`----::::::::::.. `-.
   _          .'_---. `--.__       `~~'                 `~`--.:::::`..  `..
  ; `-.____.-' ' {0} ` `--._`---.____                         `:::::::: : ::
 :_^              ~   `--.___ `----.__`----.____                ~::::::.`;':
  :`--.__,-----.___(         `---.___ `---.___  `----.___         ~|;:,' : |
   `-.___,---.____     _,        ._  `----.____ `----.__ `-----.___;--'  ; :
                  `---' `.  `._    `))  ,  , , `----.____.----.____   --' :|
                        / `,--.\    `.` `  ` ` ,   ,  ,     _.--   `-----'|'
 _.~~~~~~._____    __./'_/'     :   .:----.___ ` ` ` ``  .-'      , ,  :::'
                 ///--\;  ____  :   :'    ____`---.___.--::     , ` ` ::'
                 `'           _.'   (    /______     (   `-._   `-._,-'
    ()  ()                 .-' __.-//     /_______---'       `-._   `.
  * *(o)'      ~~~        /////    `'       ~~~~~~      ~~ ______;   ::.
  `\ )( /*                `'`'                            /_______   _.'
    {()}      ,     ~~~                  ~~~~~~~~           /___.---'  --__
     !|       `                                              ~~~
  ~~~~~~~~
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')


print('Welcome to Treasure Island!\nYour mission is to find the treasure.\n')
choice1 = input("You're at a crossroad, where do you want to go? Type 'left' or 'right': ").lower()

if choice1 == 'right':
    print("You fell into a hole. Game over")
else:
    print("You've come to a lake, there is an island in the middle of the lake.\n")
    choice2 = input('''Do you want 'swim' or 'wait'? 
    Type 'wait' to wait for a boat or type 'swim' to swim across.''').lower()

    if choice2 == 'swim':
        print("Attacked by trout. Game over.")
    else:
        print("Next question for you.")
        choice3 = input("Which door would you want to open? 'red', 'blue', 'yellow': ").lower()
        
        if choice3 == 'red':
            print("Burned by fire. Game over.")
        elif choice3 == 'yellow':
            print("You Win!")
        else:
            print("Eaten by beasts. Game over!")
