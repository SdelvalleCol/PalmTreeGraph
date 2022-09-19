#Hecho--SANTIAGO DELVALLE

from tkinter import Label, ttk
import networkx as nx
import matplotlib.pyplot as plt
import tkinter 
from tkinter import messagebox

def creacion_grafo(x):
    G = nx.DiGraph()
    # asignar atributos a nodos y aristas
    #Añadir nodos

    #Plantas
    G.add_node("A1",DATA ="semillas de palma",SEC=0,REC = "")
    G.add_node("B1",DATA ="palma joven",SEC=0,REC = "")
    G.add_node("C1",DATA ="palmas Adultas",SEC=0,REC = "")

    #Sintomas
    G.add_node("A2",DATA ="Mancha color crema sobre la radicula",SEC=0,REC = "")
    G.add_node("B2",DATA ="Moho color verde azul sobre lesiones",SEC=0,REC = "")
    G.add_node("C2",DATA ="Foliolos enroscados hacia arriba",SEC=0,REC = "")
    G.add_node("D2",DATA ="Coloracion verde palido - amarillento",SEC=0,REC = "")
    G.add_node("E2",DATA ="Perdida de brillo en hojas inferiores",SEC=0,REC = "")
    G.add_node("F2",DATA ="Secamiento de color marron en las puntas de las hojas",SEC=0,REC = "")
    G.add_node("G2",DATA ="Manchas color anaranjado en los foliolos",SEC=0,REC = "")
    G.add_node("H2",DATA ="Necrosis de los tejidos",SEC=0,REC = "")
    G.add_node("I2",DATA ="Hoja pequeña",SEC=0,REC = "")
    G.add_node("J2",DATA ="Hoja de gancho",SEC=0,REC = "")
    G.add_node("K2",DATA ="Foliolos quebradizos",SEC=0,REC = "")
    G.add_node("P2",DATA ="pudricion de los racimos",SEC=0,REC = "")
    G.add_node("N2",DATA ="Presencia de protozoarios flagelados en raices",SEC=0,REC = "")

    #Enfermedades
    G.add_node("A3",DATA ="germen marron",SEC=0,REC = ["Mancha color crema sobre la radicula","Moho color verde azul sobre lesiones"] , cons ="Afecta toda   la   raíz en emergencia causando la muerte de la plántula" ,trat ="El germen marrón se previene manteniendo el contenido de humedad de la semilla por debajo del 19%" )
    G.add_node("B3",DATA ="deficiencia de nitrogeno",SEC=0,REC = ["Foliolos enroscados hacia arriba","Coloracion verde palido - amarillento"], cons ="El tamaño de las hojas se reduce" ,trat ="Vigilar la fertilidad del suelo que  se  usa  en   las  bolsas  de  vivero  y/o  fallas  en  el  programa   de  fertilización")
    G.add_node("C3",DATA ="deficiencia de magnesio",SEC=0,REC = ["Perdida de brillo en hojas inferiores","Secamiento de color marron en las puntas de las hojas"], cons ="Puede  restringir  el  desarrollo  de  las  hojas  y  raíces" ,trat ="Vigilar la fertilidad del suelo que se  usa  en   las  bolsas  de  vivero  y/o  fallas  en  el  programa   de  fertilización. Utilizar fertilizante de sulfato de magnesio")
    G.add_node("D3",DATA ="deficiencia de potasio",SEC=0,REC = ["Manchas color anaranjado en los foliolos","Necrosis de los tejidos"], cons ="La  palma  africana  requiere  de  buenas  cantidades  de  potasio  y  este  elemento  es  removido  en  los  racimos  cosechados.  Los  síntomas  de  su  deficiencia  se  pre-sentan  en  cualquier  edad,  pero  son  más acentuados en suelos  pobres  y  en   material  con  alto  potencial  de  rendimiento,  si  éste  no  recibe  una  adecuada  fertilización." ,trat ="Utilizar fertilizante de cloruro de potasio sin ser excesivo, ya que esto puede inducir en una deficiencia de magnesio y boro")
    G.add_node("E3",DATA ="deficiencia de boro",SEC=0,REC = ["Hoja pequeña","Hoja de gancho","Foliolos quebradizos"], cons ="Se  manifiesta  por  una  gran  variedad  de  síntomas,  particularmente   por  malformaciones  y  disminución  del   tamaño  de   las  hojas.   La  denominada  hoja  de  gancho   se   manifiesta  por  un  acortamiento  de   los   folíolos,  que  permanecen  anormalmente  compacta-dos  en  el  raquis  y  rígidos.  En  el extremo de ellos se forma   un   gancho   característico,   rígido,  debido  a  la  distorsión  de  la  nervadura  central.   La  superficie  de   la   lámina   en    la   porción   del   gancho   aparece   corrugada   y   más   angosta   y   los   tejidos   se   hacen   quebradizos.   A   veces   la  parte  terminal  del  gancho  se dobla  en  forma de zigzag." ,trat ="En palmas adultas, se puede corregir aplicando Borax (tetraborato de sodio) en las axilas de las hojas, arriba de la zona donde se desarrollan los racimos. La aplicacion es anual y la dosis varia entre 60 y 70grs dependiendo de la magnitud de los sintomas")
    G.add_node("F3",DATA ="marchitez sorpresiva",SEC=0,REC = ["pudricion de los racimos","Presencia de protozoarios flagelados en raices"], cons ="La Marchitez sorpresiva de la palma de aceite ha sido asociada a la presencia de un protozoario flagelado del género Phytomonas (Trypanosomatidae), identifi-cado como P. staheli por McGhee y McGuee en 1980 (McCoy, 1981; McCoy y Martínez, 1982). El papel de estos microorganismos como patógenos de plantas no es nuevo, ellos fueron reconocidos en plantas de café  desde  1931,  y  fueron  transmitidos  por  injerto, pero no se identificó ningún vector y por muchos años no se les prestó mayor atención como patógenos de plantas.Los flagelados aislados de palmas son alargados, con un tamaño aproximado de 15-20 x 0,5-1,0 micras. Su estructura general es la típica del género Phytomonas. Ellos  no  se  encuentran  distribuidos  uniformemente en la palma, pudiéndose encontrar en algunos de los haces  vasculares  mientras  están  ausentes  en  otros (McCoy, 1981).Los primeros síntomas de la enfermedad incluyen la pérdida del brillo de los frutos, seguidos de la pudrición de los racimos y la detención del desarrollo de nuevas inflorescencias. Estos son seguidos por una decolo-ración café de los folíolos y su deshidratación severa, que se inicia en las hojas más bajas, comenzando en el ápice de los folíolos del ápice de la hoja y progre-sando rápidamente de abajo hacia arriba, hasta afectar a todas las hojas (Figura 5). Estos síntomas solo se comienzan a presentar en el campo en la medida en que las palmas alcanzan su estado de madurez" ,trat ="No hay evidencias de recuperación de una palma después de presentar los síntomas de la enfermedad, la Marchitez sorpresiva es letal. Esta enfermedad es más prevalente en plantaciones donde no se realizan buenas prácticas de manejo, especialmente no se realiza el control de las gramíneas. La enfermedad se ha controlado cuando se realizan campañas de identificación temprana de las palmas enfermas y se procede a su rápida erradicación, complementada con el manejo adecuado de las gramíneas presentes en los lotes afectados y la aplicación de insecticidas en el área, para reducir la población de los insectos que pueden estar involucrados en su diseminación")

    #Añadir aristas

    #Marrón
    G.add_edge("A1","A2")
    G.add_edge("A1","B2")
    G.add_edge("A2","A3")
    G.add_edge("B2","A3")

    #Nitrogeno
    G.add_edge("B1","C2")
    G.add_edge("B1","D2")
    G.add_edge("C2","B3")
    G.add_edge("D2","B3")

    #Magnesio
    G.add_edge("B1","E2")
    G.add_edge("B1","F2")
    G.add_edge("C1","E2")
    G.add_edge("C1","F2")
    G.add_edge("E2","C3")
    G.add_edge("F2","C3")

    #Potasio
    G.add_edge("B1","G2")
    G.add_edge("B1","H2")
    G.add_edge("C1","G2")
    G.add_edge("C1","H2")
    G.add_edge("G2","D3")
    G.add_edge("H2","D3")

    #Boro
    G.add_edge("C1","I2")
    G.add_edge("C1","J2")
    G.add_edge("C1","K2")
    G.add_edge("I2","E3")
    G.add_edge("J2","E3")
    G.add_edge("K2","E3")
    
    #Marchitez
    G.add_edge("B1","P2")
    G.add_edge("B1","N2")
    G.add_edge("P2","F3")
    G.add_edge("N2","F3")

    #Colores--Identificador
    color_map = []
    for node in G.nodes(data=True):
        dic = node[1]
        for p in x:
            if(dic["DATA"]==p):
                dic["SEC"] = 1

    for node in G.nodes(data=True):
        if(type(node[1]["REC"])!=str):
            contador = 0
            for p in x:
                for q in node[1]["REC"]:
                    if(q==p):
                        contador+=1
                        break
            node[1]["SEC"] = (contador/len(node[1]["REC"]))*100

    for node in G.nodes(data=True):
        dic = node[1]
        if(dic["SEC"]==1):
            color_map.append("yellow")
        elif(dic["SEC"]>10):
            if(dic["SEC"] < 45):
                color_map.append("green")
            elif(dic["SEC"]<65):
                color_map.append("yellow")
            else:
                color_map.append("red")
        else:
            color_map.append("cyan")

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
        "F3":(2,12)
    }

    ##INFORMACION

    sintomas = []
    for node in G.nodes(data=True):
        cui = ""
        if(node[1]["SEC"]>10):
            if(node[1]["SEC"]<30):
                cui = "Enfermedad:" + node[1]["DATA"] + "\n" "Consecuencia: " + node[1]["cons"] + "\n" + "Tratamiento: " + node[1]["trat"] + "\n" + 'moderado ('+  str(node[1]["SEC"])  + '%)'
            elif(node[1]["SEC"]<70):
                 cui = "Enfermedad:" + node[1]["DATA"] + "\n" "Consecuencia: " + node[1]["cons"] + "\n" + "Tratamiento: " + node[1]["trat"] + "\n" + 'Atención ('+  str(node[1]["SEC"])  + '%)'
            else:
                 cui = "Enfermedad:" + node[1]["DATA"] + "\n" "Consecuencia: " + node[1]["cons"] + "\n" + "Tratamiento: " + node[1]["trat"] + "\n" + 'Peligro extremo ('+  str(node[1]["SEC"])  + '%)'
            print(cui)

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

