"""
Dadas dos listas, se debe crear un programa que genere una tercera lista
con los elementos que se repiten en las dos anteriores listas sin repetirse
ningún elemento en lanueva lista.
    Lista 1: [‘h’, ‘e’, ‘l’, ‘l’, ‘o’, ‘‘, ‘t’, ‘e’, ‘a’, ‘m’]
    Lista 2: [‘h’, ‘e’, ‘l’, ‘l’, ‘o’, ‘ ‘,‘w’, ‘o’, ‘r’, ‘l’, ‘d’]
"""

"""
necessary variables for the program
    list_1: List
    list_2: List
    list_3: List
"""

#  Initialize variables
list_1 = ['h','e','l','l','o',' ','t','e','a','m']
list_2 = ['h','e','l','l','o',' ','w','o','r','l','d']
list_3 = []

# Add to list_3 the repet values in list_1
for index, value in enumerate(list_1):
    if value in list_1[index + 1:]:
        list_3.append(value)

# Add to list_3 the repet values in list_2
for index, value in enumerate(list_2):
    if value in list_2[index + 1:]:
        # If the value is already in list 3, do not add that value
        if value in list_3:
            continue
        else:
            list_3.append(value)

# Print new list
print(list_3)
        