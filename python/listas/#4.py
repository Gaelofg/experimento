#4
lista_de_vocales=["a","e","i","o","u"]
def proceso(nombres,vocal):
    consonantes=[]
    vocales=[]
    for i in nombres:
        if i[0].lower() in vocal:
            vocales.append(i)
        else:
            consonantes.append(i)
    consonantes.sort()
    vocales.sort() 
    return consonantes,vocales,len(consonantes),len(vocales)
lista_de_nombres=["Ana", "Eduardo", "Isabel", "Omar", "Ursula",
    "Carlos", "Bea", "Luis", "Ricardo", "Sofia",
    "Alonso", "Esteban", "Iker", "Oscar", "Ulises",
    "Mariana", "Pedro", "Diego", "Fernanda", "Gloria"]           
c,v,num_c,num_v=proceso(lista_de_nombres,lista_de_vocales)
print(c)
print(v)
print(f"y en total tiene {num_c} de palabras que empiezan en consonante y {num_v} de palabras que empiezan en vocal")
