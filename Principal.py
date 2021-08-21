import sys
from os import system
from tkinter import filedialog
from xml.dom import minidom
# from graphviz import Digraph
import os.path as path

from bin.Terreno import Terreno
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

            if entrada in range(1,7):
                if entrada == 1:
                    # Cargar archivo

                    system("cls")

                    print("")
                    print("CARGAR ARCHIVO")
                    print(">")

                    ruta = filedialog.askopenfilename(initialdir = "/",
                                title = "Seleccione archivo",filetypes = (("xml files","*.xml"),
                                ("all files","*.*")))

                    if path.isfile(ruta):
                        archivo_xml =  minidom.parse(ruta)
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
                            _tempOpcion = int(entrada)
                        except ValueError:
                            _tempOpcion = 0

                        if _tempOpcion == 0:
                            print("")
                            print(">> Opcion invalida")
                        else:
                            print("")

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
                    system("cls")

                    sys.exit(0)
            else:
                system("cls")

                print("")
                print(">> Opcion invalida")
                print("> ", end="")

                _temp = input()
