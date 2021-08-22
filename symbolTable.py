"""
Nombre: Alejandro Tejada
Curso: Diseño Compiladores
Fecha: agosto 2021
Programa: tablaSimbolos.py
Propósito: Este programa alojara a 3 clases, cada una será una tabla de simbolos.
Asi como diccionarios y métodos globales para saber lo que se espera de cada una
V 1.0
"""

# ZONA DE IMPORTS
from funciones import *
import sys
import json


class symbolTables():
    def __init__(self) -> None:
        # {"a" : ["int", "y"], "b": ["char", "y"]}
        self.dictStructs = {}
        # {"a" : ["int", "main", 4 ]}
        self.dictVars = {"asssss": ["int", "main", 10, 0]}
        # {"main":["void", ["param1", "param2"]]}
        self.dictMethods = {}
        self.functions = funciones()  # funciones necesarias y varias

    def getTypeVarDictVar(self, varID):
        """
        Dada un varID, retorna el tipo si existe en la tabla de variables.
        *@param: varID: el id de la variable a checar el tipo
        """
        for variableID, valor in self.dictVars.items():
            if(variableID == varID):
                return valor[0]  # retornamos el VALOR de la tabla

        return ""

    def getScopeVarDictVar(self, varID):
        """
        Dada un varID, retorna el valor si existe en la tabla de variables.
        *@param: varID: el id de la variable a checar
        """
        for variableID, valor in self.dictVars.items():
            if(variableID == varID):
                return valor[1]  # retornamos el VALOR de la tabla

        return ""

    def getValorVarDictVar(self, varID):
        """
        Dada un varID, retorna el valor si existe en la tabla de variables.
        *@param: varID: el id de la variable a checar
        """
        for variableID, valor in self.dictVars.items():
            if(variableID == varID):
                return valor[2]  # retornamos el VALOR de la tabla

        return ""

    def getOffsetVarDictVar(self, varID):
        """
        Dada un varID, retorna el valor si existe en la tabla de variables.
        *@param: varID: el id de la variable a checar
        """
        for variableID, valor in self.dictVars.items():
            if(variableID == varID):
                return valor[3]  # retornamos el VALOR de la tabla

        return ""

    def checkVarInVarSymbolTable(self, variable):
        """
        Revisa si una variable dada EXISTE en la tabla de simbolos de variables
        Si existe, retorna TRUE y el valor de esa variable. Si no, retorna False
        *@param: variable: la variable a verificar en la tabla de simbolos
        """
        for nombreVariable, valores in self.dictVars.items():
            if(str(variable) == str(nombreVariable)):
                return True, self.getValorVarDictVar(variable)

        return False, ""
