# Generated from decafJavier.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .decafJavierParser import decafJavierParser
else:
    from decafJavierParser import decafJavierParser

# This class defines a complete listener for a parse tree produced by decafJavierParser.
class decafJavierListener(ParseTreeListener):

    # Enter a parse tree produced by decafJavierParser#program.
    def enterProgram(self, ctx:decafJavierParser.ProgramContext):
        pass

    # Exit a parse tree produced by decafJavierParser#program.
    def exitProgram(self, ctx:decafJavierParser.ProgramContext):
        pass


    # Enter a parse tree produced by decafJavierParser#vardeclr.
    def enterVardeclr(self, ctx:decafJavierParser.VardeclrContext):
        pass

    # Exit a parse tree produced by decafJavierParser#vardeclr.
    def exitVardeclr(self, ctx:decafJavierParser.VardeclrContext):
        pass


    # Enter a parse tree produced by decafJavierParser#field_declr.
    def enterField_declr(self, ctx:decafJavierParser.Field_declrContext):
        pass

    # Exit a parse tree produced by decafJavierParser#field_declr.
    def exitField_declr(self, ctx:decafJavierParser.Field_declrContext):
        pass


    # Enter a parse tree produced by decafJavierParser#array_id.
    def enterArray_id(self, ctx:decafJavierParser.Array_idContext):
        pass

    # Exit a parse tree produced by decafJavierParser#array_id.
    def exitArray_id(self, ctx:decafJavierParser.Array_idContext):
        pass


    # Enter a parse tree produced by decafJavierParser#field_var.
    def enterField_var(self, ctx:decafJavierParser.Field_varContext):
        pass

    # Exit a parse tree produced by decafJavierParser#field_var.
    def exitField_var(self, ctx:decafJavierParser.Field_varContext):
        pass


    # Enter a parse tree produced by decafJavierParser#var_id.
    def enterVar_id(self, ctx:decafJavierParser.Var_idContext):
        pass

    # Exit a parse tree produced by decafJavierParser#var_id.
    def exitVar_id(self, ctx:decafJavierParser.Var_idContext):
        pass


    # Enter a parse tree produced by decafJavierParser#method_declr.
    def enterMethod_declr(self, ctx:decafJavierParser.Method_declrContext):
        pass

    # Exit a parse tree produced by decafJavierParser#method_declr.
    def exitMethod_declr(self, ctx:decafJavierParser.Method_declrContext):
        pass


    # Enter a parse tree produced by decafJavierParser#return_type.
    def enterReturn_type(self, ctx:decafJavierParser.Return_typeContext):
        pass

    # Exit a parse tree produced by decafJavierParser#return_type.
    def exitReturn_type(self, ctx:decafJavierParser.Return_typeContext):
        pass


    # Enter a parse tree produced by decafJavierParser#block.
    def enterBlock(self, ctx:decafJavierParser.BlockContext):
        pass

    # Exit a parse tree produced by decafJavierParser#block.
    def exitBlock(self, ctx:decafJavierParser.BlockContext):
        pass


    # Enter a parse tree produced by decafJavierParser#statement.
    def enterStatement(self, ctx:decafJavierParser.StatementContext):
        pass

    # Exit a parse tree produced by decafJavierParser#statement.
    def exitStatement(self, ctx:decafJavierParser.StatementContext):
        pass


    # Enter a parse tree produced by decafJavierParser#method_call_inter.
    def enterMethod_call_inter(self, ctx:decafJavierParser.Method_call_interContext):
        pass

    # Exit a parse tree produced by decafJavierParser#method_call_inter.
    def exitMethod_call_inter(self, ctx:decafJavierParser.Method_call_interContext):
        pass


    # Enter a parse tree produced by decafJavierParser#method_call.
    def enterMethod_call(self, ctx:decafJavierParser.Method_callContext):
        pass

    # Exit a parse tree produced by decafJavierParser#method_call.
    def exitMethod_call(self, ctx:decafJavierParser.Method_callContext):
        pass


    # Enter a parse tree produced by decafJavierParser#expr.
    def enterExpr(self, ctx:decafJavierParser.ExprContext):
        pass

    # Exit a parse tree produced by decafJavierParser#expr.
    def exitExpr(self, ctx:decafJavierParser.ExprContext):
        pass


    # Enter a parse tree produced by decafJavierParser#location.
    def enterLocation(self, ctx:decafJavierParser.LocationContext):
        pass

    # Exit a parse tree produced by decafJavierParser#location.
    def exitLocation(self, ctx:decafJavierParser.LocationContext):
        pass


    # Enter a parse tree produced by decafJavierParser#callout_arg.
    def enterCallout_arg(self, ctx:decafJavierParser.Callout_argContext):
        pass

    # Exit a parse tree produced by decafJavierParser#callout_arg.
    def exitCallout_arg(self, ctx:decafJavierParser.Callout_argContext):
        pass


    # Enter a parse tree produced by decafJavierParser#int_literal.
    def enterInt_literal(self, ctx:decafJavierParser.Int_literalContext):
        pass

    # Exit a parse tree produced by decafJavierParser#int_literal.
    def exitInt_literal(self, ctx:decafJavierParser.Int_literalContext):
        pass


    # Enter a parse tree produced by decafJavierParser#rel_op.
    def enterRel_op(self, ctx:decafJavierParser.Rel_opContext):
        pass

    # Exit a parse tree produced by decafJavierParser#rel_op.
    def exitRel_op(self, ctx:decafJavierParser.Rel_opContext):
        pass


    # Enter a parse tree produced by decafJavierParser#eq_op.
    def enterEq_op(self, ctx:decafJavierParser.Eq_opContext):
        pass

    # Exit a parse tree produced by decafJavierParser#eq_op.
    def exitEq_op(self, ctx:decafJavierParser.Eq_opContext):
        pass


    # Enter a parse tree produced by decafJavierParser#cond_op.
    def enterCond_op(self, ctx:decafJavierParser.Cond_opContext):
        pass

    # Exit a parse tree produced by decafJavierParser#cond_op.
    def exitCond_op(self, ctx:decafJavierParser.Cond_opContext):
        pass


    # Enter a parse tree produced by decafJavierParser#literal.
    def enterLiteral(self, ctx:decafJavierParser.LiteralContext):
        pass

    # Exit a parse tree produced by decafJavierParser#literal.
    def exitLiteral(self, ctx:decafJavierParser.LiteralContext):
        pass


    # Enter a parse tree produced by decafJavierParser#bin_op.
    def enterBin_op(self, ctx:decafJavierParser.Bin_opContext):
        pass

    # Exit a parse tree produced by decafJavierParser#bin_op.
    def exitBin_op(self, ctx:decafJavierParser.Bin_opContext):
        pass


    # Enter a parse tree produced by decafJavierParser#arith_op.
    def enterArith_op(self, ctx:decafJavierParser.Arith_opContext):
        pass

    # Exit a parse tree produced by decafJavierParser#arith_op.
    def exitArith_op(self, ctx:decafJavierParser.Arith_opContext):
        pass


    # Enter a parse tree produced by decafJavierParser#var_type.
    def enterVar_type(self, ctx:decafJavierParser.Var_typeContext):
        pass

    # Exit a parse tree produced by decafJavierParser#var_type.
    def exitVar_type(self, ctx:decafJavierParser.Var_typeContext):
        pass


    # Enter a parse tree produced by decafJavierParser#assign_op.
    def enterAssign_op(self, ctx:decafJavierParser.Assign_opContext):
        pass

    # Exit a parse tree produced by decafJavierParser#assign_op.
    def exitAssign_op(self, ctx:decafJavierParser.Assign_opContext):
        pass


    # Enter a parse tree produced by decafJavierParser#method_name.
    def enterMethod_name(self, ctx:decafJavierParser.Method_nameContext):
        pass

    # Exit a parse tree produced by decafJavierParser#method_name.
    def exitMethod_name(self, ctx:decafJavierParser.Method_nameContext):
        pass



del decafJavierParser