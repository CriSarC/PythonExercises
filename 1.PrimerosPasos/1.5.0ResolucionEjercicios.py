#Solucion ejercicios 

##Primer Ejercicio##

Texto = 'Te quiero solo como amigo'

#Primer y segundo Punto#

P2Caracteres = Texto[:2] #Primeros dos Caracteres de la cadena
ContarCaracteres = len(Texto) #Cuenta cuantos caracteres tiene la cadena
U3Caracteres = Texto[ContarCaracteres-3:ContarCaracteres] #Ultimos tres Caracteres de la cadena

print(P2Caracteres)
print (U3Caracteres)
print(Texto[-3:])


#Tercer Punto#

ContarCaracteres = len(Texto) #Cuenta cuantos caracteres tiene la cadena
NuevaCadena = "" #Crea una cadena vacia para depues llenarla
for Caracter in range(0, ContarCaracteres,2): #Ciclo que obtiene el espacio donde estan los caracteres comenzando en zero hasta ContarCaracteres con paso de dos en dos
    
    SaltosCaracter = Texto[Caracter] #Se obtienen los Caracteres en dichos espacios
    NuevaCadena +=  SaltosCaracter #Se agregan los caracteres en la cadena vacia
    
print(NuevaCadena) #se imprime en pantalla la nueva cadena

print (Texto[::2])

#Cuarto Punto#
 
ContarCaracteres = len(Texto) #Cuenta cuantos caracteres tiene la cadena
ContarCaracteresInversos = len(Texto) -1 #Cuenta cuantos caracteres tiene la cadena, como cada caracter tiene un numero de posicion asignado comenzando desde el zero si para este ejemplo al contar los caracteres hay 25 caracteres(comenzando desde el 1), para python habran 24 espacios 0,1,2,3...23,24, por lo tanto si pedimos el caracter 25 se generara un error, a lo que se soluciona restandole un -1 
NuevaCadenaInvertida = "" #Crea una cadena vacia para depues llenarla
for Inverso in range(0, ContarCaracteres): #Ciclo que obtiene el espacio donde estan los caracteres comenzando en zero hasta ContarCaracteres con paso de dos en dos
    
    CaracterInverso = Texto[ContarCaracteresInversos - Inverso] #Se obtienen los Caracteres en dichos espacios
    NuevaCadenaInvertida +=  CaracterInverso #Se agregan los caracteres en la cadena vacia
    
print(NuevaCadenaInvertida) #se imprime en pantalla la nueva cadena

print(Texto[::-1])

#Quinto Punto#

print (Texto + NuevaCadenaInvertida)

print(Texto+Texto[::-1])
##Segundo Ejercicio##
#%% colocar comas 
Palabra = 'Separar'

NewPalabra = ''
for letter in Palabra:
    NewPalabra += letter + ',' 
print(NewPalabra)


NewLetra = ''
NewPalabra2 = ''
for letter2 in Palabra:
    NewLetra = letter2
    NewPalabra2 += NewLetra.replace(letter2,letter2 + ',') 
print('Esta Es: ' , NewPalabra2)

#%% CHR, ORD, SPLIT, JOIN

# Variable = chr(122) #chr me da la letra que representa un numero y orb me da el numero que representa una letra


# Abcedario = ''
# AbcedarioComa = ''
# for NLetra in range(97,123):
#     Letra = chr(NLetra)
#     Coma = ', '

#     Abcedario += Letra #+ ' '
#     AbcedarioComa += Letra + Coma

# print (Abcedario)
#VectorAbcdario = Abcedario.split()
# print (VectorAbcdario)
# print(AbcedarioComa)

# AbcedarioComaTroceado = AbcedarioComa.split() #Descompone el String partiendolo en cada espacio si dijera split(,) lo parteria en cada coma, para unir se usa join()
# print (AbcedarioComaTroceado)

# for letra in Abcedario:
#     print("El valor de {} es {}".format(letra, ord(letra)))
#     NumRemplazar = ord(letra)
#     for cara in Palabra:
#         Remplazar = ord(cara)
#         if Remplazar = NumRemplazar then:
#             NuevaPalabra = Palabra.replace(cara,cara+',')
    
# f = 'r'
# fr = f.replace(f,f + ',')    
# print (fr)

#%%Encuentra Los Bugs

# El siguiente fragmento de código contiene 7 errores, revisa minuciosamente 
# el código, encuentra los errores y soluciónalos. No uses el editor de texto 
# para encontrarlos, trata de revisar el código desde acá y cuando encuentres todos 
# los errores, transcribe tu programa corregido al editor y verifica que funcione.



variable1 = 'Este es un ejemplo de variable de texto'

variable2 = 5901.3333

variable3 = 109293485;

variable4 = 'Ejemplo de cadena de texto'

print(variable1)

print(variable2)

print(variable3)

print(variable4)
