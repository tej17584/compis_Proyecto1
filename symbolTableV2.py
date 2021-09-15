"""
Nombre: Alejandro Tejada
Curso: Diseño Compiladores
Fecha: agosto 2021
Programa: tablaSimbolosv2.py
Propósito: Este programa alojará 3 clases para cada tabla. Este es una nueva version del codigo
de las tablas de símbolos.
V 2.0
"""
# zona de imports
from prettytable import PrettyTable
from antlr4.tree.Tree import Tree
from funciones import *
import sys
import json


class generalSymbolTable():
    def __init__(self):
        """
        Init de los métodos de la tabla de simbolos
        """
        self.dictSimbolos = []  # diccionario para los simbolos
        self.offsetVariables = 0  # ofsset de variables y de valores
        self.pretty_table = PrettyTable()  # instancia de pretty table

        print(' -- INICIANDO NUEVO AMBITO --')

    def AddEntryToTable(self, typeValue, idValue, size, offset, isParameter):
        """
        Agrega un valor a la tabla de simbolos general
        *@param: typeValue: el tipo de valor
        *@param: scope: el valor del id
        *@param: size: el size de ese valor
        *@param: offset: el offset de ese valor
        *@param: isParameter: bool para el parametro
        """
        self.dictSimbolos.append({
            'Tipo': typeValue,
            'Id': idValue,
            'Size': size,
            'Offset': offset,
            'IsParameter': isParameter
        })
        self.offsetVariables += size

    def LookUp(self, variable):
        symbols_copy = self.dictSimbolos.copy()
        symbols_copy.reverse()
        for symbol in symbols_copy:
            if symbol['Id'] == variable:
                return symbol

        return 0

    def GetSize(self):
        return sum(symbol['Size'] for symbol in self.dictSimbolos)

    def ToTable(self):
        self.pretty_table.field_names = [
            'Tipo', 'ID', 'Size', 'Offset', 'IsParameter']
        for i in self.dictSimbolos:
            self.pretty_table.add_row(list(i.values()))

        print(' ** SIMBOLOS **')
        print(self.pretty_table)
        self.pretty_table.clear_rows()


class tableDictParameters():
    def __init__(self):
        self.pretty_table = PrettyTable()
        self.dictSimbolos = []
        print(' -- INICIANDO NUEVO AMBITO --')

    def AddEntryToTable(self, typeValue, idValue):
        self.dictSimbolos.append({
            'Tipo': typeValue,
            'Id': idValue,
        })

    def LookUp(self, variable):
        symbols_copy = self.dictSimbolos.copy()
        symbols_copy.reverse()
        for symbol in symbols_copy:
            if symbol['Id'] == variable:
                return symbol
        return 0

    def ToTable(self):
        self.pretty_table.field_names = ['Tipo', 'ID']
        for i in self.dictSimbolos:
            self.pretty_table.add_row(list(i.values()))

        print(' ** PARAMETERS **')
        print(self.pretty_table)
        self.pretty_table.clear_rows()

    def Clear(self):
        self.ToTable()
        self.dictSimbolos = []


class dictTableStruct():
    def __init__(self):
        self.pretty_table = PrettyTable()
        self.dictSimbolos = []

    def AddEntryToTable(self, parent, typeValue, idValue, description):
        self.dictSimbolos.append({
            'Parent': parent,
            'Tipo': typeValue,
            'Id': idValue,
            'Description': description
        })

    def LookUp(self, variable):
        symbols_copy = self.dictSimbolos.copy()
        symbols_copy.reverse()
        for symbol in symbols_copy:
            if symbol['Id'] == variable:
                return symbol
        return 0

    def ToTable(self):
        self.pretty_table.field_names = ['Parent', 'Tipo', 'ID', 'Description']
        for i in self.dictSimbolos:
            self.pretty_table.add_row(list(i.values()))

        print(' ** STRUCTS **')
        print(self.pretty_table)
        self.pretty_table.clear_rows()

    def ExtractInfo(self, parent, scope, tabla_tipo):
        for i in scope.dictSimbolos:
            typeValue = tabla_tipo.LookUp(i['Tipo'])
            self.AddEntryToTable(parent, i['Tipo'], i['Id'], typeValue['Description'])

    def GetChild(self, typeValue, name):
        copy_symbols = self.dictSimbolos.copy()
        copy_symbols.reverse()
        for symbol in copy_symbols:
            if symbol['Parent'] in typeValue and symbol['Id'] == name:
                return symbol

        return 0


class dictTableMetods():
    def __init__(self):
        self.pretty_table = PrettyTable()
        self._methods = []
        print(' -- INICIANDO NUEVO AMBITO --')

    def AddEntryToTable(self, typeValue, idValue, parameters, returnVariable):
        self._methods.append({
            'Tipo': typeValue,
            'Id': idValue,
            'Parameters': parameters,
            'Return': returnVariable
        })

    def LookUp(self, variable):
        for method in self._methods:
            if method['Id'] == variable:
                return method

        return 0

    def ToTable(self):
        self.pretty_table.field_names = ['Tipo', 'ID', 'Parameters', 'Return']
        for i in self._methods:
            self.pretty_table.add_row(list(i.values()))

        print(' ** METODOS **')
        print(self.pretty_table)
        self.pretty_table.clear_rows()


class dictTableVars():
    def __init__(self):
        self.PRIMITIVE = 'primitive'
        self.ARRAY = 'array'
        self.STRUCT = 'struct'

        self._types = []
        self.AddEntryToTable('int', 4, self.PRIMITIVE)
        self.AddEntryToTable('char', 2, self.PRIMITIVE)
        self.AddEntryToTable('boolean', 1, self.PRIMITIVE)
        self.AddEntryToTable('void', 0, self.PRIMITIVE)
        print(' -- INICIANDO TABLA TIPOS --')

    def AddEntryToTable(self, typeValue, size, description):
        self._types.append({
            'Tipo': typeValue,
            'Size': size,
            'Description': description
        })

    def LookUp(self, typeValue):
        types_copy = self._types.copy()
        types_copy.reverse()
        for type in types_copy:
            if type['Tipo'] == typeValue:
                return type
        return 0


class SemanticError():
    def __init__(self):
        self.errores = []
        self.IDENTIFICADOR_DECLARADO_MUCHAS_VECES = 'Identificador no puede estar declarado más de una vez en el mismo ámbito.'
        self.MAIN_PARAMETERLESS = 'No existe un método llamado main sin parámetros.'
        self.NUMERO_PARAMETROS_METODO = 'El número de argumentos en la llamada al método no coincide.'
        self.TIPO_PARAMETROS_METODO = 'El typeValue de dato en los argumentos en la llamada al método no coincide.'
        self.EQ_OPS = 'El typeValue de dato de operandos no es el mismo para los operadores "==" y "!=".'
        self.ARITH_OP = 'El typeValue de dato de operando debe ser INT para operadores aritméticos.'
        self.REL_OP = 'El typeValue de dato de operando debe ser INT para operadores de relación.'
        self.COND_OP = 'El typeValue de dato en operación condicional debe ser boolean.'
        self.IF_BOOLEAN = 'El typeValue de dato dentro de condición de IF debe ser boolean.'
        self.WHILE_BOOLEAN = 'El typeValue de dato dentro de condición de WHILE debe ser boolean.'
        self.ASIGNACION = 'La asignación de dos valores deben ser del mismo typeValue.'
        self.RETURN_TYPE = 'El valor de retorno debe de ser del mismo typeValue con que fue declarado el método.'
        self.RETURN_VOID = 'Un método declarado VOID no puede retornar ningún valor.'
        self.MUST_STRUCT = 'El typeValue de dato de la variable debe ser STRUCT.'
        self.METHOD_NOT_DECLARED = 'El método no existe o no hay definición del método previamente a ser invocado.'
        self.SHADOW_PARAMETER = 'No es posible declarar una variable con el nombre de un parámetro.'

    def AddEntryToTable(self, line, col, msg):
        self.errores.append({
            'Line': line,
            'Col': col,
            'Msg': msg
        })

    def ToString(self):
        for error in self.errores:
            print(' => Line ' + str(error['Line']) +
                  ':' + str(error['Col']) + ' ' + error['Msg'])

    def GetErrores(self):
        errors = []
        for error in self.errores:
            errors.append(
                ' => Line ' + str(error['Line']) + ':' + str(error['Col']) + ' ' + error['Msg'])
        return errors
