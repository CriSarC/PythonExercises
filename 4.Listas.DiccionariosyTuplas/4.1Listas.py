# -*- coding: utf-8 -*-

Lista1 = ["tomate","cebolla", "huebos", "leche", 'arroz']
Lista2 = [1,2,3,4,5]
Lista3 = [6,7,8,9,10]

print(Lista1)
print(Lista2)
print(Lista3)

print(Lista1[1])
print(Lista2[4])#plotea el elemento que esta en espacio cuatro
print(Lista3[0])

print('leche' in Lista1) #para verificar si un elemento esta en una lista

print(Lista2[0:4]) #Para recorrer la lista

print(Lista1 + Lista2) #para unir dos listas

Lista1[0] = 'Ajo' # modifica un elemento de la lista
print(Lista1)