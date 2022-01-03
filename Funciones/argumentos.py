def promedio (*listado): #Toma todos los argumentos y crea una Tupla 
    print(listado)
    print(type(listado))
    return sum(listado) / len(listado)

resultado = promedio (10,10,5,7,10)
print(resultado)



