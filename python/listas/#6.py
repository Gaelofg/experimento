#6
estudiantes = [
    ["Ana", 85],
    ["Luis", 42],
    ["Carlos", 73],
    ["Elena", 90],
    ["María", 58],
    ["Jorge", 33],
    ["Lucía", 100],
]
def calificador(lista):
    aprobaron=[]
    reprobaron=[]
    for i in lista:
        nombre=i[0]
        nota=i[1]
        if nota > 60:
            aprobaron.append([nombre,nota])
        else:
            reprobaron.append([nombre,nota])
    aprobaron.sort(key=lambda x:x[1],reverse=True)
    reprobaron.sort(key=lambda x:x[1],reverse=True)
    return aprobaron,reprobaron            
aprobaron,reprobaron=calificador(estudiantes)
print("los estudiantes que aprovaron fueron :",aprobaron)
print("los que reprobaron fueron :",reprobaron)