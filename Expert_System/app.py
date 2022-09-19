from tkinter import Label, ttk
import networkx as nx
import matplotlib.pyplot as plt
import tkinter 
from tkinter import messagebox

def creacion_grafo(x):
    G = nx.DiGraph()
    # asignar atributos a nodos y aristas
    #Añadir nodos
    G.add_node("A1",DATA ="semillas de palma",SEC=0)
    G.add_node("B1",DATA ="palma joven",SEC=0)
    G.add_node("C1",DATA ="palmas Adultas",SEC=0)

    G.add_node("A3",DATA ="germen marron",SEC=0)
    G.add_node("B3",DATA ="deficiencia de nitrogeno",SEC=0)
    G.add_node("C3",DATA ="deficiencia de magnesio",SEC=0)
    G.add_node("D3",DATA ="deficiencia de potasio",SEC=0)
    G.add_node("E3",DATA ="deficiencia de boro",SEC=0)
    G.add_node("F3",DATA ="marchitez sorpresiva",SEC=0)

    G.add_node("A4",DATA ="Afecta toda la raíz en emergencia causando la muerte de la plántula.",SEC=0)
    G.add_node("B4",DATA ="El tamaño de las hojas se reduce",SEC=0)
    G.add_node("C4",DATA ="Puede  restringir  el  desarrollo  de  las  hojas  y  raíces",SEC=0)
    G.add_node("D4",DATA ="deficiencia de potasio",SEC=0)
    G.add_node("E4",DATA ="deficiencia de boro",SEC=0)
    G.add_node("F4",DATA ="Secamiento de gran parte de la superficie de las  hojas.",SEC=0)


    #Añadir aristas

    G.add_edge("A3","A4")
    G.add_edge("B3","B4")
    G.add_edge("C3","C4")
    G.add_edge("D3","D4")
    G.add_edge("E3","E4")
    G.add_edge("F3","F4")

    #Colores--Identificador
    color_map = []
    for node in G.nodes(data=True):
        dic = node[1]
        for p in x:
            if(dic["DATA"]==p):
                dic["SEC"] = 1

    for node in G.nodes(data=True):
        dic = node[1]
        if(dic["SEC"]==1):
            color_map.append("yellow")
        else:
            color_map.append("green")

   
        
    #Gráficar
    posicion = {
        "A1":(0,2),
        "B1":(0,4),
        "C1":(0,6),
        "A3":(2,0),
        "B3":(2,1),
        "C3":(2,2),
        "D3":(2,3),
        "E3":(2,4),
        "F3":(2,5),
        "A4":(3,1),
        "B4":(3,2),
        "C4":(3,3),
        "D4":(3,4),
        "E4":(3,5),
        "F4":(3,7)
    }

    nx.draw(G,pos=posicion, with_labels=True,node_size=500,node_color=color_map)
    plt.title("Grafo de enfermedad (Palma)")
    plt.show()

def rellenar(x,y):
    mensaje = ""
    if(y not in x):
        x.append(y)
        messagebox.showinfo(message=y+" Se ha agregado", title="Alerta")
    else:
        x.remove(y)
        messagebox.showinfo(message=y+" Se ha eliminado", title="Alerta")
    for i in x:
        mensaje = mensaje + " \n" + i
    messagebox.showinfo(message="Estos son los datos" + mensaje, title="Alerta")

def info(x):  
    creacion_grafo(x)

def ventana():
    data =[]
    ventana = tkinter.Tk()
    ventana.title("Palmas_Interfaz")
    ventana.geometry("640x480")
    tkinter.Label(ventana,text="Palmas SE").place(x=280,y=20)
    tkinter.Label(ventana,text="Identifique la edad de la palma:").place(x=90,y=70)
    tkinter.Label(ventana,text="¿Cuáles son los sintomas de la palma?:").place(x=350,y=70)
    ttk.Button(ventana, text="Semilla",command=lambda: rellenar(data,"semillas de palma")).place(x=90,y=100)
    ttk.Button(ventana, text="Palmas Jovenes",command=lambda: rellenar(data,"palma joven")).place(x=90,y=130)
    ttk.Button(ventana, text="Palmas Adultas",command=lambda: rellenar(data,"palmas Adultas")).place(x=90,y=160)
    ttk.Button(ventana, text="S1",command=lambda: rellenar(data,"s1")).place(x=350,y=100)
    ttk.Button(ventana, text="S2",command=lambda: rellenar(data,"s2")).place(x=350,y=130)
    ttk.Button(ventana, text="S3",command=lambda: rellenar(data,"s3")).place(x=350,y=160)
    ttk.Button(ventana, text="S4",command=lambda: rellenar(data,"s4")).place(x=350,y=190)
    ttk.Button(ventana, text="S5",command=lambda: rellenar(data,"s5")).place(x=350,y=220)
    tkinter.Button(ventana,text="Buscar",command=lambda: info(data)).place(x=280,y=350)
    ventana.mainloop()
   
ventana()

