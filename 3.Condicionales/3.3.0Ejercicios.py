#%% Ejercicio 1

# Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje
#  "Es vocal". Sino, decirle al usuario que no es vocal

Letra = input('Porfavor ingrese una letra: ')

if Letra == 'a' or Letra == 'e' or Letra == 'i' or Letra == 'o' or Letra == 'u':
    print('La letra {}, Es vocal'.format(Letra))
else:
    print('La letra que ingreso no es vocal')
    
if Letra in 'aeiou':
   print('Es una Vocal')
else:
   print('Es una letra')    
             

#%% Ejercicio 2

# Escribir un programa que, dado un número entero, muestre su valor absoluto.
#  Nota: para los números positivos su valor absoluto es igual al número 
#  (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto
#  es el número multiplicado por -1 (el valor absoluto de -52 es 52).

Entero = float(input('Ingrese un número: '))

Curiosity = type(Entero)

if type(Entero) != int:
    print('El valor absolto de {} es: {}'.format(Entero,abs(Entero)))
else:
    print('El número ingresado no es Entero')    

# #%% ejercicio222

# while True:
#     n = raw_input("ingrese numero jugadores: ") 

#     try: 
#      n = int(n)
#      return n
# # except ValueError:
# # print("Escribe un numero, no una letra.")