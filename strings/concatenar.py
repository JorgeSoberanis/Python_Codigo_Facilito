nombre = "Jorge Antonio"
apellido = "Soberanis Balam"


#nombre_completo= "Mr." + nombre + " " + apellido

#nombre_completo = "Mr.%s %s %s." %(nombre,apellido,)
#Se emplean los string base con %s y se reemplazan por los valores del 
#la posicion de &(valores)

#nombre_completo = "Mr.{} {}.".format(nombre,apellido)

nombre_completo= f"Mr. {nombre}{apellido}"

print(nombre_completo)

