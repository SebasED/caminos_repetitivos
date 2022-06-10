"""
La siguiente gráfica muestra elcomportamiento de los descendientes y ascendientes  
de una persona, si asumimos que esta persona es la generación 0, lageneración 1 serán
dos personas (sus padres) la generación 2 serán 4 personas (sus abuelos) y así 
sucesivamente. 

Debe crear un programaque dada una generación (mayor o igual a cero):
- Le indique al usuarioelnúmero total de personas de la familia (de todas las generaciones 
  hasta la generación dada).
- Muestre el número de personas de cada generación mientras hace el cálculo.
"""


"""
necessary variables for the program
    generations_number: int
    total_persons: int
"""

#  Initialize variables
total_persons = 0
number_generations = int(input("Enter the generations number from 0 onwards: "))

# For from 0 to the number_generatons' value
for i in range(number_generations + 1):
      # The number of people per generation is the result of 2 ** generation
      persons_for_generation = 2**i
      # Add the people per generation in each iteration
      total_persons += persons_for_generation
      
      print(f"In the generation {i} there are {persons_for_generation} persons")

print(f"The total members of your family in the whole generations are: {total_persons}")
      
