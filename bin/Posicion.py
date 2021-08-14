class Posicion():

    def __init__(self, x, y, valor):
        self.__x = x
        self.__y = y
        self.__valor = valor

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getValor(self):
        return  self.__valor