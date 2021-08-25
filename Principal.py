import os
import sys
from os import system
from tkinter import filedialog
from xml.dom import minidom

import graphviz as graphviz
from graphviz import Digraph
import os.path as path
import numpy as np
import xml.etree.ElementTree as ET

from bin.Terreno import Terreno
from bin.TerrenoSalida import TerrenoSalida
from lista.ListaSimple import ListaSimple

class Principal():

    def menu(self):
        terrenos = ListaSimple()
        terrenosProcesados = ListaSimple()

        while True:
            system("cls")

            print("")
            print("----------------------------------------------------")
            print("| INTRODUCCION A LA COMPUTACION Y PROGRAMACION 2  |")
            print("|     Jose Rodrigo Garcia Godinez / 201801295      |")
            print("----------------------------------------------------")
            print("")
            print("MENU PRINCIPAL")
            print("")
            print("1. Cargar archivo")
            print("2. Procesar archivo")
            print("3. Escribir archivo salida")
            print("4. Mostrar datos del estudiante")
            print("5. Generar grafica")
            print("6. Salir")
            print("")
            print(">> Ingrese una opcion")
            print("> ", end="")

            entrada = input()

            try:
                entrada = int(entrada)
            except ValueError:
                entrada = 0

            if entrada in range(1, 7):
                if entrada == 1:
                    # Cargar archivo

                    system("cls")

                    print("")
                    print("CARGAR ARCHIVO")
                    print(">")

                    ruta = filedialog.askopenfilename(initialdir="/",
                                                      title="Seleccione archivo", filetypes=(("xml files", "*.xml"),
                                                                                             ("all files", "*.*")))

                    if path.isfile(ruta):
                        archivo_xml = minidom.parse(ruta)
                        items = archivo_xml.getElementsByTagName("terreno")

                        for temp in items:
                            terreno = Terreno()
                            terreno.setNombre(str(temp.attributes["nombre"].value))

                            inicioX = None
                            inicioY = None

                            posicion = temp.getElementsByTagName("posicioninicio")
                            for tempPosicion in posicion:
                                inicioX = int(tempPosicion.getElementsByTagName("x")[0].childNodes[0].data)
                                inicioY = int(tempPosicion.getElementsByTagName("y")[0].childNodes[0].data)

                            terreno.setInicio(inicioX, inicioY)

                            finX = None
                            finY = None

                            posicion = temp.getElementsByTagName("posicionfin")
                            for tempPosicion in posicion:
                                finX = int(tempPosicion.getElementsByTagName("x")[0].childNodes[0].data)
                                finY = int(tempPosicion.getElementsByTagName("y")[0].childNodes[0].data)

                            terreno.setFin(finX, finY)

                            posiciones = temp.getElementsByTagName("posicion")

                            for tempPosicion in posiciones:
                                terreno.agregarPosicion(int(tempPosicion.attributes["x"].value),
                                                        int(tempPosicion.attributes["y"].value),
                                                        int(tempPosicion.childNodes[0].data))

                            terrenos.agregar(terreno)

                    system("cls")

                    print("")
                    print(">> Archivo cargado")
                    print("> ", end="")

                    _temp = input()
                elif entrada == 2:
                    # Procesar archivo

                    system("cls")

                    if terrenos.vacia():
                        print("")
                        print(">> No hay terrenos cargados")
                    else:
                        print("")
                        print(">> TERRENOS CARGADOS")
                        print("")

                        _aux = terrenos.getLista()
                        _tempContador = 0
                        while _aux:
                            _tempContador += 1
                            print("> " + str(_tempContador) + ".. " + _aux.getDato().getNombre())
                            _aux = _aux.getSiguiente()

                        print("")
                        print(">> Seleccione un terreno")
                        print("> ", end="")

                        _tempOpcion = input()

                        try:
                            _tempOpcion = int(_tempOpcion)
                        except ValueError:
                            _tempOpcion = 0

                        if (_tempOpcion == 0) or (_tempOpcion > _tempContador):
                            print("")
                            print(">> Opcion invalida")
                        else:
                            _aux = terrenos.getLista()
                            _tempAux = 1
                            while _aux:
                                if _tempAux == _tempOpcion:
                                    system("cls")

                                    print("")
                                    print("TERRENO: " + str(_aux.getDato().getNombre()))
                                    print("")

                                    print(">>Mejor ruta")

                                    _rutas = []
                                    _posiciones = _aux.getDato().getPosiciones()
                                    _posX = 0
                                    _posY = 0
                                    while _posiciones:
                                        _rutas.append(_posiciones.getDato())
                                        if _posX < _posiciones.getDato().getX():
                                            _posX = int(_posiciones.getDato().getX())

                                        if _posY < _posiciones.getDato().getY():
                                            _posY = int(_posiciones.getDato().getY())
                                        _posiciones = _posiciones.getSiguiente()

                                    _tempMatriz = np.zeros((int(_posY), int(_posX)), dtype=np.int16)

                                    for _tempRuta in _rutas:
                                        _tempMatriz[_tempRuta.getY() - 1][_tempRuta.getX() - 1] = _tempRuta.getValor()

                                    _terrenoSalida = TerrenoSalida(_aux.getDato().getNombre())
                                    _terrenoSalida.setInicio(_aux.getDato().getInicio().getX(), _aux.getDato().getInicio().getY())
                                    _terrenoSalida.setFin(_aux.getDato().getFin().getX(), _aux.getDato().getFin().getY())

                                    _inicioX = _aux.getDato().getInicio().getX() - 1
                                    _inicioY = _aux.getDato().getInicio().getY() - 1
                                    _finX = _aux.getDato().getFin().getX() - 1
                                    _finY = _aux.getDato().getFin().getY() - 1

                                    _X = _inicioX
                                    _Y = _inicioY

                                    _posX = _posX - 1
                                    _posY = _posY - 1

                                    _terrenoSalida.agregarPosicion(_X+1, _Y+1, _tempMatriz[_Y][_X])

                                    while True:
                                        if _X == 0 and _Y == 0:
                                            if _tempMatriz[0][1] <= _tempMatriz[1][0]:
                                                if _inicioX < _finX:
                                                    _X = 1
                                                else:
                                                    _Y = 1
                                            else:
                                                if _inicioY < _finY:
                                                    _Y = 1
                                                else:
                                                    _X = 1
                                        elif _X == _posX and _Y == 0:
                                            if _tempMatriz[0][_X - 1] <= _tempMatriz[1][_X]:
                                                if _inicioX > _finX:
                                                    _X -= 1
                                                else:
                                                    _Y += 1
                                            else:
                                                if _inicioY < _finY:
                                                    _Y += 1
                                                else:
                                                    _X -= 1
                                        elif _X == _posX and _Y == _posY:
                                            if _tempMatriz[_Y][_X-1] <= _tempMatriz[_Y-1][_X]:
                                                if _inicioX > _finX:
                                                    _X -= 1
                                                else:
                                                    _Y -= 1
                                            else:
                                                if _inicioY > _finY:
                                                    _Y -= 1
                                                else:
                                                    _X -= 1
                                        elif _X == 0 and _Y == _posY:
                                            if _tempMatriz[_Y][1] <= _tempMatriz[_Y-1][0]:
                                                if _inicioX < _finX:
                                                    _X = 1
                                                else:
                                                    _Y -= 1
                                            else:
                                                if _inicioY > _finY:
                                                    _Y -= 1
                                                else:
                                                    _X = 1
                                        elif 0 < _X < _posX and _Y == 0:
                                            if _inicioX < _finX:
                                                if _tempMatriz[0][_X+1] <= _tempMatriz[1][_X]:
                                                    _X += 1
                                                else:
                                                    if _inicioY < _finY:
                                                        _Y = 1
                                                    else:
                                                        _X += 1
                                            else:
                                                if _tempMatriz[0][_X-1] <= _tempMatriz[1][_X]:
                                                    _X -= 1
                                                else:
                                                    if _inicioY < _finY:
                                                        _Y = 1
                                                    else:
                                                        _X -= 1
                                        elif 0 < _X < _posX and _Y == _posY:
                                            if _inicioX < _finX:
                                                if _tempMatriz[_Y][_X+1] <= _tempMatriz[_Y-1][_X]:
                                                    _X += 1
                                                else:
                                                    _Y -= 1
                                            else:
                                                if _tempMatriz[_Y][_X-1] <= _tempMatriz[_Y-1][_X]:
                                                    _X -= 1
                                                else:
                                                    _Y -= 1
                                        elif 0 < _Y < _posY and _X == 0:
                                            if _inicioY < _finY:
                                                if _tempMatriz[_Y+1][0] <= _tempMatriz[_Y][1]:
                                                    _Y += 1
                                                else:
                                                    _X = 1
                                            else:
                                                if _tempMatriz[_Y-1][0] <= _tempMatriz[_Y][1]:
                                                    _Y -= 1
                                                else:
                                                    _X = 1
                                        elif 0 < _Y < _posY and _X == _posX:
                                            if _inicioY < _finY:
                                                if _tempMatriz[_Y+1][_X] <= _tempMatriz[_Y][_X-1]:
                                                    _Y += 1
                                                else:
                                                    _X -= 1
                                            else:
                                                if _tempMatriz[_Y-1][_X] <= _tempMatriz[_Y][_X-1]:
                                                    _Y -= 1
                                                else:
                                                    _X -= 1
                                        elif 0 < _X < _posX and 0 < _Y < _posY:
                                            if _inicioX < _finX:
                                                if _inicioY < _finY:
                                                    if _tempMatriz[_Y + 1][_X] <= _tempMatriz[_Y][_X + 1]:
                                                        _Y += 1
                                                    else:
                                                        _X += 1
                                                else:
                                                    if _tempMatriz[_Y - 1][_X] <= _tempMatriz[_Y][_X + 1]:
                                                        _Y -= 1
                                                    else:
                                                        _X += 1
                                            else:
                                                if _inicioY < _finY:
                                                    if _tempMatriz[_Y + 1][_X] <= _tempMatriz[_Y][_X - 1]:
                                                        _Y += 1
                                                    else:
                                                        _X -= 1
                                                else:
                                                    if _tempMatriz[_Y - 1][_X] <= _tempMatriz[_Y][_X - 1]:
                                                        _Y -= 1
                                                    else:
                                                        _X -= 1

                                        _terrenoSalida.agregarPosicion(_X+1, _Y+1, _tempMatriz[_Y][_X])
                                        if _X == _finX and _Y == _finY:
                                            break

                                    _tempMatriz = np.zeros((len(_tempMatriz[0]), len(_tempMatriz)), dtype=np.int16)

                                    _aux = _terrenoSalida.getPosiciones()
                                    while _aux:
                                        _X = _aux.getDato().getY() - 1
                                        _Y = _aux.getDato().getX() - 1
                                        _tempMatriz[_Y][_X] = 1

                                        _aux = _aux.getSiguiente()

                                    print("")
                                    for i in range(len(_tempMatriz)):
                                        _temp = "| "
                                        for j in range(len(_tempMatriz[i])):
                                            _temp = _temp + str(_tempMatriz[i][j]) + " | "
                                        print(_temp)

                                    print(" ")
                                    print(">>Cantidad de combustible")

                                    _combustible = 0

                                    _auxCombustible = _terrenoSalida.getPosiciones()
                                    while _auxCombustible:
                                        _combustible += int(_auxCombustible.getDato().getValor())
                                        _auxCombustible = _auxCombustible.getSiguiente()

                                    _terrenoSalida.setCombustible(_combustible)

                                    terrenosProcesados.agregar(_terrenoSalida)
                                    break
                                else:
                                    _aux = _aux.getSiguiente()
                                    _tempAux += 1

                    print("")
                    print(">> Continuar")
                    print("> ", end="")

                    _temp = input()
                elif entrada == 3:
                    # Escribir archivo salida

                    system("cls")

                    print("")
                    print(">> Guardar archivo de salida")
                    print(">")

                    _guardarArchivo = filedialog.asksaveasfilename(initialdir="/", title="Guardar archivo de salida",
                                                                   defaultextension=".xml",
                                                                   filetypes=(("xml","*.xml"),
                                                                              ("txt", "*.txt"),
                                                                              ("All files","*")))
                    data = ET.Element("terrenos")

                    _aux = terrenosProcesados.getLista()
                    while _aux:
                        _terreno = ET.SubElement(data, "terreno")
                        _terreno.set("nombre",str(_aux.getDato().getNombre()))

                        _posInicial = ET.SubElement(_terreno, "posicioninicio")
                        _X = ET.SubElement(_posInicial, "x")
                        _X.text = str(_aux.getDato().getInicio().getX())
                        _Y = ET.SubElement(_posInicial, "y")
                        _Y.text = str(_aux.getDato().getInicio().getY())

                        _posFinal = ET.SubElement(_terreno, "posicionfin")
                        _X = ET.SubElement(_posFinal, "x")
                        _X.text = str(_aux.getDato().getFin().getX())
                        _Y = ET.SubElement(_posFinal, "y")
                        _Y.text = str(_aux.getDato().getFin().getY())

                        _combustible = ET.SubElement(_terreno, "combustible")
                        _combustible.text = str(_aux.getDato().getCombustible())

                        _auxPosicion = _aux.getDato().getPosiciones()
                        while _auxPosicion:
                            _posicion = ET.SubElement(_terreno, "posicion")
                            _posicion.set("x", str(_auxPosicion.getDato().getX()))
                            _posicion.set("y", str(_auxPosicion.getDato().getY()))
                            _posicion.text = str(_auxPosicion.getDato().getValor())

                            _auxPosicion = _auxPosicion.getSiguiente()

                        _aux = _aux.getSiguiente()

                    with open(_guardarArchivo, "wb") as f:
                        f.write(ET.tostring(data))
                elif entrada == 4:
                    # Mostrar datos del estudiante

                    system("cls")

                    print("DATOS ESTUDIANTE")
                    print("")
                    print("> Jose Rodrigo Garcia Godinez")
                    print("> 201801295")
                    print("> Introduccion a la Programacion y Computacion 2 seccion A")
                    print("> Ingenieria en Ciencias y Sistemas")
                    print("> 4to Semestre")

                    print("")
                    print(">> Continuar")
                    print("> ", end="")

                    _temp = input()
                elif entrada == 5:
                    # Generar grafica

                    system("cls")

                    if terrenos.vacia():
                        print("")
                        print(">> No hay terrenos cargados")
                        print("")
                    else:
                        print("")
                        print(">> TERRENOS CARGADOS")
                        print("")

                        _aux = terrenos.getLista()
                        _tempContador = 0
                        while _aux:
                            _tempContador += 1
                            print("> " + str(_tempContador) + ".. " + _aux.getDato().getNombre())
                            _aux = _aux.getSiguiente()

                        print("")
                        print(">> Seleccione un terreno")
                        print("> ", end="")

                        _tempOpcion = input()

                        try:
                            _tempOpcion = int(_tempOpcion)
                        except ValueError:
                            _tempOpcion = 0

                        if (_tempOpcion == 0) or (_tempOpcion > _tempContador):
                            print("")
                            print(">> Opcion invalida")
                        else:
                            _aux = terrenos.getLista()
                            _tempAux = 1
                            while _aux:
                                if _tempAux == _tempOpcion:

                                    _directorio = filedialog.askdirectory()

                                    if _directorio != "":
                                        os.chdir(_directorio)

                                        grafico = graphviz.Digraph('G', filename=str(_aux.getDato().getNombre()), format="png", directory=str(os.getcwd()))

                                        _auxPosicion = _aux.getDato().getPosiciones()
                                        _posX = 0
                                        _posY = 0
                                        _rutas = []
                                        while _auxPosicion:
                                            _rutas.append(_auxPosicion.getDato())
                                            if _posX < _auxPosicion.getDato().getX():
                                                _posX = int(_auxPosicion.getDato().getX())

                                            if _posY < _auxPosicion.getDato().getY():
                                                _posY = int(_auxPosicion.getDato().getY())
                                            _auxPosicion = _auxPosicion.getSiguiente()

                                        _tempMatriz = np.zeros((int(_posY), int(_posX)), dtype=np.int16)

                                        for _temp in _rutas:
                                            _tempMatriz[_temp.getY() - 1][_temp.getX() - 1] = _temp.getValor()

                                        grafico.attr(rankdir="LR")
                                        grafico.attr("node", shape="circle")

                                        _contadorY = 0
                                        _contadorX = 0

                                        grafico.attr(rank="same")
                                        for i in range(len(_tempMatriz)):
                                            for j in range(len(_tempMatriz[i])):
                                                grafico.node(str("X" + str(j) + "Y" + str(i)),
                                                             label=str(_tempMatriz[i][j]))

                                        for i in range(len(_tempMatriz)):
                                            for j in range(len(_tempMatriz[i])):
                                                if i < len(_tempMatriz) - 1:
                                                    pos1 = str("X" + str(j) + "Y" + str(i))
                                                    pos2 = str("X" + str(j) + "Y" + str(i + 1))
                                                    grafico.edge(pos1, pos2)

                                        for i in range(len(_tempMatriz)):
                                            for j in range(len(_tempMatriz[i])):
                                                if j < len(_tempMatriz[i]) - 1:
                                                    pos1 = str("X" + str(j) + "Y" + str(i))
                                                    pos2 = str("X" + str(j + 1) + "Y" + str(i))
                                                    grafico.edge(pos1, pos2)

                                        grafico.attr(label=str(_aux.getDato().getNombre()))
                                        grafico.attr(fontsize="20")
                                        grafico.view()
                                    else:
                                        system("cls")

                                        print("")
                                        print(">> No se selecciono el directorio")

                                    system("cls")
                                    print(">> Gráfico generado")
                                    break
                                else:
                                    _aux = _aux.getSiguiente()
                                    _tempAux += 1

                    print("")
                    print(">> Continuar")
                    print("> ", end="")

                    _temp = input()
                elif entrada == 6:
                    # Salir

                    system("cls")

                    sys.exit(0)
            else:
                system("cls")

                print("")
                print(">> Opcion invalida")
                print("> ", end="")

                _temp = input()

