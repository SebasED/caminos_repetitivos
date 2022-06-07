"""
    El capitán del barco pirata Thousand Sunny, el famoso Monkey D. Luffy te ha designado 
    para que sirva de vigía en el mástil principal. Esto es lo que te ha dicho el capitán:
    Tu misión es simple marinero, pero importante para la tripulación, cuando veas alguna 
    de estas criaturas debes decirlo de esta manera:

    • ¡Ahoy! capitán, un Kraken
    • ¡Ahoy! capitán, unas Sirenas
    • ¡Ahoy! capitán, una Ballena
    • ¡Ahoy! capitán, un Hipocampo
    • ¡Ahoy! capitán, una Macaraprono
    • ¡Ahoy! capitán, un Pulpo
    • ¡Ahoy! capitán, unos Leviatanes
    • ¡Ahoy! capitán, Unas Hidras

    Tu vida va en ello marinero, debes pronunciarlos con el articulo correcto de acuerdo con 
    su especie (uno, una, unos, unas).
    Además, debes decir la dirección del barco por la que aparece la criatura:

    • A babor
    • A estribor
    • Por la proa
    • Por la popa

    Para cumplir la misión debes crear un programa que, dada la criatura y la ubicación, 
    construya la cadena correcta. El programa se debe ejecutar las veces que sea necesario
    hasta que el capital te diga “stop”.
    Por ejemplo, si aparecen:

    • Kraken y Babor debe decir: ¡Ahoy! capitán, un Kraken a babor.
    • Leviatanes y Proa debe decir: ¡Ahoy! capitán, unos Leviatanes por la proa.

    Y así hasta que ingresen la palabra para detener el programa.
"""


"""
necessary variables for the program
    creature: str
    directin: str
    stop: bool
    message: str
"""
creature = ""
direction = ""
stop = False
message = ""


"""
This code shows all options for creatures and save it in the creature variable. The code will repeat until
the user chooses a correct option
"""
while True:
    # Show the different criatures options
    print("\n\
    Which creature are you seeing?  \n\
        Kraken \n\
        Sirenas \n\
        Ballena \n\
        Hipocampo \n\
        Macaraprono \n\
        Pulpo \n\
        Leviatanes \n\
        Hidras \n\
        \n\
    choose an option: ")                              
    creature = input().capitalize()

    # If the user choose a validate option, the loop will finish
    if creature == "Kraken":
        break
    elif creature == "Sirenas":
        break
    elif creature == "Ballena":
        break
    elif creature == "Hipocampo":
        break
    elif creature == "Macaraprono":
        break
    elif creature == "Pulpo":
        break
    elif creature == "Leviatanes":
       break
    elif creature == "Hidras":
        break
    else:
        print("Choose a correct option")

"""
This code shows all options for direction and save it in the creature variable. The code will repeat until
the user chooses a correct option
"""
while True:
    # Show the different directions options
    print("\n\
    which direction the creature is?  \n\
        Babor \n\
        Estribor \n\
        Proa \n\
        Popa \n\
        \n\
    choose an option: ")                              
    direction = input().lower()

    # If the user choose a validate option, the loop will finish
    if direction == "babor":
        break
    elif direction == "estribor":
        break
    elif direction == "proa":
        break
    elif direction == "popa":
        break
    else:
        print("Choose a correct option")

"""
This code shows the final message and repeat it until the user type the "stop" word
"""
while not stop:
    # concatenate the first part of the final message based on the choossed creature
    if creature == "Kraken":
        message = "¡Ahoy! capitán, un Kraken"
    elif creature == "Sirenas":
        message = "¡Ahoy! capitán, unas Sirenas"
    elif creature == "Ballena":
        message = "¡Ahoy! capitán, una Ballena"
    elif creature == "Hipocampo":
        message = "¡Ahoy! capitán, un Hipocampo"
    elif creature == "Macaraprono":
        message = "¡Ahoy! capitán, una Macaraprono"
    elif creature == "Pulpo":
        message = "¡Ahoy! capitán, un Pulpo"
    elif creature == "Leviatanes":
        message = "¡Ahoy! capitán, unos Leviatanes"
    elif creature == "Hidras":
        message = "¡Ahoy! capitán, Unas Hidras"
    
    # concatenate the second part of the final message based on the choossed direction
    if direction == "babor":
        message = message + " a babor"
    elif direction == "estribor":
        message = message + " a estribor"
    elif direction == "proa":
        message = message + " por la proa"
    elif direction == "popa":
        message = message + " por la popa"

    # Show the final message
    print(message) 
    print() 

    # Condition for stopping the program
    if input().lower() == "stop":
        stop = True