# %%Ejercicio 1

# Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden
#  las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos 
#  últimas tiene que decir que riman un poco y si no, que no riman.

Palabra1 = input('Ingresa una palabra: ')
Palabra2 = input('Ingresa otra palabra: ')

if len(Palabra1) and len(Palabra2) < 3:
#if len(Palabra1) < 3 or len(Palabra2) < 3:
    print('Las palabras no pueden rimar')
elif Palabra1[-3:] == Palabra2[-3:]:
    print('Las Palabras Riman')
elif Palabra1[-2:] == Palabra2[-2:]:
    print('Las palabras riman un poco')
else:
    print('Las palabras no riman')

#%% Ejercicio 2

# Crear un programa que permita al usuario elegir un candidato por el cual votar.
#  Las posibilidades son: candidato A por el partido rojo, candidato B por el 
#  partido verde, candidato C por el partido azul. Según el candidato elegido
#  (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido 
#  [color que corresponda al candidato elegido]”. Si el usuario ingresa una opción
#  que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.

# Pista: Si la letra ingresada por el usuario es en minúscula, el programa debe
#  convertirla en mayúscula

print('Bienvenide a la Votación! \n le recordamos los tres candidatos: \n candidato A por el partido rojo\n candidato B por el partido verde\n candidato C por el partido azul')

Voto = input('Ingrese su votación: ')

if Voto.upper() == 'A':
    print('Usted votó por el partido rojo')
elif Voto.upper() == 'B':
    print('Usted votó por el partido verde')
elif Voto.upper() == 'C':
    print('Usted votó por el partido azul')
else:
    print('Opción erronea')

#%%¡Encuentra los BUGS!

# El siguiente fragmento de código tiene un total de aproximadamente 8 Bugs. 
# Ya sabes... tu labor es encontrarlos, luego, corregir dichos errores y
#  verificar con tu editor de código que todo esté bien


Nombre = input('Ingresa tu nombre: ')


if Nombre == "Maria":

    print('Hola Maria')

elif Nombre == "Carlos":

    print("Hola Carlos")

elif Nombre == 'Juan':

    print("Hola Juan")

else:

    print("No te tengo en mis registros")