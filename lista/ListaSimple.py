from bin.Nodo import Nodo


class ListaSimple():

    def __init__(self):
        self.__primero = None
        self.__identificador = 0

    def vacia(self):
        if self.__primero == None:
            return True

        return False

    def agregar(self, dato):
        if self.vacia():
            self.__primero = Nodo(dato)
            self.__identificador += 1
            self.__primero.setIdentificador(self.__identificador)
        else:
            aux = self.__primero

            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()

            if aux.getSiguiente() == None:
                aux.setSiguiente(Nodo(dato))
                self.__identificador += 1
                aux.getSiguiente().setIdentificador(self.__identificador)

    def getLista(self):
        return self.__primero

    def getIdentificador(self):
        return  self.__identificador