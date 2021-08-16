from antlr4 import *
from antlr4.tree.Trees import TerminalNode
from decafAlejandroLexer import decafAlejandroLexer
from decafAlejandroListener import decafAlejandroListener
from decafAlejandroParser import decafAlejandroParser
import sys


'''
Clase que vos creas que hereda del Listener que antlr te crea
Los nombres pueden cambiar en todo el ejemplo, depende de tu gramatica
'''


class DecafPrinter(decafAlejandroListener):
    def _init_(self) -> None:
        super()._init_()

    '''
    Antlr te crea distintos parametros, por ejemplo este
    enter[nombre de regla de tu gramatica]
    '''

    def enterMethodDeclaration(self, ctx: decafAlejandroParser.MethodDeclarationContext):
        '''
            ctx es el contexto de ese nodo, tambien tien un monton de funciones. Por ejemplo,
            te crea un metodo por cada posible nodo hijo de tu regla, ese te devuelve el nodo
        '''
        tipo = ctx.methodType().getText()
        nombre = ctx.ID().getText()
        print(nombre)

    def enterStructDeclaration(self, ctx: decafAlejandroParser.StructDeclarationContext):
        variable2 = ctx.depth()
        conteoHijos = ctx.getChildCount()

    def visitTerminal(self, node: TerminalNode):
        # $print(node)
        return super().visitTerminal(node)

    def enterEveryRule(self, ctx: ParserRuleContext):

        print(ctx.getText())


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
