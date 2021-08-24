from bin.Fin import Fin
from bin.Inicio import Inicio
from bin.Posicion import Posicion
from lista.ListaSimple import ListaSimple


class TerrenoSalida():

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__combustible = None
        self.__inicio = None
        self.__fin = None
        self.__posiciones = ListaSimple()

    def getNombre(self):
        return self.__nombre

    def getCombustible(self):
        return self.__combustible

    def getInicio(self):
        return self.__inicio

    def getFin(self):
        return self.__fin

    def getPosiciones(self):
        return self.__posiciones.getLista()

    def setInicio(self, x, y):
        self.__inicio = Inicio(x,y)

    def setFin(self, x, y):
        self.__fin = Fin(x,y)

    def setCombustible(self, combustible):
        self.__combustible = int(combustible)

    def agregarPosicion(self, x, y, valor):
        self.__posiciones.agregar(Posicion(x,y,valor))