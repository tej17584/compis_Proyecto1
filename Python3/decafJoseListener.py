# Generated from decafJose.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .decafJoseParser import decafJoseParser
else:
    from decafJoseParser import decafJoseParser

# This class defines a complete listener for a parse tree produced by decafJoseParser.
class decafJoseListener(ParseTreeListener):

    # Enter a parse tree produced by decafJoseParser#start.
    def enterStart(self, ctx:decafJoseParser.StartContext):
        pass

    # Exit a parse tree produced by decafJoseParser#start.
    def exitStart(self, ctx:decafJoseParser.StartContext):
        pass


    # Enter a parse tree produced by decafJoseParser#id_tok.
    def enterId_tok(self, ctx:decafJoseParser.Id_tokContext):
        pass

    # Exit a parse tree produced by decafJoseParser#id_tok.
    def exitId_tok(self, ctx:decafJoseParser.Id_tokContext):
        pass


    # Enter a parse tree produced by decafJoseParser#declaration.
    def enterDeclaration(self, ctx:decafJoseParser.DeclarationContext):
        pass

    # Exit a parse tree produced by decafJoseParser#declaration.
    def exitDeclaration(self, ctx:decafJoseParser.DeclarationContext):
        pass


    # Enter a parse tree produced by decafJoseParser#varDeclaration.
    def enterVarDeclaration(self, ctx:decafJoseParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by decafJoseParser#varDeclaration.
    def exitVarDeclaration(self, ctx:decafJoseParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by decafJoseParser#structDeclaration.
    def enterStructDeclaration(self, ctx:decafJoseParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by decafJoseParser#structDeclaration.
    def exitStructDeclaration(self, ctx:decafJoseParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by decafJoseParser#varType.
    def enterVarType(self, ctx:decafJoseParser.VarTypeContext):
        pass

    # Exit a parse tree produced by decafJoseParser#varType.
    def exitVarType(self, ctx:decafJoseParser.VarTypeContext):
        pass


    # Enter a parse tree produced by decafJoseParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:decafJoseParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by decafJoseParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:decafJoseParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by decafJoseParser#methodType.
    def enterMethodType(self, ctx:decafJoseParser.MethodTypeContext):
        pass

    # Exit a parse tree produced by decafJoseParser#methodType.
    def exitMethodType(self, ctx:decafJoseParser.MethodTypeContext):
        pass


    # Enter a parse tree produced by decafJoseParser#parameter.
    def enterParameter(self, ctx:decafJoseParser.ParameterContext):
        pass

    # Exit a parse tree produced by decafJoseParser#parameter.
    def exitParameter(self, ctx:decafJoseParser.ParameterContext):
        pass


    # Enter a parse tree produced by decafJoseParser#parameterType.
    def enterParameterType(self, ctx:decafJoseParser.ParameterTypeContext):
        pass

    # Exit a parse tree produced by decafJoseParser#parameterType.
    def exitParameterType(self, ctx:decafJoseParser.ParameterTypeContext):
        pass


    # Enter a parse tree produced by decafJoseParser#block.
    def enterBlock(self, ctx:decafJoseParser.BlockContext):
        pass

    # Exit a parse tree produced by decafJoseParser#block.
    def exitBlock(self, ctx:decafJoseParser.BlockContext):
        pass


    # Enter a parse tree produced by decafJoseParser#statement.
    def enterStatement(self, ctx:decafJoseParser.StatementContext):
        pass

    # Exit a parse tree produced by decafJoseParser#statement.
    def exitStatement(self, ctx:decafJoseParser.StatementContext):
        pass


    # Enter a parse tree produced by decafJoseParser#location.
    def enterLocation(self, ctx:decafJoseParser.LocationContext):
        pass

    # Exit a parse tree produced by decafJoseParser#location.
    def exitLocation(self, ctx:decafJoseParser.LocationContext):
        pass


    # Enter a parse tree produced by decafJoseParser#expression.
    def enterExpression(self, ctx:decafJoseParser.ExpressionContext):
        pass

    # Exit a parse tree produced by decafJoseParser#expression.
    def exitExpression(self, ctx:decafJoseParser.ExpressionContext):
        pass


    # Enter a parse tree produced by decafJoseParser#methodCall.
    def enterMethodCall(self, ctx:decafJoseParser.MethodCallContext):
        pass

    # Exit a parse tree produced by decafJoseParser#methodCall.
    def exitMethodCall(self, ctx:decafJoseParser.MethodCallContext):
        pass


    # Enter a parse tree produced by decafJoseParser#arg.
    def enterArg(self, ctx:decafJoseParser.ArgContext):
        pass

    # Exit a parse tree produced by decafJoseParser#arg.
    def exitArg(self, ctx:decafJoseParser.ArgContext):
        pass


    # Enter a parse tree produced by decafJoseParser#op.
    def enterOp(self, ctx:decafJoseParser.OpContext):
        pass

    # Exit a parse tree produced by decafJoseParser#op.
    def exitOp(self, ctx:decafJoseParser.OpContext):
        pass


    # Enter a parse tree produced by decafJoseParser#arith_op.
    def enterArith_op(self, ctx:decafJoseParser.Arith_opContext):
        pass

    # Exit a parse tree produced by decafJoseParser#arith_op.
    def exitArith_op(self, ctx:decafJoseParser.Arith_opContext):
        pass


    # Enter a parse tree produced by decafJoseParser#rel_op.
    def enterRel_op(self, ctx:decafJoseParser.Rel_opContext):
        pass

    # Exit a parse tree produced by decafJoseParser#rel_op.
    def exitRel_op(self, ctx:decafJoseParser.Rel_opContext):
        pass


    # Enter a parse tree produced by decafJoseParser#eq_op.
    def enterEq_op(self, ctx:decafJoseParser.Eq_opContext):
        pass

    # Exit a parse tree produced by decafJoseParser#eq_op.
    def exitEq_op(self, ctx:decafJoseParser.Eq_opContext):
        pass


    # Enter a parse tree produced by decafJoseParser#cond_op.
    def enterCond_op(self, ctx:decafJoseParser.Cond_opContext):
        pass

    # Exit a parse tree produced by decafJoseParser#cond_op.
    def exitCond_op(self, ctx:decafJoseParser.Cond_opContext):
        pass


    # Enter a parse tree produced by decafJoseParser#literal.
    def enterLiteral(self, ctx:decafJoseParser.LiteralContext):
        pass

    # Exit a parse tree produced by decafJoseParser#literal.
    def exitLiteral(self, ctx:decafJoseParser.LiteralContext):
        pass


    # Enter a parse tree produced by decafJoseParser#int_literal.
    def enterInt_literal(self, ctx:decafJoseParser.Int_literalContext):
        pass

    # Exit a parse tree produced by decafJoseParser#int_literal.
    def exitInt_literal(self, ctx:decafJoseParser.Int_literalContext):
        pass


    # Enter a parse tree produced by decafJoseParser#char_literal.
    def enterChar_literal(self, ctx:decafJoseParser.Char_literalContext):
        pass

    # Exit a parse tree produced by decafJoseParser#char_literal.
    def exitChar_literal(self, ctx:decafJoseParser.Char_literalContext):
        pass


    # Enter a parse tree produced by decafJoseParser#bool_literal.
    def enterBool_literal(self, ctx:decafJoseParser.Bool_literalContext):
        pass

    # Exit a parse tree produced by decafJoseParser#bool_literal.
    def exitBool_literal(self, ctx:decafJoseParser.Bool_literalContext):
        pass



del decafJoseParser