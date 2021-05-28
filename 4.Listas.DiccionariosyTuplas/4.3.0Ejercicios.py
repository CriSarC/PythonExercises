#%%Ejercicio 1

# Escribir una tupla con los meses del año, luego, pide al usuario un numero, el 
# que haya ingresado, es el mes que debe mostrar en la tupla

Meses = ('Enero', 'Febrero', 'Marzo','Abril', 'Mayo', 'Junio', 'Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')

Mes = int(input('Ingresa el Número de un mes: '))

print(Meses[Mes-1])

#%%Ejercicio 2

# Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al
#  usuario un número, el que haya ingresado, es la letra que debe imprimir el 
#  programa

ABC = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

Letra = int(input('Ingrese el Número correspondiente a una Letra en orden alfábetico: '))

print(ABC[Letra-1])