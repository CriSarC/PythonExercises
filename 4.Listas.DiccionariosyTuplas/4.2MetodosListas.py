# -*- coding: utf-8 -*-

Lista1 = ["tomate","cebolla", "huebos", "leche", 'arroz']
Lista2 = [1,2,3,4,5]
Lista3 = [6,7,8,9,10]
Lista4 = ['s',"f",'a','b','e','c']

Lista1.append(50) #agrega un elemento a una lista
print(Lista1)

del Lista1[3] #elimina elementos de una lista de pendiendo de su posicion
print(Lista1)

Lista2.extend(Lista3) #concatena o une dos listas
print(Lista2)

Lista1.remove('cebolla') #remueve un elemento sabiendo cual elemento es
print(Lista1)

Lista4.sort() #ordena alfabeticamente los elementos de una lista
print(Lista4)