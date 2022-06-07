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

# Show creatures options and saves in a variable
while True:
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
    if creature == "Kraken":
        pass

# Show direction options and saves in a variable 
print("\n\
which direction the creature is?  \n\
    Babor \n\
    Estribor \n\
    Proa \n\
    Popa \n\
    \n\
choose an option: ")                              
direction = input().capitalize()

# Variable for stopping the loop
stop = True

while stop:
    message = ""
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
    else:
        print("")
        
    