#3
def organizar(lista,letra):
   lista_nueva=[]
   for i in lista:
      if i.lower().startswith(letra.lower()):
        lista_nueva.append(i)
   lista_nueva.sort()      
   return lista_nueva
nombres = ["Ana", "Bea", "Carlos", "Alejandro", "Alma","Gael"]
abc=organizar(nombres,"a")
print(abc)
ax=organizar(nombres,"g")
print(ax)