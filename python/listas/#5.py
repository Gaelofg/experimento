#5
def organizar(lista):
    pares=[]
    impares=[]
    for i in lista:
        if i % 2 ==0:
            pares.append(i)
        else:
            impares.append(i)
    pares.sort()    
    impares.sort()
    return pares, impares,len(pares),len(impares)
lista_de_nuemeros=[12, 7, 5, 22, 19, 8, 3, 16, 45, 28, 30, 9, 4, 13, 2]
par,impar,cantidad_par,cantidad_impar=organizar(lista_de_nuemeros)
print(par)
print(impar)
print(f"la cantidad de numeros pares son {cantidad_par} y la cantidad de impares son {cantidad_impar}")