#%%Ejercicio 1

# En la siguiente lista, debes hacer un programa que muestre los valores al usuario, 
# a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos 
# en el primer y segundo lugar:

# [20, 50, "Curso", 'Python', 3.14]

ListaCambio = [20, 50, 'Curso','Python', 3.14]

print(ListaCambio)

Dato1 = input('Ingresa un Dato: ')
Dato2 = input('Ingresa otro Dato: ')

ListaUno = [Dato1,Dato2]

del ListaCambio[0]

del ListaCambio[0]

ListaUno.extend(ListaCambio)
print(ListaUno)

#%%Ejercicio1111

ListaCambio = [20, 50, 'Curso','Python', 3.14]

print(ListaCambio)

Dato1 = input('Ingresa un Dato: ')
Dato2 = input('Ingresa otro Dato: ')

ListaCambio[0] = Dato1
ListaCambio[1] = Dato2 

print(ListaCambio)




#%%Ejercicio 2

# Escribe una lista que tenga los números de 1 al 10. Luego, debes hacer que los
# datos que están en las posiciones 4, 7 y 9 sean multiplicados por 2; por último,
# mostrar la lista nueva con los nuevos datos

ListaNum = [1,2,3,4,5,6,7,8,9,10]

Posi4 = ListaNum[4] * 2
Posi7 = ListaNum[7] * 2
Posi9 = ListaNum[9] * 2

NuevaLista = [1,2,3,4,Posi4,6,7,Posi7,9,Posi9]
print(NuevaLista)