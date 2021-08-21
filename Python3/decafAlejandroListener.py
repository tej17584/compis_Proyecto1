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


    # Enter a parse tree produced by decafAlejandroParser#vardeclr.
    def enterVardeclr(self, ctx:decafAlejandroParser.VardeclrContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#vardeclr.
    def exitVardeclr(self, ctx:decafAlejandroParser.VardeclrContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#field_declr.
    def enterField_declr(self, ctx:decafAlejandroParser.Field_declrContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#field_declr.
    def exitField_declr(self, ctx:decafAlejandroParser.Field_declrContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#array_id.
    def enterArray_id(self, ctx:decafAlejandroParser.Array_idContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#array_id.
    def exitArray_id(self, ctx:decafAlejandroParser.Array_idContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#field_var.
    def enterField_var(self, ctx:decafAlejandroParser.Field_varContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#field_var.
    def exitField_var(self, ctx:decafAlejandroParser.Field_varContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#var_id.
    def enterVar_id(self, ctx:decafAlejandroParser.Var_idContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#var_id.
    def exitVar_id(self, ctx:decafAlejandroParser.Var_idContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#struct_declr.
    def enterStruct_declr(self, ctx:decafAlejandroParser.Struct_declrContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#struct_declr.
    def exitStruct_declr(self, ctx:decafAlejandroParser.Struct_declrContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#method_declr.
    def enterMethod_declr(self, ctx:decafAlejandroParser.Method_declrContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#method_declr.
    def exitMethod_declr(self, ctx:decafAlejandroParser.Method_declrContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#return_type.
    def enterReturn_type(self, ctx:decafAlejandroParser.Return_typeContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#return_type.
    def exitReturn_type(self, ctx:decafAlejandroParser.Return_typeContext):
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


    # Enter a parse tree produced by decafAlejandroParser#method_call_inter.
    def enterMethod_call_inter(self, ctx:decafAlejandroParser.Method_call_interContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#method_call_inter.
    def exitMethod_call_inter(self, ctx:decafAlejandroParser.Method_call_interContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#method_call.
    def enterMethod_call(self, ctx:decafAlejandroParser.Method_callContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#method_call.
    def exitMethod_call(self, ctx:decafAlejandroParser.Method_callContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#expr.
    def enterExpr(self, ctx:decafAlejandroParser.ExprContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#expr.
    def exitExpr(self, ctx:decafAlejandroParser.ExprContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#location.
    def enterLocation(self, ctx:decafAlejandroParser.LocationContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#location.
    def exitLocation(self, ctx:decafAlejandroParser.LocationContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#callout_arg.
    def enterCallout_arg(self, ctx:decafAlejandroParser.Callout_argContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#callout_arg.
    def exitCallout_arg(self, ctx:decafAlejandroParser.Callout_argContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#int_literal.
    def enterInt_literal(self, ctx:decafAlejandroParser.Int_literalContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#int_literal.
    def exitInt_literal(self, ctx:decafAlejandroParser.Int_literalContext):
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


    # Enter a parse tree produced by decafAlejandroParser#bin_op.
    def enterBin_op(self, ctx:decafAlejandroParser.Bin_opContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#bin_op.
    def exitBin_op(self, ctx:decafAlejandroParser.Bin_opContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#arith_op.
    def enterArith_op(self, ctx:decafAlejandroParser.Arith_opContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#arith_op.
    def exitArith_op(self, ctx:decafAlejandroParser.Arith_opContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#var_type.
    def enterVar_type(self, ctx:decafAlejandroParser.Var_typeContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#var_type.
    def exitVar_type(self, ctx:decafAlejandroParser.Var_typeContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#assign_op.
    def enterAssign_op(self, ctx:decafAlejandroParser.Assign_opContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#assign_op.
    def exitAssign_op(self, ctx:decafAlejandroParser.Assign_opContext):
        pass


    # Enter a parse tree produced by decafAlejandroParser#method_name.
    def enterMethod_name(self, ctx:decafAlejandroParser.Method_nameContext):
        pass

    # Exit a parse tree produced by decafAlejandroParser#method_name.
    def exitMethod_name(self, ctx:decafAlejandroParser.Method_nameContext):
        pass



del decafAlejandroParser