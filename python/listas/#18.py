#18
alimentos = [
    ["Quinoa", 120, "Grano", "Orgánico"],
    ["Avena", 80, "Grano", "Regular"],
    ["Almendras", 200, "Fruto seco", "Orgánico"],
    ["Nueces", 150, "Fruto seco", "Regular"],
    ["Lentejas", 60, "Grano", "Orgánico"],
    ["Chía", 140, "Semilla", "Orgánico"],
    ["Semillas de girasol", 90, "Semilla", "Regular"]
]
#Aplica descuentos:
#20% a productos orgánicos
#10% a productos regulares
#Filtra los productos cuyo precio final sea menor a 130.
#Agrúpalos por su tipo (Grano, Fruto seco, Semilla).
#Imprime los productos organizados por tipo y ordenados por precio.
decuentos=list(map(lambda x:[x[0],round(x[1]*(.80 if x[3] == "Orgánico" else .90 if x[3] == "Regular" else 1),2),x[2],x[3]],alimentos))
filtro=list(filter(lambda x :x[1]<130, decuentos))
agrupar={

}
for i in filtro:
    comida,precio,tipo,clase=i
    if tipo not in agrupar:
        agrupar[tipo]=[]
    agrupar[tipo].append([comida,precio])   
for j in agrupar:
    print(f"\n {j} :")
    agrupar[j].sort(key=lambda x:x[1])
    for m in agrupar[j]:
        print(f"{m[0]} , {m[1]} ")