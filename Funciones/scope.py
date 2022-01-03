# Scope
animal = "Leon" #variables global se usan en->Funcion, Condicion o Ciclo

def imprimir_animal():
    animal = "Ballena" #Variable local solo se utiliza dentro del bloque donde fue creada
    
    tipo = "Mamifero"

    print(animal)
    print(id(animal))

imprimir_animal()
print(animal)
print(id(animal))

