import tkinter as tk
fondo=tk.Tk()
fondo.title("hello")
fondo.geometry("700x500")
texto=tk.Label(fondo,text="ingresa tu nombre ",fg="red")
texto.pack()
saludo=tk.Label(fondo,text="",fg="blue")
ingresar_nombre=tk.Entry(fondo)
ingresar_nombre.pack()
def saludar():
    name=ingresar_nombre.get()
    if name.strip():
        saludo.config(text=f"hello {name} welcome!!",fg="green")
        saludo.pack()
    else:
        saludo.config(text="please enter your name",fg="red",font=("arial",15))
        saludo.pack()
boton=tk.Button(fondo,text="enviar",command=saludar)
boton.pack()
fondo.mainloop()