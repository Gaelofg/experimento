#9
empleados = [
    ["Ana", 1800, "Marketing"],
    ["Luis", 2500, "Ventas"],
    ["Carlos", 3200, "IT"],
    ["Elena", 1500, "Marketing"],
    ["Jorge", 2800, "IT"],
    ["Lucía", 2100, "Ventas"]
]
filtro=list(filter(lambda x:x[1]<2500,empleados))
aumento=list(map(lambda x:[x[0],round(x[1] * 1.10,2),x[2]],filtro))
aumento.sort(key=lambda x :x[1],reverse=True)
final=list(map(lambda x:f"{x[0]} - {x[1]} ({x[2]})",aumento))
print(final)