
rango = range(21) #Listado de un rango del 0-20

for valor in rango:
    #print(type(valor))
    print(valor)


Rango = range(0 , 20 , 2)
#stard, end, skips
for c in Rango:
    print(c)


numeros =[10,20,30,40,50]

for indicem, numero in enumerate(numeros):
    print(indicem,numero)