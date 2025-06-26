# paso final
tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
def espacios_vacios(tablero):
  for i in range(9):
     for j in range(9):
         if tablero[i][j] == 0: 
          return (i,j)
  return None 
def validar3x3(tablero,numero,pos):
 fila,columna=pos
 #vereficar fila 
 for y in range(9):
  if tablero[fila][y] == numero and y != columna:
   return False
   #vereficar columnas
 for x in range(9):
  if tablero[x][columna] == numero and x != fila:
   return False
 #vereficar el 3x3
  index_fila=(fila//3)*3
  index_columna=(columna//3)*3
 for i in range(index_fila,index_fila+3):
  for j in range(index_columna,index_columna+3):
   if tablero[i][j] == numero and (i,j)!= pos:
    return False
 return True  
def resolver_sodoku(tablero):
   vacios=espacios_vacios(tablero)
   if not vacios:
      return True
   fila,columna=vacios
   for i in range(1,10):
      if validar3x3(tablero,i,vacios):
        tablero[fila][columna]=i
        if resolver_sodoku(tablero):
          return True
        else:
         tablero[fila][columna]=0 
   return False
if resolver_sodoku(tablero):
  for i in tablero:
    print(i)     