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

    G.add_node("A2",DATA ="Mancha color crema sobre la radicula",SEC=0)
    G.add_node("B2",DATA ="Moho color verde azul sobre lesiones",SEC=0)
    G.add_node("C2",DATA ="Foliolos enroscados hacia arriba",SEC=0)
    G.add_node("D2",DATA ="Coloracion verde palido - amarillento",SEC=0)
    G.add_node("E2",DATA ="Perdida de brillo en hojas inferiores",SEC=0)
    G.add_node("F2",DATA ="Secamiento de color marron en las puntas de las hojas",SEC=0)
    G.add_node("G2",DATA ="Manchas color anaranjado en los foliolos",SEC=0)
    G.add_node("H2",DATA ="Necrosis de los tejidos",SEC=0)
    G.add_node("I2",DATA ="Hoja pequeña",SEC=0)
    G.add_node("J2",DATA ="Hoja de gancho",SEC=0)
    G.add_node("K2",DATA ="Foliolos quebradizos",SEC=0)
    G.add_node("P2",DATA ="pudricion de los racimos",SEC=0)
    G.add_node("N2",DATA ="Presencia de protozoarios flagelados en raices",SEC=0)

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
        "A1":(0,0),
        "B1":(0,6),
        "C1":(0,12),
        "A2":(1,0),
        "B2":(1,1),
        "C2":(1,2),
        "D2":(1,3),
        "E2":(1,4),
        "F2":(1,5),
        "G2":(1,6),
        "H2":(1,7),
        "I2":(1,8),
        "J2":(1,9),
        "K2":(1,10),
        "P2":(1,11),
        "N2":(1,12),
        "A3":(2,0),
        "B3":(2,2.5),
        "C3":(2,5),
        "D3":(2,7.5),
        "E3":(2,10),
        "F3":(2,12),
        "A4":(3,0),
        "B4":(3,2.5),
        "C4":(3,5),
        "D4":(3,7.5),
        "E4":(3,10),
        "F4":(3,12)
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
    tkinter.Label(ventana,text="Identifique la edad de la palma:").place(x=40,y=70)
    tkinter.Label(ventana,text="¿Cuáles son los sintomas de la palma?:").place(x=220,y=70)
    ttk.Button(ventana, text="Semilla",command=lambda: rellenar(data,"semillas de palma")).place(x=40,y=100)
    ttk.Button(ventana, text="Palmas Jovenes",command=lambda: rellenar(data,"palma joven")).place(x=40,y=130)
    ttk.Button(ventana, text="Palmas Adultas",command=lambda: rellenar(data,"palmas Adultas")).place(x=40,y=160)
    ttk.Button(ventana, text="Mancha color crema sobre la radicula",command=lambda: rellenar(data,"Mancha color crema sobre la radicula")).place(x=220,y=100)
    ttk.Button(ventana, text="Moho color verde azul sobre lesiones",command=lambda: rellenar(data,"Moho color verde azul sobre lesiones")).place(x=220,y=130)
    ttk.Button(ventana, text="Foliolos enroscados hacia arriba",command=lambda: rellenar(data,"Foliolos enroscados hacia arriba")).place(x=220,y=160)
    ttk.Button(ventana, text="Coloracion verde palido - amarillento",command=lambda: rellenar(data,"Coloracion verde palido - amarillento")).place(x=220,y=190)
    ttk.Button(ventana, text="Perdida de brillo en hojas inferiores",command=lambda: rellenar(data,"Perdida de brillo en hojas inferiores")).place(x=220,y=220)
    ttk.Button(ventana, text="Secamiento de color marron en las puntas de las hojas",command=lambda: rellenar(data,"Secamiento de color marron en las puntas de las hojas")).place(x=220,y=250)
    ttk.Button(ventana, text="Manchas color anaranjado en los foliolos",command=lambda: rellenar(data,"Manchas color anaranjado en los foliolos")).place(x=220,y=280)
    ttk.Button(ventana, text="Necrosis de los tejidos",command=lambda: rellenar(data,"Necrosis de los tejidos")).place(x=220,y=310)
    ttk.Button(ventana, text="Hoja pequeña",command=lambda: rellenar(data,"Hoja pequeña")).place(x=220,y=340)
    ttk.Button(ventana, text="Hoja de gancho",command=lambda: rellenar(data,"Hoja de gancho")).place(x=220,y=370)
    ttk.Button(ventana, text="Foliolos quebradizos",command=lambda: rellenar(data,"Foliolos quebradizos")).place(x=220,y=400)
    ttk.Button(ventana, text="pudricion de los racimos",command=lambda: rellenar(data,"Foliolos quebradizos")).place(x=220,y=430)
    ttk.Button(ventana, text="Presencia de protozoarios flagelados en raices",command=lambda: rellenar(data,"Foliolos quebradizos")).place(x=220,y=220)
    tkinter.Button(ventana,text="Buscar",command=lambda: info(data)).place(x=40,y=350)
    ventana.mainloop()
   
ventana()

