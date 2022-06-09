"""
En 1590 Galileo presentó las leyes de la caída libre:
    Sin resistencia los cuerpos caen a la misma velocidad
    independientemente de su masa, forma y composición.
    Cuando se lanza un objeto la distancia que recorre es
    proporcional al tiempo d = v * t ± (1/2) * g * t^2, donde:
    
        • d es la distancia recorrida.
        • g es la aceleración originada por la gravedad es decir 9.8𝑚/s^2.
        • t es el tiempo transcurrido.

Esta y otras afirmaciones le valieron a Galileo una amable invitación a
beber la Cicuta, pero finalmente fue condonada su pena a cadena Perpetua.

En honor al gran científicoGalilei, se debe implementar una aplicación que 
dada una altura en metros de un edificio del que se va a lanzar una esfera,
vaya mostrando la distancia recorrida segundo a segundo hasta tocar el suelo.
"""

"""
necessary variables for the program
    time: int
    distance: float
    GRAVITY: float
"""

#  Initialize variables
time = 0
GRAVITY = 9.8
BUILDING_HEIGHT = float(input("Enter the height of the building in meters: "))
distance = BUILDING_HEIGHT
while distance >= 0:
    distance = BUILDING_HEIGHT
    aux_distance = (1/2) * GRAVITY * time**2
    distance -= aux_distance
    if distance <= 0:
        break
    print(f"The building height is {distance} meters in the second {time}")
    time += 1
    