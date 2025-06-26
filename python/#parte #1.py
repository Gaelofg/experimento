#parte #1
matrix=[[1,2,0],[2,3,0],[4,5,6]]
for i in matrix:
    print(i)
def esta(matriz,numero):
    for indice_fila,i in enumerate(matriz):
        for indice_columna,j in enumerate(i):
            if j == numero:
                return (indice_fila,indice_columna)

    return "no esta"    
            
print(esta(matrix,5))            