#1
#Pida al usuario que ingrese nombres de invitados uno por uno.
#Termine cuando el usuario escriba salir.
#Guarde todos los nombres en una lista.
#Al final, muestre:
#Cuántos nombres hay.
#Cuáles empiezan con la letra a (sin importar mayúsculas).
#Todos los nombres en orden alfabético.
lista=[]
lista_de_a=[]
lista_de_normales=[]
while True:
  nombre=input("ingresa los nombres , cuando quieras parar escribes 'salir' :")
  if nombre != "salir":
    lista.append(nombre)
  else:
    break 
for i in lista:
  if i.lower().startswith("a"):
    lista_de_a.append(i)
  else:
   lista_de_normales.append(i)
lista_de_a.sort()
lista_de_normales.sort()   
print(f"los nombres que empiezan por a son :{lista_de_a} y la cantidad de nombres que empezaron con 'a' son {len(lista_de_a)}")
print(f"los nombres normales son {lista_de_normales} y son la cnatidad de {len(lista_de_normales)}")   