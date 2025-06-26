#20
productos = [
    ["Curso de Python", 100, "Educación", 4.8],
    ["Antivirus Pro", 60, "Software", 4.2],
    ["Plantillas Excel", 30, "Utilidad", 3.9],
    ["Curso de Data Science", 120, "Educación", 4.9],
    ["Editor de Video", 80, "Software", 4.5],
    ["Manual de Finanzas", 50, "Educación", 4.1],
    ["Compresor de Archivos", 40, "Utilidad", 4.0],
    ["Curso de Excel", 90, "Educación", 4.7]
]
#Aplica descuento:
#Educación: 15%
#Software: 10%
#Utilidad: 5%
#Filtra productos cuyo precio con descuento sea menor a 100 y tengan calificación mayor a 4.0.
#Agrúpalos por categoría.
#Ordena cada grupo primero por:
#Calificación descendente
#Luego por precio ascendente
def descuento(productos):
    cursos,precio,modelo,calificacion=productos
    if modelo =="Educación":
        nuevo_precio=precio*.85
    elif modelo =="Software":
        nuevo_precio=precio*.90
    elif modelo == "Utilidad":
        nuevo_precio = precio*0.95
    else:
        nuevo_precio=precio
    return [cursos,nuevo_precio,modelo,calificacion] 
descue=list(map(descuento,productos))               
primer_filtro=list(filter(lambda x: x[1]<100 and x[3]>4.0,descue))
categoria={
}
for i in primer_filtro:
    cursos,precio,modelo,calificacion=i
    if modelo not in categoria:
        categoria[modelo]=[]
    categoria[modelo].append([cursos,precio,calificacion])
for j in categoria:
    print(f"\ncategoria : {j}")
    categoria[j].sort(key=lambda x:x[2],reverse=True)
    categoria[j].sort(key=lambda x:x[1])
    for x in categoria[j]:
        print(f" el curso de {x[0] ,}cuesta {x[1]} y tiene una calificacion de {x[2]}")
    