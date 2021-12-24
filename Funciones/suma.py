"""def suma():
    numero_uno = int(input("Ingresa el primer numero entero: "))
    numero_dos = int(input("Ingresa el segundo numero entero: "))
    
    resultado = numero_dos + numero_uno
    print("La suma es:" , (resultado))
    
suma() 
"""

def suma (n1,n2):
    return n1, n2, "La funcion retorna dos valores"

numero_uno = int(input("Ingresa el primero numero entero: "))
numero_dos = int(input("Ingresa el segundon numero entero:  "))

resultado = suma(numero_dos,numero_uno)
print(resultado)

