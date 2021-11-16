lista_cursos = ["Python", "Django", "Flask","Ruby", "Java", "Rust"] 
lista_curso_2=["C", "C++", "Docker"]

print(len(lista_cursos))

lista_cursos.append("MongoDB")
lista_cursos.append("C#")
lista_cursos.append("JavaScript")

lista_cursos.insert(1,"Rails")
lista_cursos.insert(0,"PyGam")

#Sirve para unir dos listas en una sola con la funcion .extend
lista_cursos.extend(lista_curso_2)

#Son formas de elminar elementos por dos metodos
lista_cursos.remove("MongoDB")
del lista_cursos[-1]

#borra todos los elementos de la lista
lista_cursos.clear()

print(len(lista_cursos))

print(lista_cursos)


