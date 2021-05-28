#%%Ejercicio 1

# En el siguiente diccionario se encuentran capitales de los paises en el mundo, 
# debes realizar un programa que pida un pais al usuario, y muestre la capital de
#  ese pais, en dado caso el pais no este en el diccionario, se debe mostrar un
#  mensaje diciendo que ese pais no se encuentra.

# {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras",
#  "Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", 
#  "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

Paises = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

Pais = input('Ingresa el nombre de un pais Hispanohablante: ')
print(Pais.capitalize()) #coloca la primera letra en mayuscula

if Pais.capitalize() in Paises:
    print(Paises[Pais.capitalize()])
else:
    print('El Pais no se encuentra')

#%%Ejercicio 2

# Con el siguiente diccionario, debes crear un programa que pregunte al usuario
#  por un número; el programa debe imprimir el jugador al que hace referencia 
#  ese número

# {

#     1 : "Casillas", 15 : "Ramos",

#     3 : "Pique", 5 : "Puyol",

#     11 : "Capdevila", 14 : "Xabi Alonso",

#     16 : "Busquets", 8 : "Xavi Hernandez",

#     18 : "Pedrito", 6 : "Iniesta",

#     7 : "Villa"

# }


Jugadores = {

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

}

NumeroJ = int(input('Ingrese el número de un Jugador: '))
print(Jugadores[NumeroJ])

#%%¡Encuentra los BUGS!

# Para este fragmento, solo puedo decirte que tiene muchos Bugs; considera que 
# cuando hay un signo de ">>>", significa que ese va ser el resultado que el
# programa debería mostrar al ser ejecutado. Por ejemplo: print("Hola Mundo") >>> Hola Mundo


lista = [1,2,3,4,5]

Diccionario = {"Uno": 1, "Dos": 2, "Tres": 3, "Cuatro": 4}

tupla = (6,7,8,9,10)


print(lista[0])

#>>> 1


print(Diccionario["Dos"])

#>>> 2


print(tupla[2])

#>>>8