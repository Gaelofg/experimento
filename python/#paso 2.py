#paso 2
matriz=[[2,1,3],[1,2,3],[2,3,1]]
for i in matriz:
    print(i)
def encontrar(matriz,numero):
        contador=[]
        for ind_l,i in enumerate(matriz):
              for ind_c,j in enumerate(i):
                    if j == numero:
                          contador.append([ind_l,ind_c])
        return contador
print(encontrar(matriz,2))                                         