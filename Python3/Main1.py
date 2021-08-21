from antlr4 import *
from antlr4.tree.Trees import TerminalNode
from decafAlejandroLexer import decafAlejandroLexer
from decafAlejandroListener import decafAlejandroListener
from decafAlejandroParser import decafAlejandroParser
import sys


class DecafPrinter(decafAlejandroListener):
    def _init_(self) -> None:
        super()._init_()
        self.notMainName = True

    '''
    Antlr te crea distintos parametros, por ejemplo este
    enter[nombre de regla de tu gramatica]
    '''

    def enterMethodDeclaration(self, ctx: decafAlejandroParser.MethodDeclarationContext):

        #print("-----------ENTER ---------------")
        tipo = ctx.methodType().getText()
        nombre = ctx.ID().getText()
        parametro = ctx.parameter()
        conteo = ctx.getChildCount()
        #print(tipo, " ", nombre, " ", parametro, " ", conteo, " ")
        # print("-----------ENTER---------------")
        """ for x in range(0, conteo):
            print(ctx.getChild(x).getText())
        print("---------------") """

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
        #print("-----------EXIT ---------------")
        tipo = ctx.methodType().getText()
        nombre = ctx.ID().getText()
        parametro = ctx.parameter()
        conteo = ctx.getChildCount()
        #print(tipo, " ", nombre, " ", parametro, " ", conteo, " ")
        #print("----------- FIN EXIT ---------------")

    """ def visitTerminal(self, node: TerminalNode):
        print(node.getText())
        if(node == "void" and (node+1) == "main" and (node+2) == "(" and (node+3) == ")"):
            print("YAY regla cumplida") """


def main():
    data = open('Python3/programs/simple.decaf').read()
    lexer = decafAlejandroLexer(InputStream(data))
    stream = CommonTokenStream(lexer)
    parser = decafAlejandroParser(stream)
    tree = parser.program()

    printer = DecafPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


main()
