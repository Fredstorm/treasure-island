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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line 👇
decision1 = input("As you follow your map, you realise that there is an unexpected dead end. You are faced with a road that splits to the **left** and to the **right**. Which way will you go? ")
decision1 = decision1.lower()

if decision1 == "right":
  print("As you take a step onto the right side trail, the ground parts beneath you and you fall to your death.") 
  print("Game Over.")
  exit()
else:
  decision2 = input("After a long trek on the left side trail, you reach the shore. In the distance you can see the infamous treasure island. Will you **swim** to the island or **wait** for a boat? ")

decision2 = decision2.lower()
if decision2 == "swim":
  print("You strip down to your underwear and dive into the water. As you enter the water a swarm of piranhas appear around you and eat you.")
  print("Game Over")
  exit()
else:
  decision3 = input("You wait for about 15 minutes before a deserted boat drifts to the shore. You board the boat and head towards the treasure island. When you arrive at the island, you enter a ruined temple and are confronted by three doors. Will you go through the **red**, **yellow**, or **blue** door? ")

decision3 = decision3.lower()
if decision3 == "red":
  print("As you turn the doorknob and open the red door, flames gush out through the door. You slam the door shut but it is too late, you are turned to a pile of ashes.")
  print("Game Over.")
elif decision3 == "yellow":
  print("As you turn the doorknob and open the yellow door, you are greeted with a sight of beauty. A pile of gold with a treasure chest sitting atop it greets you. You walk towards the treasure chest and flip it open. You are blinded by the bright sheen of a diamond crown.")
  print('''                                    o
                                   $""$o
                                  $"  $$
                                   $$$$
                                   o "$o
                                  o"  "$
             oo"$$$"  oo$"$ooo   o$    "$    ooo"$oo  $$$"o
o o o o    oo"  o"      "o    $$o$"     o o$""  o$      "$  "oo   o o o o
"$o   ""$$$"   $$         $      "   o   ""    o"         $   "o$$"    o$$
  ""o       o  $          $"       $$$$$       o          $  ooo     o""
     "o   $$$$o $o       o$        $$$$$"       $o        " $$$$   o"
      ""o $$$$o  oo o  o$"         $$$$$"        "o o o o"  "$$$  $
        "" "$"     """""            ""$"            """      """ "
         "oooooooooooooooooooooooooooooooooooooooooooooooooooooo$
          "$$$$"$$$$" $$$$$$$"$$$$$$ " "$$$$$"$$$$$$"  $$$""$$$$
           $$$oo$$$$   $$$$$$o$$$$$$o" $$$$$$$$$$$$$$ o$$$$o$$$"
           $"""""""""""""""""""""""""""""""""""""""""""""""""""$
           $"                                                  o
           $"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$$
''')
  print("You Win!")
else:
  print("As you turn the doorknon and open the blue door, a growl eminates from the room. You slam the door shut instantly before it is ripped open by a pack of wild wolves. You are eaten alive.")
  print("Game Over.")
