#prueba sodoku
tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]
def vereficar_filas(tablero):  
    for i in tablero:
         contador=[]
         for j in i:
             if j!= 0:
                contador.append(j)  
         if len(contador) != len(set(contador)):
             return False
    
    return True                        
def columnas(tablero):
    for i in range(0,9):
        lista=[]
        for x in range(0,9):
            if tablero[x][i] != 0:
                lista.append(tablero[x][i])
        if len(lista)!=len(set(lista)):
         return False  
    return True 
def matriz(tablero):
    for fila in range(0,9,3):
        for columna in range(0,9,3):
            numeros_repetidos=[]
            for i in range(fila,fila+3):
                for j in range(columna,columna+3):
                    if tablero[i][j] != 0:
                        numeros_repetidos.append(tablero[i][j])
            if len(numeros_repetidos) != len(set(numeros_repetidos)):
             return False
    return True      

def verificador(tablero):
    if vereficar_filas(tablero) and columnas(tablero) and matriz(tablero):
        print("Valido")
    else:
        print("Invalido")
verificador(tablero)