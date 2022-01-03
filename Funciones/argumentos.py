def promedio (*args): #Toma todos los argumentos y crea una Tupla 
    return sum(args) / len(args)

"""resultado = promedio (10,10,5,7,10,50,8)
print(resultado)

def conbinacion(p1,p2,*args, p4=500): #Asigna los argumentos bien pero el resto sirve para generar una tupla a args
    print(p1)
    print(p2)
    print(args)
    print(p4)
conbinacion(10,20,30, 3, 4,5,6,7,8,p4=1000)
"""

def usuarios (**kwargs): #Se conbierte en un diccionario con doble asterisco
    print(kwargs)
    print(type(kwargs))

usuarios (eduardo=[10,10,8], fernando= [10,9,10])




