#sooku parte  1
lista=[]    
for i in range(1,10):
 nueva_lista=[]
 for j in range(1,10):
     nueva_lista.append(0) 
 lista.append(nueva_lista)  
lista[4][3]=7 
for x in lista:
   print(x)     
for i in lista :
   print(lista[3][3])
def reglas(lista,fila,numero):
  
  if numero in lista[fila]:
     return True
  else:
     return False
print(f"el numero esta en la fila?")
resultado=reglas(lista,4,7)
print(resultado)

def columnas(lista,columna,numero):
    for i in range(0,9):  
      if lista[i][columna] == numero:
         return True
    return False      
           
col=columnas(lista,3,7)  
print(col)