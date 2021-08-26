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
from antlr4.tree.Tree import Tree
from funciones import *
import sys
import json


class symbolTables():
    def __init__(self) -> None:
        # {1 : ["a", int", "main", 0, 0 ], "b": ["string", "y", "global", 0,0]}
        self.dictVars = {}
        # {1 : ["A", "a", "int" ], 2: ["B", "variable", "int"]}
        self.dictStructs = {}
        # {1: :["main", "void", ["param1", "param2"], ["resultado"]]}
        self.dictMethods = {}
        self.functions = funciones()  # funciones necesarias y varias
        self.contadorGlobalDictVars = 0
        self.contadorGlobalDictMethods = 0
        self.contadorGlobalDictStructs = 0

    def getDictVar(self):
        return self.dictVars

    def getVarIDVarDictVar(self, varID):
        """
        Dada un varID, retorna el nombre de la variable si existe en la tabla de variables.
        *@param: varID: el id de la variable a checar el tipo
        """
        for numeroTupla, valorTupla in self.dictVars.items():
            if(valorTupla[0] == varID):
                return valorTupla[0]  # retornamos el nombre de la tabla

        return ""

    def getTypeVarDictVar(self, varID, scope):
        """
        Dada un varID, retorna el tipo si existe en la tabla de variables.
        *@param: varID: el id de la variable a checar el tipo
        """
        for numeroTupla, valorTupla in self.dictVars.items():
            if((str(varID) == str(valorTupla[0])) and (str(scope) == valorTupla[2])):
                return valorTupla[1]  # retornamos el tipo de la tabla

        return ""

    def getScopeVarDictVar(self, varID):
        """
        Dada un varID, retorna el valor si existe en la tabla de variables.
        *@param: varID: el id de la variable a checar
        """
        for numeroTupla, valorTupla in self.dictVars.items():
            if(valorTupla[0] == varID):
                return valorTupla[2]  # retornamos el scope de la tabla

        return ""

    def getValorVarDictVar(self, varID, scope):
        """
        Dada un varID, retorna el valor si existe en la tabla de variables.
        *@param: varID: el id de la variable a checar
        """
        for numeroTupla, valorTupla in self.dictVars.items():
            if((str(varID) == str(valorTupla[0])) and (str(scope) == valorTupla[2])):
                return valorTupla[3]  # retornamos el valor de la tabla
        return ""

    def getOffsetVarDictVar(self, varID, scope):
        """
        Dada un varID, retorna el valor si existe en la tabla de variables.
        *@param: varID: el id de la variable a checar
        """
        for numeroTupla, valorTupla in self.dictVars.items():
            if((str(varID) == str(valorTupla[0])) and (str(scope) == valorTupla[2])):
                return valorTupla[4]  # retornamos el offset de la tabla

        return ""

    def AddNewVar_DictVar(self, varID="", varType="", methodID="", valor=0, offset=0):
        """
        Agrega una nueva tupla a la tabla de simbolos.
        *@param: varID: el nombre de la variable
        *@param: varType: el tipo de la variable
        *@param: methodID: el método  o scope al que pertenece de la variable
        *@param: valor: el valor de la variable
        *@param: offset: el offset de la variable
        """
        existsEntry = self.checkVarInVarSymbolTableV2(varID, methodID)
        # colocamos en el orden especificado
        arraynuevo = [varID, varType, methodID, valor, offset]
        # si la entrada NO existe
        if(existsEntry == False):
            # agregamos una nueva entrada al diccionario
            self.dictVars[self.contadorGlobalDictVars] = arraynuevo
            self.contadorGlobalDictVars += 1
        else:
            print("Error a nivel de tabla de simbolos. La entrada ya existe.")

    def checkVarInVarSymbolTable(self, variable, scope):
        """
        Revisa si una variable dada EXISTE en la tabla de simbolos de variables
        Si existe, retorna TRUE y el valor de esa variable. Si no, retorna False
        *@param: variable: la variable a verificar en la tabla de simbolos
        """
        for numeroTupla, valorTupla in self.dictVars.items():
            if(str(variable) == str(valorTupla[0])):
                return True, self.getValorVarDictVar(variable, scope)

        return False, ""

    def checkVarInVarSymbolTableV2(self, variable, scope):
        """
        Revisa si una variable dada EXISTE en la tabla de simbolos de variables
        Si existe, retorna TRUE. Si no, retorna False
        *@param: variable: la variable a verificar en la tabla de simbolos
        *@param: scope: elscope de la variable, ya que podemos tener dos distintas
        """
        existsDictVar = False
        for numeroTupla, valorTupla in self.dictVars.items():
            if((str(variable) == str(valorTupla[0])) and (str(scope) == valorTupla[2])):
                existsDictVar = True

        if((existsDictVar == True)):
            return True
        else:
            return False
