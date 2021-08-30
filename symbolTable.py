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
        # {1: :["main", "void", ["param1", "param2"], [True]]}
        self.dictMethods = {}
        self.functions = funciones()  # funciones necesarias y varias
        self.contadorGlobalDictVars = 0
        self.contadorGlobalDictMethods = 0
        self.contadorGlobalDictStructs = 0

    # ! ------------------------- METODOS DE DICCIONARIO DE METODOS ---------
    def getDictVar(self):
        """
        Retorna el diccionario de variables
        """
        return self.dictVars

    def getVarIDVarDictVar(self, varID, scope):
        """
        Dada un varID, retorna el nombre de la variable si existe en la tabla de variables.
        *@param: varID: el id de la variable a checar el tipo
        *@param: scope: el scope actual
        """
        for numeroTupla, valorTupla in self.dictVars.items():
            if(valorTupla[0] == varID and (str(scope) == valorTupla[2])):
                return valorTupla[0]  # retornamos el nombre de la tabla

        return ""

    def getTypeVarDictVar(self, varID, scope):
        """
        Dada un varID, retorna el tipo si existe en la tabla de variables.
        *@param: varID: el id de la variable a checar el tipo
        *@param: scope: el scope actual
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
        *@param: scope: el scope actual
        """
        for numeroTupla, valorTupla in self.dictVars.items():
            if((str(varID) == str(valorTupla[0])) and (str(scope) == valorTupla[2])):
                return valorTupla[3]  # retornamos el valor de la tabla
        return ""

    def getOffsetVarDictVar(self, varID, scope):
        """
        Dada un varID, retorna el valor si existe en la tabla de variables.
        *@param: varID: el id de la variable a checar
        *@param: scope: el scope actual
        """
        for numeroTupla, valorTupla in self.dictVars.items():
            if((str(varID) == str(valorTupla[0])) and (str(scope) == valorTupla[2])):
                return valorTupla[4]  # retornamos el offset de la tabla

        return ""

    def AddNewVar_DictVar(self, varID="", varType="", methodID="", valor=0, offset=0):
        """
        Agrega una nueva tupla a la tabla de simbolos de la tabla de VARIABLES
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

    def varExistsRecursivo(self, nombre, scope, existe=False):
        """
        Revisa si una variable dada EXISTE en la tabla de simbolos de variables
        Si existe, retorna TRUE. Si no, retorna False, RECURSIVO
        *@param: nombre: la variable a verificar en la tabla de simbolos
        *@param: scope: el scope de la variable, ya que podemos tener dos distintas
        *@param: existe: si existe
        """
        if(existe):
            return True
        if(len(self.dictVars) > 0):
            for i in range(len(self.dictVars)):
                valor = self.dictVars[i]
                if(nombre == valor[0] and scope == valor[2]):
                    existe = True
            if self.checkMethodInMethodSymbolTableV2(scope) and existe == False:
                nuevoScope = self.getPadreMethodDictMethods(scope)
                if(nuevoScope != ''):
                    return self.varExistsRecursivo(nombre, nuevoScope)
        return existe

    def getVarInformationRecursivo(self, nombre, scope, existe=False, var=""):
        """
        Revisa si una variable dada EXISTE en la tabla de simbolos de variables
        Si existe, retorna TRUE. Si no, retorna False, RECURSIVO
        *@param: nombre: la variable a verificar en la tabla de simbolos
        *@param: scope: el scope de la variable, ya que podemos tener dos distintas
        *@param: existe: si existe
        *@param: var: los valores de retorno
        """
        if(existe):
            return var
        if(len(self.dictVars) > 0):
            for i in range(len(self.dictVars)):
                valor = self.dictVars[i]
                if(nombre == valor[0] and scope == valor[2]):
                    existe = True
                    var = valor
            if self.checkMethodInMethodSymbolTableV2(scope) and existe == False:
                nuevoScope = self.getPadreMethodDictMethods(scope)
                if(nuevoScope != ''):
                    return self.getVarInformationRecursivo(nombre, nuevoScope)
        return var
        # ! ------------------------- METODOS DE DICCIONARIO DE METODOS ---------

    def getDictMethod(self):
        """
        Retorna el diccionario de métodos
        """
        return self.dictMethods

    def checkMethodInMethodSymbolTableV2(self, methodName):
        """
        Revisa si un método existe en la tabla de métodos,sino retonar FALSE. Sino TRUe
        *@param: methodName: el nombre del método
        """
        existsMethod = False
        for numeroTupla, valorTupla in self.dictMethods.items():
            if(str(methodName) == str(valorTupla[1])):
                existsMethod = True

        if((existsMethod == True)):
            return True
        else:
            return False

    def AddNewMethod_DictMethod(self, methodType="", methodName="", parametros=[], returnValue=False, padre=""):
        """
        Agrega una nueva tupla a la tabla de simbolos de la tabla de METODOS
        *@param: methodType: el tipo de método, como void
        *@param: methodName: el nombre del método -> como main
        *@param: parametros: un array con sus parámetros
        *@param: returnValue: el valor que planea retornar o el tipo, sino vacío
        *@param: padre: el padre del método
        """
        existsEntry = self.checkMethodInMethodSymbolTableV2(methodName)
        # colocamos en el orden especificado
        arraynuevo = [methodType, methodName, parametros, returnValue, padre]
        # si la entrada NO existe
        if(existsEntry == False):
            # agregamos una nueva entrada al diccionario
            self.dictMethods[self.contadorGlobalDictMethods] = arraynuevo
            self.contadorGlobalDictMethods += 1
        else:
            print("Error a nivel de tabla de simbolos. La entrada del método ya existe.")

    def getTypeMethodDictMethods(self, methodName):
        """
        Retorna el tipo de método
        *@param: methodName: el nombre del método
        """
        for numeroTupla, valorTupla in self.dictMethods.items():
            if(str(methodName) == str(valorTupla[1])):
                return valorTupla[0]

        return ""

    def getPadreMethodDictMethods(self, methodName):
        """
        Retorna el padre del método
        *@param: methodName: el nombre del método
        """
        for numeroTupla, valorTupla in self.dictMethods.items():
            if(str(methodName) == str(valorTupla[1])):
                return valorTupla[4]

        return ""

    def getParametersDictMethods(self, methodName):
        """
        Retorna los parámetros del método mandado
        *@param: methodName: el nombre del método
        """
        for numeroTupla, valorTupla in self.dictMethods.items():
            if(str(methodName) == str(valorTupla[1])):
                return valorTupla[2]

        return []

    def getParametersTypeDictMethods(self, methodName):
        """
        Retorna los parámetros del método mandado
        *@param: methodName: el nombre del método
        """
        parametros = []
        arrayTipos = []
        for numeroTupla, valorTupla in self.dictMethods.items():
            if(str(methodName) == str(valorTupla[1])):
                parametros = valorTupla[2]

        tipoVariable = ""
        for x in parametros:
            tipoVariable = self.getTypeVarDictVar(x, methodName)
            arrayTipos.append(tipoVariable)

        return arrayTipos

    def getReturnDictMethods(self, methodName):
        """
        Retorna el tipo de return de un metodo
        *@param: methodName: el nombre del método
        """
        for numeroTupla, valorTupla in self.dictMethods.items():
            if(str(methodName) == str(valorTupla[1])):
                return valorTupla[3]

        return False

    # ! ------------------------- METODOS DE DICCIONARIO DE ESTRUCTURAS ---------
    def getDictStruct(self):
        """
        Retorna el diccionario de estructuras
        """
        return self.dictStructs

    def checkStructInStructSymbolTableV2(self, structName):
        """
        Revisa si una estructura existe en la tabla de structs,
        sino retonar FALSE. Sino True
        *@param: structName: el nombre de la estructura
        """
        existsStruct = False
        for numeroTupla, valorTupla in self.dictStructs.items():
            if(str(structName) == str(valorTupla[0])):
                existsStruct = True

        if((existsStruct == True)):
            return True
        else:
            return False

    def getStructInformation(self, structName):
        """
        Retorna la tupla de una estructura
        *@param: structName: el nombre de la estructura
        """
        existsStruct = []
        for numeroTupla, valorTupla in self.dictStructs.items():
            if(str(structName) == str(valorTupla[0])):
                existsStruct = valorTupla

        return existsStruct

    def AddNewStruct_DictStruct(self, structName="", structType="", scopePadre=""):
        """
        Agrega una nueva tupla a la tabla de simbolos de la tabla de ESTRUCTURAS
        *@param: structName: el nombre de la estructura
        *@param: structType: el tipo de la estructura SI tiene
        *@param: scopePadre: el scope padre
        """
        existsEntry = self.checkStructInStructSymbolTableV2(structName)
        # colocamos en el orden especificado
        arraynuevo = [structName, structType, scopePadre]
        # si la entrada NO existe
        if(existsEntry == False):
            # agregamos una nueva entrada al diccionario
            self.dictStructs[self.contadorGlobalDictStructs] = arraynuevo
            self.contadorGlobalDictStructs += 1
        else:
            print(
                "Error a nivel de tabla de simbolos. La entrada de la struct ya existe.")
