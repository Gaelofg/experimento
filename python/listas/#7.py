#lambda #7
"Nombre (Categoría) - $Precio"
productos = [
    ["Laptop", 1200, "Electrónica"],
    ["Camiseta", 25, "Ropa"],
    ["Smartphone", 950, "Electrónica"],
    ["Zapatos", 80, "Ropa"],
    ["Auriculares", 150, "Electrónica"],
    ["Libro", 15, "Librería"]
]
filtro=list(filter(lambda x: x[1]>100,productos))
filtro.sort(key=lambda x:x[1],reverse=True)
resultado = list(map(lambda x: f"{x[0]} ({x[2]}) - ${x[1]}",filtro))
print(resultado)