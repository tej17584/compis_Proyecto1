"""
Nombre: Alejandro Tejada
Curso: Diseño Compiladores
Fecha: Agosto 2021
Programa: main.py
Propósito: Este programa es el encargado de llamar al listener, printer, walker, etc de
ANTRL, tambien maneja algunas logicas
"""

# ZONA DE IMPORTS
from decafAlejandroLexer import decafAlejandroLexer
from decafAlejandroParser import decafAlejandroParser
from decafAlejandroListener import decafAlejandroListener
from antlr4.error.ErrorListener import ErrorListener
from antlr4 import *
from antlr4.tree.Trees import TerminalNode
from funciones import *
from ErrorClass import *
from symbolTable import *
import sys


class MyErrorListener(ErrorListener):
    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(str(line) + ":" + str(column) + ": sintaxis ERROR encontrado, " +
              str(msg))
        sys.exit()


class decafAlejandroPrinter(decafAlejandroListener):
    """
    Clase encargada de los métodos generados por ANTLR
    # primera vuelta
    """

    def __init__(self) -> None:
        self.functions = funciones()  # funciones necesarias y varias
        self.tablaSimbolos = symbolTables()
        self.scopeActual = "global"
        self.scopeAnterior = "global"

    def enterStatement(self, ctx: decafAlejandroParser.StatementContext):
        return super().enterStatement(ctx)

    def exitProgram(self, ctx: decafAlejandroParser.ProgramContext):
        diccionarioFinal = self.tablaSimbolos.getDictVar()
        print(diccionarioFinal)

    def enterStruct_declr(self, ctx: decafAlejandroParser.Struct_declrContext):
        # actualizamos el scope
        self.scopeAnterior = self.scopeActual
        self.scopeActual = ctx.ID().getText()

    def exitStruct_declr(self, ctx: decafAlejandroParser.Struct_declrContext):
        # actualizamos el scope cuando salimso de la funcion
        self.scopeActual = self.scopeAnterior

    def enterMethod_declr(self, ctx: decafAlejandroParser.Method_declrContext):
        # actualizamos el scope
        self.scopeAnterior = self.scopeActual
        self.scopeActual = ctx.method_name().getText()

    def exitMethod_declr(self, ctx: decafAlejandroParser.Method_declrContext):
        # actualizamos el scope cuando salimso de la funcion
        self.scopeActual = self.scopeAnterior

    def enterStatement(self, ctx: decafAlejandroParser.StatementContext):
        name = ctx.location().getText()  # el nombre de la variable
        valorAsignado = ctx.expr().getText()
        line = ctx.start.line
        column = ctx.start.column
        scope = self.scopeActual
        varExists = self.tablaSimbolos.checkVarInVarSymbolTableV2(
            name, scope)
        # verificamos si existe en el scope actual
        if(varExists):
            tipoGuardado = self.tablaSimbolos.getTypeVarDictVar(name)
            typeMatch = self.functions.checkGeneraltype(
                valorAsignado, tipoGuardado)
            if(typeMatch == False):
                print(
                    f'ERROR. La variable -> {name} <- está siendo asignada con el valor {valorAsignado} pero no son el mismo TIPO')
                exit()
            else:
                print("PRINT LOCAL")
        else:
            # si no existe en el scope actual, revismos en el global
            varExists2 = self.tablaSimbolos.checkVarInVarSymbolTableV2(
                name, "global")
            if(varExists2):
                # si existe en el global, verificamos que el tipo con el que fue guardado haga match
                tipoGuardado = self.tablaSimbolos.getTypeVarDictVar(name)
                typeMatch = self.functions.checkGeneraltype(
                    valorAsignado, tipoGuardado)
                if(typeMatch == False):
                    print(
                        f'ERROR. La variable {tipoGuardado} -> {name} <- está siendo asignada con el valor {valorAsignado} pero no son el mismo TIPO')
                    exit()
                else:
                    print("PRINT GLOBAL")

            elif(varExists2 == False):
                print(
                    f'ERROR. La variable -> {name} <- está siendo asignada con el valor {valorAsignado} ANTES de ser declarada')
                exit()

    def enterVardeclr(self, ctx: decafAlejandroParser.VardeclrContext):
        for x in range(len(ctx.field_var())):
            name = ctx.field_var()[x].getText()  # el nombre de la variable
            tipo = ctx.var_type()[x].getText()
            line = ctx.start.line
            column = ctx.start.column
            scope = self.scopeActual
            arrayValue = ""
            # condicion por si es un array
            if("[" in name and "]" in name):
                name = name[0]
                arrayValue = ctx.field_var()[x].array_id().expr().getText()

                if(self.functions.checkIfIsInt(arrayValue)):
                    # valor declarado dentro del array
                    arrayValue = int(arrayValue)
                    claseError = Errores(name, column, line, "")
                    hasError, errorValue = claseError.checkArrayError(
                        arrayValue, False)
                    if(hasError):
                        print(errorValue)
                        exit()
                else:
                    oldArrayValue = arrayValue
                    varExistsInner, arrayValue = self.tablaSimbolos.checkVarInVarSymbolTable(
                        arrayValue)
                    if(varExistsInner):
                        tipoDato = self.tablaSimbolos.getTypeVarDictVar(
                            oldArrayValue)
                        claseError = Errores(name, column, line, tipoDato)
                        hasError, errorValue = claseError.checkArrayError(
                            arrayValue, True)
                        if(hasError):
                            print(errorValue)
                            exit()
                    else:
                        print(
                            f'La variable {oldArrayValue} no ha sido declarada e intenta usarse en un array en la linea:{line} columna:{column} ')
                        exit()

            varExists = self.tablaSimbolos.checkVarInVarSymbolTableV2(
                name, scope)
            if(varExists == False):
                if("struct" in tipo):
                    tipo = tipo.replace("struct", "")
                self.tablaSimbolos.AddNewVar_DictVar(name, tipo, scope, 0, 0)
            elif(varExists == True):
                print(
                    f'Error, la variable {name} ya fue declarada en el scope {scope}. Linea: {line} columna: {column} ')
                exit()
            # ya tenemos las variables actuales
            # print(name, " ", column, " ", line, " ", tipo, " scope: ", scope)

    """ def enterArray_id(self, ctx: decafAlejandroParser.Array_idContext):
        name = ctx.ID().getText()  # el nombre del array
        column = ctx.start.column
        line = ctx.start.line
        # verificamos si lo que viene es un numero o letra
        arrayValue = ctx.expr().getText()
        if(self.functions.checkIfIsInt(arrayValue)):
            # valor declarado dentro del array
            arrayValue = int(arrayValue)
            claseError = Errores(name, column, line, "")
            hasError, errorValue = claseError.checkArrayError(
                arrayValue, False)
            if(hasError):
                print(errorValue)
                exit()
        else:
            oldArrayValue = arrayValue
            varExists, arrayValue = self.tablaSimbolos.checkVarInVarSymbolTable(
                arrayValue)
            if(varExists):
                tipoDato = self.tablaSimbolos.getTypeVarDictVar(oldArrayValue)
                claseError = Errores(name, column, line, tipoDato)
                hasError, errorValue = claseError.checkArrayError(
                    arrayValue, True)
                if(hasError):
                    print(errorValue)
                    exit()
            else:
                print(
                    f'La variable {oldArrayValue} no ha sido declarada e intenta usarse en un array en la linea:{line} columna:{column} ')
                exit() """

    """  def enterMethodDeclaration(self, ctx: decafAlejandroParser.MethodDeclarationContext):

        # print("-----------ENTER ---------------")
        tipo = ctx.methodType().getText()
        nombre = ctx.ID().getText()
        parametro = ctx.parameter()
        conteo = ctx.getChildCount()
        # print(tipo, " ", nombre, " ", parametro, " ", conteo, " ")
        # print("-----------ENTER---------------")
        for x in range(0, conteo):
            print(ctx.getChild(x).getText())
        print("---------------")

    def enterStructDeclaration(self, ctx: decafAlejandroParser.StructDeclarationContext):
        variable2 = ctx.depth()
        conteoHijos = ctx.getChildCount()

    def enterVarDeclaration(self, ctx: decafAlejandroParser.VarDeclarationContext):
        name = ctx.ID().getText()
        column = ctx.start.column
        line = ctx.start.line
        type = ctx.varType().getText()
        error = "ERRORAZO"
        print(name, " ", column, " ", line, " ", type, " ", error, "")

    def exitMethodDeclaration(self, ctx: decafAlejandroParser.MethodDeclarationContext):
        # print("-----------EXIT ---------------")
        tipo = ctx.methodType().getText()
        nombre = ctx.ID().getText()
        parametro = ctx.parameter()
        conteo = ctx.getChildCount()
        # print(tipo, " ", nombre, " ", parametro, " ", conteo, " ")
        # print("----------- FIN EXIT ---------------") """


def main():
    # hacemos el open de la data del archivo de prueba
    data = open('Python3/programs/simple.decaf').read()
    # invocamos al lexer
    lexer = decafAlejandroLexer(InputStream(data))
    # jalamos el stream
    stream = CommonTokenStream(lexer)
    # invocamos al parser
    parser = decafAlejandroParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener())
    # invocamos al arbol
    tree = parser.program()
    # ? invocamos al printer, este printer es nuestra CLASE declarada arriba
    printer = decafAlejandroPrinter()
    # el walker camina
    walker = ParseTreeWalker()
    # l eindicamos al walker que avance en el arbol con el priner
    walker.walk(printer, tree)


main()
