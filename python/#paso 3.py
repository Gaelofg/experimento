#paso 3
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
for x in tablero:
    print(x)
def vereficar_filas(tablero):
   
    for i in tablero:
         contador=[]
         for j in i:
             if j!= 0:
                contador.append(j)  
         if len(contador) != len(set(contador)):
             return "invalido"
    
    return"valido"                        


print(vereficar_filas(tablero))        
