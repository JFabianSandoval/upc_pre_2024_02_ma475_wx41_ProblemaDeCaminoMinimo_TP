import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import networkx as nx
import matplotlib.pyplot as plt


def matrizTam():
    tam = random.randint(8, 16) 
    return tam


def matrizAleatoria():
    tam = matrizTam()
    matriz = [[0 for _ in range(tam)] for _ in range(tam)]
    
    for i in range(tam):
        for j in range(i, tam):
            valor = random.randint(0, 1)
            matriz[i][j] = valor
            matriz[j][i] = valor

    return matriz


def matrizPersonalizable():
    tam = matrizTam()  
    matriz = [[0 for _ in range(tam)] for _ in range(tam)]
    
    for i in range(tam):
        for j in range(tam):
            matriz[i][j] = int(input(f"Valor para matriz[{i}][{j}] (0 o 1): "))
    
    return matriz


def mostrarGrafoYCaminoMinimo(matriz):
    G = nx.Graph()

   
    for i in range(len(matriz)):
        G.add_node(i)

  
    for i in range(len(matriz)):
        for j in range(i, len(matriz)):
            if matriz[i][j] == 1:
                G.add_edge(i, j)

  
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='black', node_size=1000, font_size=15)
    plt.show()

   
    vertice1 = simpledialog.askinteger("Seleccionar vértice", "Ingrese el primer vértice:")
    vertice2 = simpledialog.askinteger("Seleccionar vértice", "Ingrese el segundo vértice:")

   
    if nx.has_path(G, vertice1, vertice2):
        camino_minimo = nx.shortest_path(G, vertice1, vertice2)
        resultado_text.insert(tk.END, f"\nCamino mínimo entre {vertice1} y {vertice2}: {camino_minimo}\n")
    else:
        resultado_text.insert(tk.END, f"\nNo existe un camino entre {vertice1} y {vertice2}\n")


def op1():
    matrizSimetrica = matrizAleatoria()
    resultado_text.delete(1.0, tk.END) 
    for fila in matrizSimetrica:
        resultado_text.insert(tk.END, f"{fila}\n")
    mostrarGrafoYCaminoMinimo(matrizSimetrica)

def op2():
    matriz2 = matrizPersonalizable()
    resultado_text.delete(1.0, tk.END)  
    for fila in matriz2:
        resultado_text.insert(tk.END, f"{fila}\n")
    mostrarGrafoYCaminoMinimo(matriz2)

def op3():
    root.quit()


root = tk.Tk()
root.title("Programa de Matrices")
root.geometry("600x600+0+0")

btn_op1 = tk.Button(root, text="Generar Matriz Aleatoria", command=op1)
btn_op1.pack(pady=10)

btn_op2 = tk.Button(root, text="Generar Matriz Personalizada", command=op2)
btn_op2.pack(pady=10)

btn_op3 = tk.Button(root, text="Salir", command=op3)
btn_op3.pack(pady=10)


resultado_text = tk.Text(root, height=20, width=50)
resultado_text.pack(pady=10)


root.mainloop()
