#16
productos = [
    ["Bufanda", 40, "Ropa", "Invierno"],
    ["Sandalias", 35, "Ropa", "Verano"],
    ["Refrigerador", 800, "Electrodomésticos", "Todo el año"],
    ["Guantes", 25, "Ropa", "Invierno"],
    ["Ventilador", 150, "Electrodomésticos", "Verano"],
    ["Libro de cocina", 50, "Librería", "Todo el año"],
    ["Paraguas", 20, "Accesorios", "Invierno"],
    ["Gafas de sol", 60, "Accesorios", "Verano"],
    ["Calefactor", 300, "Electrodomésticos", "Invierno"],
    ["Shorts", 45, "Ropa", "Verano"]
]
#Aplica los siguientes descuentos:
#Invierno: 30% de descuento
#Verano: 25% de descuento
#Todo el año: 10% de descuento
descuentos=list(map(lambda x:[x[0],round(x[1]*(.70 if x[3]=="Invierno" else .75 
    if x[3]=="Verano" else .90 ),3),x[2],x[3]],productos))
filtro=list(filter(lambda x:x[1]>40,descuentos))
diccionario={}
for i in filtro:
    prenda,precio,clase,epoca=i
    if clase not in diccionario:
        diccionario[clase]=[]
    diccionario[clase].append([prenda,precio])

for j in diccionario:
    print(f"\ncategoria :{j}")   
    for z in diccionario[j]:
        print(f"la prenda {z[0]} y cuesta {z[1]}")    