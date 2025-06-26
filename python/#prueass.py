#prueass
import tkinter as tk
from tkinter import messagebox

def crear_tablero(root, tablero):
    entradas = []
    for i in range(9):
        fila_entradas = []
        for j in range(9):
            e = tk.Entry(root, width=2, font=('Arial', 24), justify='center')
            e.grid(row=i, column=j, padx=1, pady=1)
            if tablero[i][j] != 0:
                e.insert(0, str(tablero[i][j]))
                e.config(state='disabled')  # bloquear celdas iniciales
            fila_entradas.append(e)
        entradas.append(fila_entradas)
    return entradas

def leer_tablero(entradas):
    tablero = []
    for i in range(9):
        fila = []
        for j in range(9):
            val = entradas[i][j].get()
            if val == '':
                fila.append(0)
            else:
                try:
                    n = int(val)
                    if n >= 1 and n <= 9:
                        fila.append(n)
                    else:
                        return None  # valor fuera de rango
                except:
                    return None  # valor no numérico
        tablero.append(fila)
    return tablero

def es_valido(tablero, fila, col, num):
    # verificar fila
    for i in range(9):
        if tablero[fila][i] == num:
            return False
    # verificar columna
    for i in range(9):
        if tablero[i][col] == num:
            return False
    # verificar subcuadro 3x3
    start_fila = (fila // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if tablero[start_fila + i][start_col + j] == num:
                return False
    return True

def resolver_sudoku(tablero):
    for fila in range(9):
        for col in range(9):
            if tablero[fila][col] == 0:
                for num in range(1, 10):
                    if es_valido(tablero, fila, col, num):
                        tablero[fila][col] = num
                        if resolver_sudoku(tablero):
                            return True
                        tablero[fila][col] = 0
                return False
    return True

def mostrar_solucion(entradas, tablero):
    for i in range(9):
        for j in range(9):
            entradas[i][j].config(state='normal')
            entradas[i][j].delete(0, tk.END)
            if tablero[i][j] != 0:
                entradas[i][j].insert(0, str(tablero[i][j]))
                # Opcional: bloquear las celdas originales o todas al final
                entradas[i][j].config(state='disabled')
            else:
                entradas[i][j].config(state='normal')

def boton_resolver():
    tablero_usuario = leer_tablero(entradas)
    if tablero_usuario is None:
        messagebox.showerror("Error", "Por favor, ingresa solo números del 1 al 9 o deja vacío.")
        return
    tablero_copia = [fila[:] for fila in tablero_usuario]  # copiar tablero para no modificar original
    if resolver_sudoku(tablero_copia):
        mostrar_solucion(entradas, tablero_copia)
    else:
        messagebox.showinfo("Sin solución", "No se encontró solución para este Sudoku.")

# --- Programa principal ---

tablero_inicial = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

root = tk.Tk()
root.title("Sudoku Interactivo")

entradas = crear_tablero(root, tablero_inicial)

boton = tk.Button(root, text="Resolver Sudoku", command=boton_resolver)
boton.grid(row=9, column=0, columnspan=9, sticky="we", pady=10)

root.mainloop()
