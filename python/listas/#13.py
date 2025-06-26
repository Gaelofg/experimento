#13
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
filtrar=list(filter(lambda x:x[1]<1000,productos))
descuentos=list(map(lambda x:[x[0],round(x[1] * (.85 if x[2] == "Electrónica" else .75 if x[2]=="Ropa" else .95 if x[2] == "Librería" else 1),3),x[2]],filtrar))
diccionario={
}
for i in descuentos:
    objeto,precio,clase=i
    if clase not in diccionario:
        diccionario[clase]=[]
    diccionario[clase].append([objeto,precio])
print(diccionario)    