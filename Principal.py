import sys
from os import system

class Principal():

    def menu(self):
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
            print(">", end="")

            entrada = input()

            try:
                entrada = int(entrada)
            except ValueError:
                entrada = 0

            if entrada in range(1,7):
                if entrada == 1:
                    # Cargar archivo
                    pass
                elif entrada == 2:
                    # Procesar archivo
                    pass
                elif entrada == 3:
                    # Escribir archivo salida
                    pass
                elif entrada == 4:
                    # Mostrar datos del estudiante
                    pass
                elif entrada == 5:
                    # Generar grafica
                    pass
                elif entrada == 6:
                    system("cls")

                    sys.exit(0)
            else:
                self.mensajeError("opcion invalida")

    def mensajeError(self, mensaje):
        system("cls")

        print("")
        print(">> " + mensaje)
        print("> ", end="")

        temp = input()