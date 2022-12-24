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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome Treasure Island!")
print("Your mission is to find the treasure.")
number_of_lives = 3

while number_of_lives != 0:
    action_1 = str(input("Go (l)eft or (r)ight?: "))

    if action_1 == 'l':
        action_2 = str(input("(s)wim or (w)ait?: "))
        if action_2 == 's':
            print('You were attacked by trout!')
            number_of_lives -= 1
            if number_of_lives == 1:
                print(f'You have {number_of_lives} life left')
            else:
                print(f'You have {number_of_lives} lives left.')
        else:
            action_3 = str(input("3 colored doors have appeared! Which Door? (R)ed, (B)lue, or (Y)ellow?: ")).lower()
            if action_3 == 'r':
                print("You were burned by fire!")
                number_of_lives -= 1
                if number_of_lives == 1:
                    print(f'You have {number_of_lives} life left')
                else:
                    print(f'You have {number_of_lives} lives left.')
            elif action_3 == 'b':
                print("You were eaten by beasts!")
                number_of_lives -= 1
                if number_of_lives == 1:
                    print(f'You have {number_of_lives} life left')
                else:
                    print(f'You have {number_of_lives} lives left.')
            elif action_3 == 'y':
                print("You've found the treasure! You Win!")
            else:
                print("Game Over.")
    else:
        print('You fell into a hole !')
        number_of_lives -= 1
        if number_of_lives == 1:
            print(f'You have {number_of_lives} life left')
        else:
            print(f'You have {number_of_lives} lives left.')
print('Game Over!')
input()
