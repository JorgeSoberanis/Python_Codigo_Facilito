lista_cursos = ["Python", "Django", "Flask","Ruby", "Java", "Rust"] 
#                  0           1       2       3       4       5
#Para generar una sublistas se coloca [start:end] el final no se toma en cuenta
#[Start:] Se obtienen los ultimos elementos de la lista
#[:end] Se obtiene los primeras elementos de la lista
#[start:end:skip]

sub_lista= lista_cursos[::-1]
print(sub_lista)