# 11
productos = [
    ["Laptop", 1200, "Electrónica"],
    ["Camiseta", 25, "Ropa"],
    ["Smartphone", 950, "Electrónica"],
    ["Zapatos", 80, "Ropa"],
    ["Auriculares", 150, "Electrónica"],
    ["Libro", 15, "Librería"],
    ["Tablet", 600, "Electrónica"]
]
filtro=list(filter(lambda x:x[1]<1000,productos))
descuento_electronica=list(map(lambda x:[x[0],round(x[1]*(.85 if x[2]=="Electrónica" else .95),2),x[2]],filtro))
print(descuento_electronica)