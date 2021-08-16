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
    enter[nombre de relga de tu gramatica]
    '''

    def enterMethodDeclaration(self, ctx: decafAlejandroParser.MethodDeclarationContext):
        '''
            ctx es el contexto de ese nodo, tambien tien un monton de funciones. Por ejemplo,
            te crea un metodo por cada posible nodo hijo de tu regla, ese te devuelve el nodo
        '''
        tipo = ctx.methodType().getText()
        nombre = ctx.id_tok().getText()


def main():
    data = open('antlr/Python3/programs/test.txt').read()
    lexer = decafAlejandroLexer(InputStream(data))
    stream = CommonTokenStream(lexer)
    parser = decafAlejandroParser(stream)
    tree = parser.program()

    printer = DecafPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


main()
