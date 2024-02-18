print(''''
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
/______/______/______/______/______/______/______/______/______/______/[Shevron]
*******************************************************************************      
''')

print("welcome to the Treasure Island, your journey begins.")

option_1 = input('Which way do you want to go?, "left" or "right". ').lower()

if option_1 == "left":
  option_2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
  if option_2 == "wait":
    option_3 = input('You arrived at the island unharmed. There is a house with 3 doors. One "red", one "Yellow" and one "Blue". Which colour do you choose? ').lower()
    if option_3 == "red":
      print("You ran into a room full of fire, game over!!!")
    elif option_3 == "yellow":
      print("You found the treasure, YOU WIN !!!")
    elif option_3 == "blue":
      print("You ran into a room full of beasts, game over!!!")
    else:
      print("Wrong input, game over!!!")
  else:
    print("You got attacked by a trout, game over!!!")
else:
  print("You fell into a hole, game over!!!")