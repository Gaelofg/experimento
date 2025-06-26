import tkinter as tk
fondo=tk.Tk()
fondo.title("new")
fondo.geometry("1000x700")
entry1=tk.Entry(fondo)
entry2=tk.Entry(fondo)
entry3=tk.Entry(fondo)
entry4=tk.Entry(fondo)
entry5=tk.Entry(fondo)
entry6=tk.Entry(fondo)
entry7=tk.Entry(fondo)
entry8=tk.Entry(fondo)
entry9=tk.Entry(fondo)
inputs=[[entry1,entry2,entry3],
        [entry4,entry5,entry6],
        [entry7,entry8,entry9]]
for i,fila in enumerate(inputs):
    for j,columna in enumerate(fila):
        columna.grid(row=i,column=j,padx=5,pady=5)

def convertilo(inputs):
    new=[]
    for fila in inputs:
        new_mini=[]
        for columna in fila:
            num=columna.get()
            if num.isdigit():  
             entero = int(num)
            else:
             entero = 0 
            new_mini.append(entero)
        new.append(new_mini)    
    return new
def resolucion(matriz):
 numeros=[] 
 for x,fil in enumerate(matriz):
   for y,col in enumerate(fil):
      numeros.append(matriz[x][y])
 if len(numeros) != len(set(numeros)):
       return False
 return True
def mostrar():
 matriz=convertilo(inputs)
 for z in matriz:
      print(z)
 if resolucion(matriz) is True:
     print("este sudoku es valido")
 else:
     print("no es un sudoku valido")    
boton=tk.Button(fondo,text="click",command=mostrar)
boton.grid(row=4, column=0, columnspan=3, pady=10)
print()
print()
  
fondo.mainloop()