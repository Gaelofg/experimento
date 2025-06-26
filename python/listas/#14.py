#14
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

filtro=list(filter(lambda x:x[1]<1000,productos))
descuentos=list(map(lambda x:[x[0],round(x[1]*(.80 if x[2] ==  "Electrónica" else .70 
    if x[2] == "Ropa" else .90 if x[2] == "Librería" else 1),3),x[2]],filtro))
diccionario={}
for i in descuentos:
    objeto,precio,clase=i
    if clase not in diccionario:
        diccionario[clase]=[]
    diccionario[clase].append([objeto,precio])    
print(diccionario)
for clase in diccionario:
    diccionario[clase].sort(key=lambda x:x[1])
for cl in diccionario:
    print(f"\ncateforia :{cl}")
    for j in diccionario[cl]:
        print(f"el objeto :{j[0]} , cuesta {j[1]}")