#12
productos = [
    ["Laptop", 1200, "Electrónica"],
    ["Camiseta", 25, "Ropa"],
    ["Smartphone", 950, "Electrónica"],
    ["Zapatos", 80, "Ropa"],
    ["Auriculares", 150, "Electrónica"],
    ["Libro", 15, "Librería"],
    ["Tablet", 600, "Electrónica"],
    ["Chaqueta", 130, "Ropa"]
]
filtrar=list(filter(lambda x:x[1]>100,productos))
descuento=list(map(lambda x:[x[0], x[1],round(x[1]*(.80 if x[2] == "Ropa" else .90),2), x[2]],filtrar))
print(descuento)