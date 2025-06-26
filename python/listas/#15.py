#15
productos = [
    ["Laptop", 1200, "Electrónica"],
    ["Camiseta", 25, "Ropa"],
    ["Smartphone", 950, "Electrónica"],
    ["Zapatos", 80, "Ropa"],
    ["Auriculares", 150, "Electrónica"],
    ["Libro", 15, "Librería"],
    ["Tablet", 600, "Electrónica"],
    ["Chaqueta", 130, "Ropa"],
    ["Cuaderno", 10, "Librería"],
    ["Agenda", 20, "Librería"]
]
descuento=list(map(lambda x:[x[0],round(x[1]*(.75 if x[2] == "Electrónica" else 
    .60 if x[2]=="Ropa" else .90 if x[2] == "Librería" else 1),3),x[2]],productos))
filtro=list(filter(lambda x:x[1]>50,descuento))
diccionario={}
for  i in filtro:
    objeto,precio,clase=i
    if clase not in diccionario:
        diccionario[clase]=[]
    diccionario[clase].append([objeto,precio])
for j in diccionario:
    print(f"\ncategoria :{j}")
    for cls in diccionario[j] :
     print(f"el objeto{cls[0]} cuesta ${cls[1]}")       