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
from antlr4 import *
from antlr4.tree.Trees import TerminalNode
from funciones import *
from ErrorClass import *
from symbolTable import *
import sys


class decafAlejandroPrinter(decafAlejandroListener):
    """
    Clase encargada de los métodos generados por ANTLR
    """

    def __init__(self) -> None:
        self.functions = funciones()  # funciones necesarias y varias
        self.tablaSimbolos = symbolTables()

    def enterVardeclr(self, ctx: decafAlejandroParser.VardeclrContext):
        return super().enterVardeclr(ctx)

    def enterArray_id(self, ctx: decafAlejandroParser.Array_idContext):
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
                    f'La variable {oldArrayValue} no ha sido declarada e intenta usarse en la declaración de un array en la linea:{line} columna:{column} ')
                exit()

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
    # invocamos al arbol
    tree = parser.program()
    # ? invocamos al printer, este printer es nuestra CLASE declarada arriba
    printer = decafAlejandroPrinter()
    # el walker camina
    walker = ParseTreeWalker()
    # l eindicamos al walker que avance en el arbol con el priner
    walker.walk(printer, tree)


main()
