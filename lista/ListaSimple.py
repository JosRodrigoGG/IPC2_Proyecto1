from bin.Nodo import Nodo

class ListaSimple():

    def __init__(self):
        self.__primero = None

    def vacia(self):
        if self.__primero == None:
            return True

        return False

    def agregar(self, dato):
        if self.vacia():
            self.__primero = Nodo(dato)
        else:
            aux = self.__primero

            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()

            if aux.getSiguiente() == None:
                aux.setSiguiente(Nodo(dato))

    def getLista(self):
        return self.__primero