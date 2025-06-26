#paso 5
tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 9, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]
def matriz(tablero):
    for fila in range(0,9,3):
        for columna in range(0,9,3):
            numeros_repetidos=[]
            for i in range(fila,fila+3):
                for j in range(columna,columna+3):
                    if tablero[i][j] != 0:
                        numeros_repetidos.append(tablero[i][j])
            if len(numeros_repetidos) == len(set(numeros_repetidos)):
                print("valido")
            else:
                print("invalido")            
matriz(tablero)