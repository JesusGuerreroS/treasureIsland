#############################################
#very simple minimage of the treasure-island
#############################################
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
print("Bienvenido a la isla del tesoro.")
print("Tu misión es encontrar el tesoro.") 

#first path
option = input('Tu estas en una intersección de caminos. A donde quieres ir? "izquierda" o "derecha"')

if option == "izquierda":
    #second path
    option = input('''Te encuentras en un mini lago para poder cruzar a la otra orilla. Escribe "esperar" para esperar por un bote. Escribe "nadar" para nadar hacia la otra orilla :\n''')

    if option == "esperar":
        #third path
        option = input('''Llegas a la otra orilla y te encuentras con un castillo de tres puertas una de color "roja" "azul" y "amarilla".. Entonces eliges una: \n''')

        if option == "roja":
            print("Te consumen las llamas. Perdiste!")

        elif option == "azul":
            print("Eres devorado por una enorme bestia. Perdiste!")
        elif option == "amarilla":
            #end of the game
            print("Excelente acabas de encontrar el tesoro.. Acabas de Ganar!!!")
        else:
            print("Perdiste!!!!")
    else:
        print("Atacado por un tiburon.. Perdiste!")

else:
    print("Acabas de caer en un agujero, Perdiste!")