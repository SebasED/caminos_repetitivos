"""
Se debe crear un programa que dada una longitud en cuadros (mayor a cero), genere un tablero,
como en la siguiente imagen (Es un tablero con una longitud de 8x8):
"""

"""
necessary variables for the program
    frame_length: int
    figura_1 = str
    figura_2 = str
"""

#  Initialize variables
frame_length = int(input("Enter the frame lenght: "))
figura_1 = ""
figura_2 = ""

# In this for I get the 2 rows for creating the whole board
for i in range(8):
    if i % 2 == 0:
        figura_1 += "  " * frame_length
        figura_2 += " *" * frame_length
    else:
        figura_1 += " *" * frame_length
        figura_2 += "  " * frame_length

# In this for I print each row based on the frame_length's value
for i in range(8):
    for j in range(frame_length):
        if i % 2 == 0:
            print(figura_1)
        else:
            print(figura_2)
        
