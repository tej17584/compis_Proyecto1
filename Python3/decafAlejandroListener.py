# Generated from decafAlejandro.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .decafAlejandroParser import decafAlejandroParser
else:
    from decafAlejandroParser import decafAlejandroParser

# This class defines a complete listener for a parse tree produced by decafAlejandroParser.
class decafAlejandroListener(ParseTreeListener):

    # Enter a parse tree produced by decafAlejandroParser#program.
    def enterProgram(self, ctx:decafAlejandroParser.ProgramContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#program.
    def exitProgram(self, ctx:decafAlejandroParser.ProgramContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#declaration.
    def enterDeclaration(self, ctx:decafAlejandroParser.DeclarationContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#declaration.
    def exitDeclaration(self, ctx:decafAlejandroParser.DeclarationContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#varDeclaration.
    def enterVarDeclaration(self, ctx:decafAlejandroParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#varDeclaration.
    def exitVarDeclaration(self, ctx:decafAlejandroParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#structDeclaration.
    def enterStructDeclaration(self, ctx:decafAlejandroParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#structDeclaration.
    def exitStructDeclaration(self, ctx:decafAlejandroParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#varType.
    def enterVarType(self, ctx:decafAlejandroParser.VarTypeContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#varType.
    def exitVarType(self, ctx:decafAlejandroParser.VarTypeContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:decafAlejandroParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:decafAlejandroParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#methodType.
    def enterMethodType(self, ctx:decafAlejandroParser.MethodTypeContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#methodType.
    def exitMethodType(self, ctx:decafAlejandroParser.MethodTypeContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#parameter.
    def enterParameter(self, ctx:decafAlejandroParser.ParameterContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#parameter.
    def exitParameter(self, ctx:decafAlejandroParser.ParameterContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#parameterType.
    def enterParameterType(self, ctx:decafAlejandroParser.ParameterTypeContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#parameterType.
    def exitParameterType(self, ctx:decafAlejandroParser.ParameterTypeContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#block.
    def enterBlock(self, ctx:decafAlejandroParser.BlockContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#block.
    def exitBlock(self, ctx:decafAlejandroParser.BlockContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#statement.
    def enterStatement(self, ctx:decafAlejandroParser.StatementContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#statement.
    def exitStatement(self, ctx:decafAlejandroParser.StatementContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#location.
    def enterLocation(self, ctx:decafAlejandroParser.LocationContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#location.
    def exitLocation(self, ctx:decafAlejandroParser.LocationContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#expression.
    def enterExpression(self, ctx:decafAlejandroParser.ExpressionContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#expression.
    def exitExpression(self, ctx:decafAlejandroParser.ExpressionContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#methodCall.
    def enterMethodCall(self, ctx:decafAlejandroParser.MethodCallContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#methodCall.
    def exitMethodCall(self, ctx:decafAlejandroParser.MethodCallContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#arg.
    def enterArg(self, ctx:decafAlejandroParser.ArgContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#arg.
    def exitArg(self, ctx:decafAlejandroParser.ArgContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#op.
    def enterOp(self, ctx:decafAlejandroParser.OpContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#op.
    def exitOp(self, ctx:decafAlejandroParser.OpContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#arith_op.
    def enterArith_op(self, ctx:decafAlejandroParser.Arith_opContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#arith_op.
    def exitArith_op(self, ctx:decafAlejandroParser.Arith_opContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#rel_op.
    def enterRel_op(self, ctx:decafAlejandroParser.Rel_opContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#rel_op.
    def exitRel_op(self, ctx:decafAlejandroParser.Rel_opContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#eq_op.
    def enterEq_op(self, ctx:decafAlejandroParser.Eq_opContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#eq_op.
    def exitEq_op(self, ctx:decafAlejandroParser.Eq_opContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#cond_op.
    def enterCond_op(self, ctx:decafAlejandroParser.Cond_opContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#cond_op.
    def exitCond_op(self, ctx:decafAlejandroParser.Cond_opContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#literal.
    def enterLiteral(self, ctx:decafAlejandroParser.LiteralContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#literal.
    def exitLiteral(self, ctx:decafAlejandroParser.LiteralContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#int_literal.
    def enterInt_literal(self, ctx:decafAlejandroParser.Int_literalContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#int_literal.
    def exitInt_literal(self, ctx:decafAlejandroParser.Int_literalContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#char_literal.
    def enterChar_literal(self, ctx:decafAlejandroParser.Char_literalContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#char_literal.
    def exitChar_literal(self, ctx:decafAlejandroParser.Char_literalContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#bool_literal.
    def enterBool_literal(self, ctx:decafAlejandroParser.Bool_literalContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#bool_literal.
    def exitBool_literal(self, ctx:decafAlejandroParser.Bool_literalContext):
        pass



del decafAlejandroParser