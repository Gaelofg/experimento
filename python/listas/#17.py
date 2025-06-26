#17
gadgets = [
    ["Smartwatch", 200, "Wearable", "2023"],
    ["Drone", 950, "Aéreo", "2022"],
    ["VR Headset", 400, "Entretenimiento", "2023"],
    ["Tablet", 600, "Móvil", "2021"],
    ["Fitness Band", 90, "Wearable", "2023"],
    ["GoPro", 300, "Aéreo", "2022"],
    ["E-Reader", 120, "Móvil", "2021"],
    ["Game Console", 500, "Entretenimiento", "2022"]
]
#Aplica un descuento del:
#15% para gadgets de 2023
#20% para gadgets de 2022
#25% para gadgets de 2021
#Filtra solo los productos con precio final mayor a 100.
#Agrúpalos por su tipo (Wearable, Aéreo, etc.).
#Muestra los resultados ordenados de menor a mayor precio dentro de cada grupo.
def descuentos_2(gadgets):
    objeto,precio,tipo,año=gadgets
    if año == "2023":
        nuevo_precio=round(precio*.85,2)
    elif año == "2022":
        nuevo_precio=round(precio*.80,2)
    elif año =="2021": 
        nuevo_precio=round(precio*.75,2)
    else:
        nuevo_precio=precio 
    return [objeto,nuevo_precio,tipo,año]          
descuentos=list(map(descuentos_2,gadgets))
filtro=list(filter(lambda x:x[1]>100,descuentos))
diccionario={
}
for i in filtro:
    obj,nue,tip,añio=i
    if tip not in diccionario:
        diccionario[tip]=[]
    diccionario[tip].append([obj,nue,añio])
for j in diccionario:
    diccionario[j].sort(key=lambda  x:x[1] )

for tipo in diccionario:
    print(f"\n {tipo}")
    for x in diccionario[tipo] :
        print(f"{x[0]} , cuesta {x[1]} y es de {x[2]}")
