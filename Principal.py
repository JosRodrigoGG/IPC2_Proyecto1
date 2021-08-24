import sys
from os import system
from tkinter import filedialog
from xml.dom import minidom
# from graphviz import Digraph
import os.path as path
import numpy as np

from bin.Posicion import Posicion
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

                                    print(">>Calcular la mejor ruta")

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

                                    _tempSalida = []
                                    _inicioX = _aux.getDato().getInicio().getX() - 1
                                    _inicioY = _aux.getDato().getInicio().getY() - 1
                                    _finX = _aux.getDato().getFin().getX() - 1
                                    _finY = _aux.getDato().getFin().getY() - 1

                                    _X = _inicioX
                                    _Y = _inicioY

                                    _posX = _posX - 1
                                    _posY = _posY - 1

                                    print(_tempMatriz)
                                    print(_X)
                                    print(_Y)
                                    while True:
                                        if _X == 0 and _Y == 0:
                                            

                                            if _tempMatriz[0][1] < _tempMatriz[1][0]:
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
                                            if _tempMatriz[0][_X - 1] < _tempMatriz[1][_X]:
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
                                            if _tempMatriz[_Y][_X-1] < _tempMatriz[_Y-1][_X]:
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
                                            if _tempMatriz[_Y][1] < _tempMatriz[_Y-1][0]:
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
                                                if _tempMatriz[0][_X+1] < _tempMatriz[1][_X]:
                                                    _X += 1
                                                else:
                                                    _Y = 1
                                            else:
                                                if _tempMatriz[0][_X-1] < _tempMatriz[1][_X]:
                                                    _X -= 1
                                                else:
                                                    _Y = 1
                                        elif 0 < _X < _posX and _Y == _posY:
                                            if _inicioX < _finX:
                                                if _tempMatriz[_Y][_X+1] < _tempMatriz[_Y-1][_X]:
                                                    _X += 1
                                                else:
                                                    _Y -= 1
                                            else:
                                                if _tempMatriz[_Y][_X-1] < _tempMatriz[_Y-1][_X]:
                                                    _X -= 1
                                                else:
                                                    _Y -= 1
                                        elif 0 < _Y < _posY and _X == 0:
                                            if _inicioY < _finY:
                                                if _tempMatriz[_Y+1][0] < _tempMatriz[_Y][1]:
                                                    _Y += 1
                                                else:
                                                    _X = 1
                                            else:
                                                if _tempMatriz[_Y-1][0] < _tempMatriz[_Y][1]:
                                                    _Y -= 1
                                                else:
                                                    _X = 1
                                        elif 0 < _Y < _posY and _X == _posX:
                                            print("A")
                                            if _inicioY < _finY:
                                                if _tempMatriz[_Y+1][_X] < _tempMatriz[_Y][_X-1]:
                                                    _Y += 1
                                                else:
                                                    _X -= 1
                                            else:
                                                if _tempMatriz[_Y-1][_X] < _tempMatriz[_Y][_X-1]:
                                                    _Y -= 1
                                                else:
                                                    _X -= 1
                                        elif 0 < _X < _posX and 0 < _Y < _posY:
                                            if _inicioX < _finX:
                                                if _inicioY < _finY:
                                                    if _tempMatriz[_Y + 1][_X] < _tempMatriz[_Y][_X + 1]:
                                                        _Y += 1
                                                    else:
                                                        _X += 1
                                                else:
                                                    if _tempMatriz[_Y - 1][_X] < _tempMatriz[_Y][_X + 1]:
                                                        _Y -= 1
                                                    else:
                                                        _X += 1
                                            else:
                                                if _inicioY < _finY:
                                                    if _tempMatriz[_Y + 1][_X] < _tempMatriz[_Y][_X - 1]:
                                                        _Y += 1
                                                    else:
                                                        _X -= 1
                                                else:
                                                    if _tempMatriz[_Y - 1][_X] < _tempMatriz[_Y][_X - 1]:
                                                        _Y -= 1
                                                    else:
                                                        _X -= 1

                                        print("X=" + str(_X) + " Y=" + str(_Y))
                                        if _X == _finX and _Y == _finY:
                                            break

                                    print("---------------")
                                    print(_X)
                                    print(_Y)

                                    print(">> Calcular cantidad de combustible")

                                    # combustible

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
                    pass
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
                    pass
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

