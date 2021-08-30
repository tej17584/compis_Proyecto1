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
        self.conteoIfs = 0

    def enterStatement(self, ctx: decafAlejandroParser.StatementContext):
        return super().enterStatement(ctx)

    def exitProgram(self, ctx: decafAlejandroParser.ProgramContext):
        diccionarioVarsFinal = self.tablaSimbolos.getDictVar()
        print(diccionarioVarsFinal)
        print("")
        diccionarioMethodsFinal = self.tablaSimbolos.getDictMethod()
        print(diccionarioMethodsFinal)
        # ! verificamos la logica de la definicion de main sin parametros
        mainMethodExists = self.tablaSimbolos.checkMethodInMethodSymbolTableV2(
            "main")
        tipoMetodo = self.tablaSimbolos.getTypeMethodDictMethods("main")
        parametros = self.tablaSimbolos.getParametersDictMethods("main")
        returnValue = self.tablaSimbolos.getReturnDictMethods("main")
        if(mainMethodExists == True and tipoMetodo == "void" and len(parametros) == 0 and returnValue == False):
            pass
        else:
            print(
                f'ERROR. No está declarado el método main sin parámetros  linea: {ctx.start.line}, columna: {ctx.start.column}')
            exit()

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
        # miramos si tiene return
        returnValue = ""
        returnExpresion = ""
        try:
            # el nombre de la variable
            returnValue = ctx.block().statement()[0].expr().getText()
        except:
            pass
        try:
            # el valor de return
            returnExpresion = ctx.block().statement()[0].RETURN().getText()
        except:
            pass
        #! agregamos los métodos
        name = ctx.method_name().getText()  # el nombre del método
        tipo = ctx.return_type().getText()
        # print("El tipo de metodo es", tipo)
        parametros = ctx.var_id()
        tiposVariables = ctx.var_type()
        line = ctx.start.line
        column = ctx.start.column
        scope = self.scopeActual
        methodExists = self.tablaSimbolos.checkMethodInMethodSymbolTableV2(
            name)
        if(methodExists == False):
            # ahora miramos los parametros
            parametrosToAdd = []
            methodReturnsThings = False
            for x in range(0, len(parametros)):
                # agregamos al array para guardarlo
                variable = parametros[x].getText()
                tipoVariable = tiposVariables[x].getText()
                parametrosToAdd.append(variable)
                # una vez agregado, ahora vamos a guardar la variable en el scope
                varExists = self.tablaSimbolos.checkVarInVarSymbolTableV2(
                    variable, scope)
                if(varExists == False):
                    if("struct" in tipo):
                        tipo = tipo.replace("struct", "")
                    self.tablaSimbolos.AddNewVar_DictVar(
                        variable, tipoVariable, scope, 0, 0)
                elif(varExists == True):
                    print(
                        f'Error, la variable {variable} ya fue declarada en el scope {scope}. Linea: {line} columna: {column} ')
                    exit()
                # print("parametros", parametros[x].getText())
            if(returnExpresion == "return" and returnValue != ""):
                methodReturnsThings = True
            if(tipo != "void"):
                if(returnExpresion == "" or returnValue == ""):
                    print(
                        f'ERROR. El método {name} no esta retornando nada. "{self.scopeActual}", linea: {ctx.start.line}, columna: {ctx.start.column}')
                    exit()
                # una vez guardados parametros y variables, ahora guardamos la nueva entrada del diccionario
            self.tablaSimbolos.AddNewMethod_DictMethod(
                tipo, name, parametrosToAdd, methodReturnsThings, self.scopeAnterior)
        else:
            print(
                f'Error, el método {name} ya fue declarado anteriormente. Linea: {line} columna: {column} ')
            exit()
        # print("La variable existe", methodExists)

    def exitMethod_declr(self, ctx: decafAlejandroParser.Method_declrContext):
        # actualizamos el scope cuando salimso de la funcion
        self.scopeActual = self.scopeAnterior

    def enterStatement(self, ctx: decafAlejandroParser.StatementContext):
        # validaciones para que no entre por gusto
        hasReturnValue = self.functions.hasReturnValue(ctx)
        name = ""
        try:
            name = ctx.location().getText()  # el nombre de la variable
        except:
            pass
        # si tiene valor de retorno
        if(hasReturnValue):
            # verificamos si deberia poder retornar algo
            methodTypeFromTable = self.tablaSimbolos.getTypeMethodDictMethods(
                self.scopeActual)
            if(methodTypeFromTable == "void"):
                print(
                    f'ERROR. Un método tipo VOID no puede devolver algo. "{self.scopeActual}", linea: {ctx.start.line}, columna: {ctx.start.column}')
                exit()
            else:
                value = ctx.expr().getText()
                arrayVars = []
                if((value == "true" or value == "false") and methodTypeFromTable != "boolean"):
                    print(
                        f'ERROR. Variable boolean retornada en un método NO booleano "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                    exit()
                elif(self.functions.checkIfIsInt(value) and methodTypeFromTable != "int"):
                    print(
                        f'ERROR. Variable int retornada en un método NO INT "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                    exit()
                elif(self.functions.checkGeneraltype(value, "string") and methodTypeFromTable != "string"):
                    print(
                        f'ERROR. Variable string retornada en un método NO STRING "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                    exit()

                if(self.functions.checkIfIsInt(value) == False and value != "false" and value != "true" and self.functions.checkGeneraltype(value, "string") == False):
                    for i in range(len(value)):
                        var = self.tablaSimbolos.getTypeVarDictVar(
                            value[i], self.scopeActual)
                        if isinstance(var, str) and len(var) > 0:
                            arrayVars.append(var)
                        if not len(set(arrayVars)) <= 1:
                            print(
                                f'ERROR. Hay un error en el valor de retorno en el scope "{self.scopeActual}", linea: {ctx.start.line}')
                            exit()
                    e = ""
                    if(len(arrayVars) > 0):
                        e = next(iter(arrayVars))
                    # obtenemos el tipo de método
                    if(methodTypeFromTable != e):
                        print(
                            f'ERROR. El tipo de retorno de un método SIEMPRE debe ser igual al declarado "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                        exit()

        else:
            methodCallAsignacion = ""
            mehtodCallNormal = ""
            try:
                methodCallAsignacion = ctx.expr().method_call()
            except:
                pass
            try:
                mehtodCallNormal = ctx.method_call()
            except:
                pass
            # este if es para ver si la llamada a un método es con asignacion
            if(methodCallAsignacion != None and methodCallAsignacion != ""):
                metodoAsignado = ctx.expr().method_call().method_call_inter().method_name().getText()
                # verificamos si deberia poder retornar algo
                scope = self.scopeActual
                methodTypeFromTableV2 = self.tablaSimbolos.getTypeMethodDictMethods(
                    metodoAsignado)
                tipoGuardado = self.tablaSimbolos.getTypeVarDictVar(
                    name, scope)
                if(methodTypeFromTableV2 == "void"):
                    print(
                        f'ERROR. Un metodo VOID no puede asignarse a una variable. linea: {ctx.start.line} , columna: {ctx.start.column}')
                    exit()
                if(methodTypeFromTableV2 == ""):
                    print(
                        f'ERROR. El método "{metodoAsignado}" NO existe y esta siendo asignado a la variable local "{name}". linea: {ctx.start.line} , columna: {ctx.start.column}')
                    exit()
                elif(tipoGuardado != methodTypeFromTableV2):
                    print(
                        f'ERROR. El método "{metodoAsignado}" tiene un tipo de retorno "{methodTypeFromTableV2}" y la variable local "{name}" es del tipo "{tipoGuardado}" NO CONCUERDAN . linea: {ctx.start.line} , columna: {ctx.start.column}')
                    exit()
                # ahora verificamos que si necesita parámetros
                parametrosMetodo = []
                parametrosEnviados = ""  # variable para ver si NOSOTROS estamos mandando parametros
                parametrosMetodo = self.tablaSimbolos.getParametersTypeDictMethods(
                    metodoAsignado)
                if(len(parametrosMetodo) > 0):
                    nombreParametro = ""
                    tipoParametrosEnviar = []
                    tipoParametrosEnviarGlobal = []
                    # print("tipos parámetros esperados por el método ",
                    #      parametrosMetodo)
                    parametrosEnviados = ctx.expr().method_call(
                    ).method_call_inter().expr()
                    for x in range(0, len(parametrosEnviados)):
                        canTryAgain = True
                        if(canTryAgain):
                            try:
                                interTry = parametrosEnviados[x].location(
                                ).var_id().getText()
                                if(interTry == "true" or interTry == "false"):
                                    tipoParametroEnviado = "boolean"
                                    canTryAgain = False
                                else:
                                    tipoParametroEnviado = "variable"
                                    canTryAgain = False
                            except:
                                pass
                        if(canTryAgain):
                            try:
                                interTry = parametrosEnviados[x].literal(
                                ).int_literal().getText()
                                tipoParametroEnviado = "int"
                                canTryAgain = False
                            except:
                                pass
                        if(canTryAgain):
                            try:
                                interTry = parametrosEnviados[x].literal(
                                ).getText()
                                tipoParametroEnviado = "string"
                                canTryAgain = False
                            except:
                                pass
                        if(tipoParametroEnviado == "variable"):
                            nombreParametro = parametrosEnviados[x].location(
                            ).var_id().getText()
                            tipoParametro = self.tablaSimbolos.getTypeVarDictVar(
                                nombreParametro, self.scopeActual)
                            tipoParametroG = self.tablaSimbolos.getTypeVarDictVar(
                                nombreParametro, "global")
                            tipoParametrosEnviar.append(tipoParametro)
                            tipoParametrosEnviarGlobal.append(
                                tipoParametroG)
                        elif(tipoParametroEnviado == "boolean"):
                            nombreParametro = parametrosEnviados[x].location(
                            ).var_id().getText()
                            tipoParametrosEnviar.append("boolean")
                            tipoParametrosEnviarGlobal.append("boolean")
                        elif(tipoParametroEnviado == "string"):
                            nombreParametro = parametrosEnviados[x].literal(
                            ).getText()
                            tipoParametrosEnviar.append("string")
                            tipoParametrosEnviarGlobal.append("string")
                        elif(tipoParametroEnviado == "int"):
                            nombreParametro = parametrosEnviados[x].literal(
                            ).int_literal().getText()
                            tipoParametrosEnviar.append("int")
                            tipoParametrosEnviarGlobal.append("int")
                    # print("TIPOS DAODS ", tipoParametrosEnviar)
                    if(len(parametrosMetodo) != len(tipoParametrosEnviar)):
                        print(
                            f'ERROR. El método "{metodoAsignado}" pide un total de {len(parametrosMetodo)} parámetros, pero se están enviando {len(tipoParametrosEnviar)}.linea: {ctx.start.line} , columna: {ctx.start.column}')
                        exit()
                    for y in range(0, len(parametrosMetodo)):
                        if(tipoParametrosEnviar[y] != ""):
                            if(parametrosMetodo[y] != tipoParametrosEnviar[y]):
                                print(
                                    f'ERROR. Un parámetro enviado al método "{metodoAsignado}" no es del mismo tipo REQUERIDO .linea: {ctx.start.line} , columna: {ctx.start.column}')
                                exit()
                        else:
                            print(
                                f'ERROR. Un parámetro enviado al método "{metodoAsignado}" NO ha sido DECLARADO.linea: {ctx.start.line} , columna: {ctx.start.column}')
                            exit()
                    # revisamos globalmente
                    for y in range(0, len(parametrosMetodo)):
                        if(tipoParametrosEnviarGlobal[y] != ""):
                            if(parametrosMetodo[y] != tipoParametrosEnviarGlobal[y]):
                                print(
                                    f'ERROR2. Un parámetro enviado al método "{metodoAsignado}" no es del mismo tipo REQUERIDO .linea: {ctx.start.line} , columna: {ctx.start.column}')
                                exit()
            # este if es para ver si la llamada a un metodo es sin asignacion, solo normalmente
            elif(mehtodCallNormal != None and mehtodCallNormal != ""):
                metodoAsignado = ctx.method_call().method_call_inter().method_name().getText()
                # verificamos si deberia poder retornar algo
                scope = self.scopeActual
                methodTypeFromTableV2 = self.tablaSimbolos.getTypeMethodDictMethods(
                    metodoAsignado)
                if(methodTypeFromTableV2 == ""):
                    print(
                        f'ERRORA2. El método "{metodoAsignado}" NO existe "{name}". linea: {ctx.start.line} , columna: {ctx.start.column}')
                    exit()
                # ahora verificamos que si necesita parámetros
                parametrosMetodo = []
                parametrosEnviados = ""  # variable para ver si NOSOTROS estamos mandando parametros
                parametrosMetodo = self.tablaSimbolos.getParametersTypeDictMethods(
                    metodoAsignado)
                if(len(parametrosMetodo) > 0):
                    nombreParametro = ""
                    tipoParametrosEnviar = []
                    tipoParametrosEnviarGlobal = []
                    # print("tipos parámetros esperados por el método ",
                    #      parametrosMetodo)
                    tipoParametroEnviado = ""
                    parametrosEnviados = ctx.method_call().method_call_inter().expr()
                    if(len(parametrosEnviados) > 0):
                        for x in range(0, len(parametrosEnviados)):
                            canTryAgain = True
                            if(canTryAgain):
                                try:
                                    interTry = parametrosEnviados[x].location(
                                    ).var_id().getText()
                                    if(interTry == "true" or interTry == "false"):
                                        tipoParametroEnviado = "boolean"
                                        canTryAgain = False
                                    else:
                                        tipoParametroEnviado = "variable"
                                        canTryAgain = False
                                except:
                                    pass
                            if(canTryAgain):
                                try:
                                    interTry = parametrosEnviados[x].literal(
                                    ).int_literal().getText()
                                    tipoParametroEnviado = "int"
                                    canTryAgain = False
                                except:
                                    pass
                            if(canTryAgain):
                                try:
                                    interTry = parametrosEnviados[x].literal(
                                    ).getText()
                                    tipoParametroEnviado = "string"
                                    canTryAgain = False
                                except:
                                    pass

                            if(tipoParametroEnviado == "variable"):
                                nombreParametro = parametrosEnviados[x].location(
                                ).var_id().getText()
                                tipoParametro = self.tablaSimbolos.getTypeVarDictVar(
                                    nombreParametro, self.scopeActual)
                                tipoParametroG = self.tablaSimbolos.getTypeVarDictVar(
                                    nombreParametro, "global")
                                tipoParametrosEnviar.append(tipoParametro)
                                tipoParametrosEnviarGlobal.append(
                                    tipoParametroG)
                            elif(tipoParametroEnviado == "boolean"):
                                nombreParametro = parametrosEnviados[x].location(
                                ).var_id().getText()
                                tipoParametrosEnviar.append("boolean")
                                tipoParametrosEnviarGlobal.append("boolean")
                            elif(tipoParametroEnviado == "string"):
                                nombreParametro = parametrosEnviados[x].literal(
                                ).getText()
                                tipoParametrosEnviar.append("string")
                                tipoParametrosEnviarGlobal.append("string")
                            elif(tipoParametroEnviado == "int"):
                                nombreParametro = parametrosEnviados[x].literal(
                                ).int_literal().getText()
                                tipoParametrosEnviar.append("int")
                                tipoParametrosEnviarGlobal.append("int")
                    # print("TIPOS DAODS ", tipoParametrosEnviar)
                    if(len(parametrosMetodo) != len(tipoParametrosEnviar)):
                        print(
                            f'ERROR. El método "{metodoAsignado}" pide un total de {len(parametrosMetodo)} parámetros, pero se están enviando {len(tipoParametrosEnviar)}.linea: {ctx.start.line} , columna: {ctx.start.column}')
                        exit()
                    # Reviosamos localmente
                    for y in range(0, len(parametrosMetodo)):
                        if(tipoParametrosEnviar[y] != ""):
                            if(parametrosMetodo[y] != tipoParametrosEnviar[y]):
                                print(
                                    f'ERROR1. Un parámetro enviado al método "{metodoAsignado}" no es del mismo tipo REQUERIDO .linea: {ctx.start.line} , columna: {ctx.start.column}')
                                exit()
                    # revisamos globalmente
                    for y in range(0, len(parametrosMetodo)):
                        if(tipoParametrosEnviarGlobal[y] != ""):
                            if(parametrosMetodo[y] != tipoParametrosEnviarGlobal[y]):
                                print(
                                    f'ERROR2. Un parámetro enviado al método "{metodoAsignado}" no es del mismo tipo REQUERIDO .linea: {ctx.start.line} , columna: {ctx.start.column}')
                                exit()

            else:
                if(ctx.IF()):
                    print("hay if nuevo scope")
                    print("scope antes del IF", self.scopeActual)
                    self.conteoIfs += 1
                    scopeNuevo = 'if'+str(self.conteoIfs)
                    self.scopeAnterior = self.scopeActual
                    self.scopeActual = scopeNuevo
                    print("scope antes LUEGO  IF", self.scopeActual)
                    tipoVariableEqOps = ""
                    tipoVariablecondOps = ""
                    tipoVariableRelOps = ""
                    try:
                        tipoVariableEqOps = ctx.expr().bin_op().eq_op().getText()
                    except:
                        pass
                    try:
                        tipoVariablecondOps = ctx.expr().bin_op().cond_op().getText()
                    except:
                        pass
                    try:
                        tipoVariableRelOps = ctx.expr().bin_op().rel_op().getText()
                    except:
                        pass
                    if(tipoVariableEqOps == "" and tipoVariablecondOps == "" and tipoVariableRelOps == ""):
                        print(
                            f'ERROR. En una condicion, deben darse valores booleanos "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                        exit()
                    # agregamos el nuevo if como metodo
                    self.tablaSimbolos.AddNewMethod_DictMethod(
                        "", scopeNuevo, [], False, self.scopeAnterior)
                    # variables de EQ_OPS
                    arraySplitEqOps = []
                    if((tipoVariableEqOps == "==" or tipoVariableEqOps == "!=")
                            and tipoVariablecondOps == "" and tipoVariableRelOps == ""):
                        # hacemos split de cada valor y vamos a buscarlo
                        arraySplitEqOps = ctx.expr().getText().split(tipoVariableEqOps)
                        valor1 = arraySplitEqOps[0]
                        valor2 = arraySplitEqOps[1]
                        varExists3 = ""
                        varExists4 = ""
                        varInformation = []
                        for x in arraySplitEqOps:
                            if((valor2 == "true" or valor2 == "false") and (valor1 != "true" and valor1 != "false")):
                                varExists3 = self.tablaSimbolos.varExistsRecursivo(
                                    valor1, self.scopeActual, False)
                                if(varExists3 == False):
                                    print(
                                        f'ERROR. La variable {valor1} NO ha sido declarada o no es valida "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                    exit()
                                else:
                                    varInformation = self.tablaSimbolos.getVarInformationRecursivo(
                                        valor1, self.scopeActual, False, [])
                                    # el tipo de variable
                                    varTypeInterno = varInformation[1]
                                    if(varTypeInterno != "boolean"):
                                        print(
                                            f'ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        exit()
                            elif((valor1 == "true" or valor1 == "false") and (valor2 != "true" and valor2 != "false")):
                                varExists3 = self.tablaSimbolos.varExistsRecursivo(
                                    valor2, self.scopeActual, False)
                                if(varExists3 == False):
                                    print(
                                        f'ERROR. La variable {valor2} NO ha sido declarada o no es valida "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                    exit()
                                else:
                                    varInformation = self.tablaSimbolos.getVarInformationRecursivo(
                                        valor2, self.scopeActual, False, [])
                                    # el tipo de variable
                                    varTypeInterno = varInformation[1]
                                    if(varTypeInterno != "boolean"):
                                        print(
                                            f'ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        exit()
                            elif(self.functions.checkIfIsInt(valor1) and self.functions.checkIfIsInt(valor2) == False):
                                varExists3 = self.tablaSimbolos.varExistsRecursivo(
                                    valor2, self.scopeActual, False)
                                if(varExists3 == False):
                                    print(
                                        f'ERROR. La variable {valor2} NO ha sido declarada o no es valida "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                    exit()
                                else:
                                    varInformation = self.tablaSimbolos.getVarInformationRecursivo(
                                        valor2, self.scopeActual, False, [])
                                    # el tipo de variable
                                    varTypeInterno = varInformation[1]
                                    if(varTypeInterno != "int"):
                                        print(
                                            f'ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        exit()
                            elif(self.functions.checkIfIsInt(valor2) and (self.functions.checkIfIsInt(valor1) == False)):
                                varExists3 = self.tablaSimbolos.varExistsRecursivo(
                                    valor1, self.scopeActual, False)
                                if(varExists3 == False):
                                    print(
                                        f'ERROR. La variable {valor1} NO ha sido declarada o no es valida "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                    exit()
                                else:
                                    varInformation = self.tablaSimbolos.getVarInformationRecursivo(
                                        valor1, self.scopeActual, False, [])
                                    # el tipo de variable
                                    varTypeInterno = varInformation[1]
                                    if(varTypeInterno != "int"):
                                        print(
                                            f'ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        exit()
                            elif(self.functions.checkGeneraltype(valor1, "string") and self.functions.checkGeneraltype(valor2, "string") == False):
                                varExists3 = self.tablaSimbolos.varExistsRecursivo(
                                    valor2, self.scopeActual, False)
                                if(varExists3 == False):
                                    print(
                                        f'ERROR. La variable {valor2} NO ha sido declarada o no es valida "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                    exit()
                                else:
                                    varInformation = self.tablaSimbolos.getVarInformationRecursivo(
                                        valor2, self.scopeActual, False, [])
                                    # el tipo de variable
                                    varTypeInterno = varInformation[1]
                                    if(varTypeInterno != "string"):
                                        print(
                                            f'ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        exit()
                            elif(self.functions.checkGeneraltype(valor2, "string") and self.functions.checkGeneraltype(valor1, "string") == False):
                                varExists3 = self.tablaSimbolos.varExistsRecursivo(
                                    valor1, self.scopeActual, False)
                                if(varExists3 == False):
                                    print(
                                        f'ERROR. La variable {valor1} NO ha sido declarada o no es valida "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                    exit()
                                else:
                                    varInformation = self.tablaSimbolos.getVarInformationRecursivo(
                                        valor1, self.scopeActual, False, [])
                                    # el tipo de variable
                                    varTypeInterno = varInformation[1]
                                    if(varTypeInterno != "string"):
                                        print(
                                            f'ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        exit()
                            else:
                                # verificamos ambas variables
                                varExists3 = self.tablaSimbolos.varExistsRecursivo(
                                    valor1, self.scopeActual, False)
                                varExists4 = self.tablaSimbolos.varExistsRecursivo(
                                    valor2, self.scopeActual, False)
                                if(varExists3 == True and varExists4 == False):
                                    print(
                                        f'ERROR. Una variable no ha sido declarada en una condicion "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                    exit()
                                elif(varExists3 == False and varExists4 == True):
                                    print(
                                        f'ERROR. Una variable no ha sido declarada en una condicion "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                    exit()
                                elif(varExists3 == False and varExists4 == False):
                                    print(
                                        f'ERROR. Una variable no ha sido declarada en una condicion "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                    exit()
                                elif(varExists3 == True and varExists4 == True):
                                    varInformation1 = self.tablaSimbolos.getVarInformationRecursivo(
                                        valor1, self.scopeActual, False, [])
                                    varInformation2 = self.tablaSimbolos.getVarInformationRecursivo(
                                        valor2, self.scopeActual, False, [])
                                    # el tipo de variable
                                    varTypeInterno1 = varInformation1[1]
                                    varTypeInterno2 = varInformation2[1]
                                    if(varTypeInterno1 != varTypeInterno2):
                                        print(
                                            f'ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        exit()
                                # variables de  cond_OPS
                    if((tipoVariablecondOps == "&&" or tipoVariablecondOps == "||")
                            and tipoVariableEqOps == "" and tipoVariableRelOps == ""):
                        print("variable condOps")
                    # variables de REL_OPS
                    elif((tipoVariableRelOps == "<" or tipoVariableRelOps == "<=" or
                          tipoVariableRelOps == ">" or tipoVariableRelOps == ">=")
                            and tipoVariableEqOps == "" and tipoVariablecondOps == ""):
                        print("variableRelOps")
                else:
                    valorAsignado = ctx.expr().getText()
                    line = ctx.start.line
                    column = ctx.start.column
                    scope = self.scopeActual
                    if("[" in name and "]" in name):
                        name = name[0]
                    varExists = self.tablaSimbolos.checkVarInVarSymbolTableV2(
                        name, scope)
                    # verificamos si existe en el scope actual
                    if(varExists):
                        tipoGuardado = self.tablaSimbolos.getTypeVarDictVar(
                            name, scope)
                        typeMatch = self.functions.checkGeneraltype(
                            valorAsignado, tipoGuardado)
                        if(typeMatch == False):
                            print(
                                f'ERROR3. La variable {tipoGuardado} -> {name} <- está siendo asignada con el valor {valorAsignado} pero no son el mismo TIPO. linea: {ctx.start.line} , columna: {ctx.start.column}')
                            exit()
                        else:
                            print("")
                            # print("PRINT LOCAL", name)
                    else:
                        # si no existe en el scope actual, revismos en el global
                        varExists2 = self.tablaSimbolos.checkVarInVarSymbolTableV2(
                            name, "global")
                        if(varExists2):
                            # si existe en el global, verificamos que el tipo con el que fue guardado haga match
                            tipoGuardado = self.tablaSimbolos.getTypeVarDictVar(
                                name,  "global")
                            typeMatch = self.functions.checkGeneraltype(
                                valorAsignado, tipoGuardado)
                            if(typeMatch == False):
                                print(
                                    f'ERROR1. La variable {tipoGuardado} -> {name} <- está siendo asignada con el valor {valorAsignado} pero no son el mismo TIPO. linea: {ctx.start.line} , columna: {ctx.start.column}')
                                exit()
                            else:
                                print("PRINT GLOBAL")

                        elif(varExists2 == False):
                            print(
                                f'ERROR2. La variable -> {name} <- está siendo asignada con el valor {valorAsignado} ANTES de ser declarada. linea: {ctx.start.line} , columna: {ctx.start.column}')
                            exit()

                # print(self.tablaSimbolos.getDictVar())

    def exitStatement(self, ctx: decafAlejandroParser.StatementContext):
        if('if' in ctx.getText() or 'for' in ctx.getText() or 'while' in ctx.getText() or 'else' in ctx.getText()):
            self.scopeActual = self.scopeAnterior

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
                        arrayValue, self.scopeActual)
                    if(varExistsInner):
                        tipoDato = self.tablaSimbolos.getTypeVarDictVar(
                            oldArrayValue, scope)
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
