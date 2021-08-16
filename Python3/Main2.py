from antlr4 import *
from antlr4.tree.Trees import TerminalNode
from decafAlejandroLexer import decafAlejandroLexer
from decafAlejandroListener import decafAlejandroListener
from decafAlejandroParser import decafAlejandroParser
from nltk import Tree
from antlr4.tree.Trees import Trees
import sys


class KeyPrinter(decafAlejandroListener):
    def exitKey(self, ctx):
        print("Hola: %s" % ctx.ID())


def traverse(tree, rule_names, indent=0):
    if tree.getText() == "<EOF>":
        return
    elif isinstance(tree, TerminalNode):
        print("{0}T='{1}'".format("  " * indent, tree.getText()))
    else:
        print("{0}R='{1}'".format("  " * indent,
                                  rule_names[tree.getRuleIndex()]))
        if (tree.children != None):
            for child in tree.children:
                traverse(child, rule_names, indent + 1)


def main():
    print("Imprimiendo el árbol..................")
    data = open('Python3/programs/test.txt').read()
    lexer = decafAlejandroLexer(InputStream(data))
    stream = CommonTokenStream(lexer)
    parser = decafAlejandroParser(stream)
    tree = parser.program()

    printer = KeyPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    traverse(tree, parser.ruleNames)
    #print(Trees.toStringTree(tree, None, parser))
    # print(Trees.getChildren(tree))
    listaHijos = Trees.getChildren(tree)
    print(listaHijos)


if __name__ == '__main__':
    main()
