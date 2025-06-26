#10
productos = [
    ["Laptop", 1200, "Electrónica"],
    ["Camiseta", 25, "Ropa"],
    ["Smartphone", 950, "Electrónica"],
    ["Zapatos", 80, "Ropa"],
    ["Auriculares", 150, "Electrónica"],
    ["Libro", 15, "Librería"],
    ["Tablet", 600, "Electrónica"]
]
filtro=list(filter(lambda x:x[2] == "Electrónica",productos))
segundo_filtro=list(filter(lambda x:x[1]>500,filtro))
descuento=list(map(lambda x:[x[0],round(x[1]*.75,2),x[2]],segundo_filtro))
print(descuento)