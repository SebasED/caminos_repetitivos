"""
El funcionamiento de los radares de velocidad se basa en un principio básico de la cinética que 
establece 𝑣 = 𝑥 / 𝑡, donde:

v: velocidad
x: posición – distancia
t: tiempo

El  radar  envía  dos  haces  de  luz en cierto tiempo (en segundos) y obtiene la distancia del vehículo 
al radar en cada haz de luz enviado, así puede calcular la velocidad del vehículo y establecer si está en 
los límites  permitidos  o  por  el  contrario  debe  ser  multado.  El  radar  toma estos datos en metros.

Dadas las dos distancias obtenidas del vehículo y el tiempo, calcular si debe pagar una multa de acuerdo con 
la siguiente tabla:

|  Velocidad (km/h)  |                   Multa                       |
|--------------------------------------------------------------------|
|    De 1 a 20       |   Llamado de atención por baja velocidad.     |
|    De 21 a 60      |   Normal                                      |
|    De 61 a 80      |   Llamado de atención por alta velocidad.     |
|    De 81 a 120     |   Multa tipo I                                |
|    Más de 120      |   Multa tipo II e inmovilizacióndel vehículo. |

En caso de tener multapor velocidad, se le practica un examen de alcoholemia al conductor que acarrea multas
adicionales de acuerdo con la siguiente norma:

    • Entre 20 y 39 mg de etanol/l00 ml de sangre total, además de las sanciones previstas en la presente ley,
      se decretará la suspensión de la licencia de conducción entre seis (6) y doce (12) meses.
    • Primer grado de embriaguez entre 40 y 99 mg de etanol/100 ml de sangre total, adicionalmente a la sanción
      multa, se decretará la suspensión de la Licencia de Conducción entre uno (1) y tres (3) años.
    • Segundo grado de embriaguez entre 100 y 149 mg de etanol/100 ml de sangre total, adicionalmente a la 
      sanción multa, se decretará la suspensión de la Licencia de Conducción entre tres (3) y cinco (5) años, 
      y la obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y
      drogadicción en centros de rehabilitación debidamente autorizados, por un mínimo de cuarenta (40) horas.
    • Tercer grado de embriaguez, desde 150mg de etanol/100 ml de sangre total en adelante, adicionalmente a la
      sanción de la sanción de multa, se decretará la suspensión entre cinco (5) y diez (10) años de la Licencia 
      de Conducción, y la obligación de realizar curso de sensibilización, conocimientos y consecuencias de la
      alcoholemia y drogadicción en centros de rehabilitación debidamente autorizados, por un mínimo de ochenta 
      (80) horas.
"""

"""
necessary variables for the program
    speed: float
    time: float
    distance_1: float
    distance_2: float
    etanol = float
    blood_alcohol: float
"""

"""
assign values to variables
"""
distance_1 = float(input("Distance 1: "))
distance_2 = float(input("Distance 2: "))
time = float(input("Time: "))

# calculate the speed
speed = (distance_2 - distance_1) / time
# go from m/s to km/h
speed = (speed * 60 * 60) / 1000

"""
code to display results based on the data obtained
"""
# Options based on speed
if speed <= 20:
    print(f" your speed is the {speed} km/h, please drive faster")
elif speed > 20 and speed <= 60:
    print(f" your speed is the {speed} km/h, very good!")
elif speed > 60 and speed <= 80:
    print(f" your speed is the {speed} km/h, please drive slower")
elif speed > 81:
    if speed <= 120:
        print(f" your speed is the {speed} km/h, you have a 'type I' traffic ticket")
    else:
        print(f" \tyour speed is the {speed} km/h, you have a 'type II' traffic ticket and \n\
        'immobilization of the vehicle'")
    
    # calculate the blood alcohol level
    etanol = float(input("etanol level: "))
    blood_alcohol = etanol / 100
    
    # Options based on blood alcohol level
    if blood_alcohol >= 0.2 and blood_alcohol < 0.4:
        print("\tFurthermore, you have alcohol in your blood. So, your driver's license will \n\
        be suspended between six (6) to twelve (12) months.")
    elif blood_alcohol >= 0.1 and blood_alcohol < 1:
        print("\tFurthermore, you have first degree of intoxication. So, your driver's license \n\
        will be suspended between one (1) to three (3) years.")
    elif blood_alcohol >= 1 and blood_alcohol < 1.5:
        print("\tFurthermore, you have second degree of intoxication. So, your driver's license \n\
        will be suspended between three (3) to five (5) years and the obligation to take a \n\
        course on awareness, knowledge and consequences of alcohol and drug addiction in duly \n\
        authorized rehabilitation centers, for a minimum of forty (40) hours. ")
    elif blood_alcohol >= 1.5:
        print("\tFurthermore, you have second degree of intoxication. So, your driver's license \n\
        will be suspended between five (5) to ten (10) years and the obligation to take a \n\
        course on awareness, knowledge and consequences of alcohol and drug addiction in duly \n\
        authorized rehabilitation centers, for a minimum of forty (80) hours. ")
    