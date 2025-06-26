import tkinter as tk
fondo=tk.Tk()
fondo.title("hello app")
fondo.geometry("500x300")
mensaje=tk.Label(fondo,text="hello",fg="blue")
mensaje.pack()
def cambiar():
    mensaje.config(text="nice to meet you",fg="red",font=("Arial",38))
    boton.config(state="disabled")
boton=tk.Button(fondo,text="click here",command=cambiar)    
boton.pack()
fondo.mainloop()