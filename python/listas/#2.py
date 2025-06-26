#2
nombres = ["Ana", "Bea", "Carlos", "Alejandro", "Alma"] 
lista=[]
for i in nombres:
    if i.lower().startswith("a"):
        lista.append(i)
lista.sort()
print(lista)        