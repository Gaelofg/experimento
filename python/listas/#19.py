#19
libros = [
    ["El Hobbit", 180, "Fantasía"],
    ["1984", 150, "Ciencia ficción"],
    ["Orgullo y Prejuicio", 130, "Romance"],
    ["Dune", 200, "Ciencia ficción"],
    ["Harry Potter", 170, "Fantasía"],
    ["Romeo y Julieta", 90, "Romance"]
]
#Tareas:
#Aplica descuentos:
#Fantasía: 10%
#Ciencia ficción: 20%
#Romance: 30%
#Filtra libros cuyo precio con descuento sea mayor a 100.
#Agrúpalos por género.
#Muestra los libros ordenados de mayor a menor precio en cada género.

def descuentos(libros):
 libro,precio,clase=libros
 if clase == "Fantasía":
  nuevo_precio=round(precio*.90,2)
 elif clase == "Ciencia ficción":
  nuevo_precio=round(precio * .80,2)
 elif clase == "Romance":
  nuevo_precio=round(precio*.70,2)
 else:
  nuevo_precio=precio 
 return [libro,nuevo_precio,clase]
descuen=list(map(descuentos,libros))  
filtro=list(filter(lambda x: x[1] > 100,descuen))
agrupacion={}
for i in filtro:
  libro , precio, genero =i
  if genero not in agrupacion:
   agrupacion[genero]=[]
  agrupacion[genero].append([libro,precio])
for j in agrupacion:
 print(f"\nel genero {j} tiene los siguientes libros :")   
 agrupacion[j].sort(key=lambda x:x[1],reverse=True)
 for x in agrupacion[j]:
  print (f"el libro de {x[0]} cuesta {x[1]}")
