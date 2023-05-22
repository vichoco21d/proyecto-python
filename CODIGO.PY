# lista= [15, "nombre", 3.1415,True]
# print (lista[0])
#usuario=["usernametest1","pass123","correo@correo" ]
#print (usuario[1])
# se empieza a contar del 0, username seria=(0), pass123= el (1), correo@correo= seria el (2).
# numeros=[10, 50, 100, 255, 500]
# numeros.append (1000)
# print (numeros)
#el append agregas un valor a la lista, como se agrego el 1.000
numeros=[10, 50, 100, 255, 500]
numeros.append (1000)
print (numeros)
#extend, permite añadir valores a la lista inicial. 
extra=[75,350, 990]
numeros.extend(extra)
print (numeros)
#insert, permite añadir un elemento en una posición determinado
numeros.insert(6,5000)
print(numeros)
#remove,  permite recibir como argumento un objeto y lo borra de la lista.
numeros.remove(50)
print(numeros)
#pop, elimina el ultimo registro, elimina la posicion del numero
numeros.pop(3)
print(numeros)
#reverse, permite invertir el orden dela lista.
numeros.reverse()
print(numeros)
#sort, ), permite ordenar los elementos de menor a mayor
#tambien permite ordenar los elementos de mayor a menor, agregandole un: 
# lista=[1,2,3]
#lista.sort(reverse=true) 
#print(lista)
numeros.sort()
print(numeros)









