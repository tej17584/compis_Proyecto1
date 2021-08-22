"""
Nombre: Alejandro Tejada
Curso: Diseño Compiladores
Fecha: agosto 2021
Programa: ErrorClass.py
Propósito: este programa maneja los errores que podemos chequear
           y los imprime en consola
V 1.0
"""


class Errores():
    """
    Esta clase se encarga de los errores que puedan surgir y que podamos
    manejar a nivel lógico sin necesidad de tabla de símbolos
    """

    def __init__(self, nombre="", columna="", linea="", tipo="") -> None:
        self.nombre = nombre
        self.columna = columna
        self.linea = linea
        self.tipo = tipo

    def checkArrayError(self, numero, isLetter):
        """
        Método general de chequeado de errores para arrays
        *@param numero: es el numero declarado en el array
        *@param isLetter: indica si estamos tanteando una letra
        """
        # Chequeo de regla semántica: num en la
        # declaración de un arreglo debe de ser mayor a 0.
        if(numero <= 0 and (isLetter == False)):
            return True, f'Error de declaración del array con nombre:{self.nombre}. En linea: {self.linea}, columna:{self.columna}. El valor declarado es de : -> {numero} <- y se espera uno mayor a 0'
        elif(numero <= 0 and (isLetter == True)):
            return True, f'Error de declaración del array con nombre:{self.nombre}. En linea: {self.linea}, columna:{self.columna}. La variable usada DENTRO del array tiene un valor de: -> {numero} <- y se espera uno mayor a 0'
        return False, ""
