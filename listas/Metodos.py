lista=[2, 1, 500, 800, 75, 9]

#La funcion sort sirve para ordenar de manera automatica asecendente
#Con la funcion reverse=True se pone de mayor a menor.

"""
lista.sort(reverse=True)
print(lista)
"""
"""Se ordenan los elementos de menor a mayor
lista.sort()
print(lista[0])
print(lista[-1])
"""
#El uso de la funciona min y max sirven para lo mismo
"""print(min(lista))
print(max(lista))"""
#Es una forma para comprobar si un elemento esta dentro de una lista, genera valores booleanos
print(9 in lista)

index= lista.index(9)
print(index)