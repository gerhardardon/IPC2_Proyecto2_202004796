import webbrowser
from os import system
from tkinter import Tk
from tkinter import filedialog as fd
from xml.dom import minidom
from ciudades import *
from filas import *
from casilla import *
from drones import *
from infocity import*

mydoc = ""
ciudad = ""
fila = ""
casilla = ""
dron = ""
city_selected=""


class bcolor:
    morado = "\033[1;35m"
    reset = '\033[0m'


def cargar():
    global ciudad, fila, casilla, dron
    ciudades = mydoc.getElementsByTagName('ciudad')  # Obtenemos los nodos con el tag 'ciudades'
    '''print('Cantidad de Ciudades del xml:')
    print(len(ciudades))
'''
    ciudad = lista_ciudades()
    i = 0
    while i < len(ciudades):
        name = ciudades[i].getElementsByTagName('nombre')[0].firstChild.data  # obtenemos nombre de la ciudad
        # print(name)

        row = ciudades[i].getElementsByTagName('nombre')[0].attributes['filas'].value  # obtenemos filas de ciudad
        column = ciudades[i].getElementsByTagName('nombre')[0].attributes[
            'columnas'].value  # obtenemos columnas de ciudad
        # print("filas", row, "columnas", column)

        # print(len(ciudades[i].getElementsByTagName('fila')))

        fila = lista_filas()
        j = 0
        while j < len(ciudades[i].getElementsByTagName('fila')):  # recorre todas las filas
            cont = (ciudades[i].getElementsByTagName('fila')[j].firstChild.data)  # obtenemos el contenido de cada fila
            cont = cont.replace('"', '')

            casilla = lista_casilla()
            posx = 0
            for x in cont:
                casilla.agregar(posx, x)
                # casilla.imprimir()

                posx += 1

            fila.agregar(j, casilla)

            j += 1

        # print(len(ciudades[i].getElementsByTagName('unidadMilitar')))

        ciudad.agregar(i, name, row, column, fila)
        j = 0
        while j < len(ciudades[i].getElementsByTagName('unidadMilitar')):  # recorre todas las UM

            row2 = ciudades[i].getElementsByTagName('unidadMilitar')[j].attributes['fila'].value  # obtiene fila de UM
            column2 = ciudades[i].getElementsByTagName('unidadMilitar')[j].attributes[
                'columna'].value  # obtiene columna de UM

            ciudad.setcolor(name, int(column2)-1, int(row2)-1, "M")
            # print("fila", row2, "coluna", column2, "vida", ciudades[i].getElementsByTagName('unidadMilitar')[j].firstChild.data)  # obtenemos el contenido de UM

            j += 1



        i += 1

    ########################### DRONES #########################################
    drones = mydoc.getElementsByTagName('robot')  # Obtenemos los nodos con el tag 'ciudades'
    '''print('Cantidad de Drones del xml:')
    print(len(drones))'''

    dron = lista_drones()
    i = 0
    while i < len(drones):
        name = drones[i].getElementsByTagName('nombre')[0].firstChild.data  # obtenemos nombre del dron
        # print(name)

        tipo = drones[i].getElementsByTagName('nombre')[0].attributes['tipo'].value  # obtenemos tipo de dron
        if tipo == "ChapinFighter":
            capacidad = drones[i].getElementsByTagName('nombre')[0].attributes[
                'capacidad'].value  # obtenemos capacidad de dron
        else:
            capacidad = None
        dron.agregar(i, name, tipo, capacidad)
        # print("tipo", tipo, "capacidad", capacidad)

        i += 1

    # dron.imprimir()


def grafica(codigo, row, column, code):
    with open(codigo + '.dot', 'w') as f:
        f.write('''
        digraph {
node [shape=plaintext]
rankdir=TB

A [label=<
  <table BORDER="0" CELLBORDER="1" CELLSPACING="0">
    
        ''')
        i = 0
        k = 0
        while i < int(row):
            #print("Row", i)
            f.write("<tr>")
            j = 0
            while j < int(column):
                #print("-", code[k])
                if code[k] == "*":
                    f.write('<td bgcolor="black">     </td>')
                elif code[k] == "#":
                    f.write('<td bgcolor="yellow">     </td>')
                    pass
                elif code[k] == "C":
                    f.write('<td bgcolor="skyblue">     </td>')
                elif code[k] == "E":
                    f.write('<td bgcolor="green">     </td>')
                elif code[k] == "R":
                    f.write('<td bgcolor="gray">     </td>')
                elif code[k] == "M":
                    f.write('<td bgcolor="red">     </td>')
                else:
                    f.write('<td bgcolor="white">     </td>')
                k = k + 1
                j = j + 1
            f.write("</tr>")
            i = i + 1
        f.write(''' </table>
    > ]

    }
    ''')
    try:
        system('dot -Tpng ' + codigo + '.dot -o ' + codigo + '.png')
        webbrowser.open_new_tab(codigo + '.png')
    except:
        print("")


maze = []
def convertirgrafica(row, column, code):
    global maze
    i = 0
    k = 0
    maze = []
    while i < int(row):
        #print("Row", i)
        # f.write("<tr>")
        linea = []
        j = 0
        while j < int(column):
            #print("-", code[k])
            if code[k] == "*":
                linea.append(1)
            elif code[k] == "C":
                linea.append(0)
            elif code[k] == "E":
                linea.append(0)
            elif code[k] == "R":
                linea.append(0)
            elif code[k] == "M":
                linea.append(0)
            else:
                linea.append(0)
            k = k + 1
            j = j + 1
        # f.write("</tr>")
        maze.append(linea)
        i = i + 1




def init():
    print("\n\n\n\n\n\n", bcolor.morado + "\n========== MENU ==========" + bcolor.reset)
    print(
        "Seleccione la opcion:\n   1. Cargar XML\n   2. Mostrar info de ciudades \n   3. Escoger misión \n   4. Salir")
    x = input()
    if x == "1":
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        filename = fd.askopenfilename(title="Select file")
        print(filename)
        global mydoc
        mydoc = minidom.parse(filename)
        cargar()
        print("\n\nXML CARGADO CON EXITO!")
    if x == "2":
        print("\n\n", bcolor.morado + "Lista de Ciudades:" + bcolor.reset)
        ciudad.imprimir()
        init()
    if x == "3":
        print("\n\n", bcolor.morado + "Seleccione una ciudad:" + bcolor.reset)
        ciudad.imprimir()

        global city_selected
        city_selected = input()
        row = ciudad.getrow(city_selected)
        column = ciudad.getcolumn(city_selected)
        code = ciudad.buscar(city_selected)
        grafica(city_selected, row, column, code)
        convertirgrafica(row, column, code)

        print("\n\n", bcolor.morado + "Seleccione un drone:" + bcolor.reset)
        dron.imprimir()
        drone_selected = input()

        print("\n\n", bcolor.morado + "Coordenada X de Entrada:" + bcolor.reset)
        oX=input()
        print("\n\n", bcolor.morado + "Coordenada Y de Entrada:" + bcolor.reset)
        oY = input()
        start = (int(oY), int(oX))

        print("\n\n", bcolor.morado + "Coordenada X de Objetivo:" + bcolor.reset)
        fX = input()
        print("\n\n", bcolor.morado + "Coordenada Y de Objetivo:" + bcolor.reset)
        fY = input()
        end = (int(fY), int(fX))


        path = astar(maze, start, end)
        #print(path)
        for x in path:
            ciudad.setcolor(city_selected, x[1], x[0], "#")

        row = ciudad.getrow(city_selected)
        column = ciudad.getcolumn(city_selected)
        code = ciudad.buscar(city_selected)
        grafica("Solution", row, column, code)

        tipo=dron.gettipo(drone_selected)
        if tipo=="ChapinFighter":
            print(bcolor.morado, "\n\n\nTipo de Mision:", bcolor.reset," extraccion de recursos")
            print(bcolor.morado, "Drone utlizado:", bcolor.reset,drone_selected+"("+tipo+")")
        else:
            print(bcolor.morado, "\n\n\nTipo de Mision:", bcolor.reset, " rescate")
            print(bcolor.morado, "Drone utilizado:", bcolor.reset,drone_selected+"("+tipo+")")

        print(bcolor.morado, "Objetivo en:", bcolor.reset,"("+fX+","+fY+")")
        init()

    if x == "4":


        exit()
    else:
        init()


if __name__ == '__main__':
    init()
