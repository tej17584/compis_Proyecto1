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
from pprint import pprint


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

    def enterProgram(self, ctx: decafAlejandroParser.ProgramContext):
        pprint("--------------------COMENZANDO REVISIÓN DE PROGRAMA--------------")
        pprint(" -----> LOS ERRORES APARECEERÁN ABAJO")
        pprint("")

    def exitProgram(self, ctx: decafAlejandroParser.ProgramContext):
        pprint(
            "------------------FINALIZADA REVISIÓN DE PROGRAMA------------------------")
        pprint("LOS DICCIONARIOS O TABLAS FINALES SON: ")
        pprint("")
        pprint("----------------------TABLA DE VARIABLES---------------------")
        diccionarioVarsFinal = self.tablaSimbolos.getDictVar()
        pprint(diccionarioVarsFinal)
        pprint("")
        pprint("----------------------TABLA DE METODOS---------------------")
        diccionarioMethodsFinal = self.tablaSimbolos.getDictMethod()
        pprint(diccionarioMethodsFinal)
        pprint("")
        pprint("----------------------TABLA DE ESTRUCTURAS---------------------")
        diccionarioStructsFinal = self.tablaSimbolos.getDictStruct()
        pprint(diccionarioStructsFinal)
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
                f'--> ERROR. No está declarado el método main sin parámetros  linea: {ctx.start.line}, columna: {ctx.start.column}')
            # exit()

    def enterStruct_declr(self, ctx: decafAlejandroParser.Struct_declrContext):
        # actualizamos el scope
        self.scopeAnterior = self.scopeActual
        self.scopeActual = ctx.ID().getText()
        # tomamos los datos que nos interesan
        name = ctx.ID().getText()
        tipo = ctx.STRUCT().getText()
        line = ctx.start.line
        column = ctx.start.column
        scope = self.scopeActual
        # agregamos la nueva estructura
        self.tablaSimbolos.AddNewStruct_DictStruct(
            name, tipo, self.scopeAnterior)
        # agregamos la estructura como nuevo método
        self.tablaSimbolos.AddNewMethod_DictMethod(
            "struct", name, [], False, self.scopeAnterior)

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
        returnExpresionIF = ""
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
                        f'--> Error_varDeclaration, la variable {variable} ya fue declarada en el scope {scope}. Linea: {line} columna: {column} ')
                    # exit()
            # el valor de return
            returnExpresionIF = ctx.block().statement()
            lenReturnExpresionIF = len(ctx.block().statement())
            for x in range(0, lenReturnExpresionIF):
                # obtenemos el obtjeto
                valorInterno = returnExpresionIF[x].block()
                for y in range(0, len(valorInterno)):
                    valorReturn = valorInterno[y].statement()[
                        0].getText()
                    if(valorReturn != "" or valorReturn != None):
                        if("return" in valorReturn):
                            returnExpresion = "return"

                # print("parametros", parametros[x].getText())
            if(returnExpresion == "return" and returnValue != ""):
                methodReturnsThings = True
            if(tipo != "void"):
                if(returnExpresion == "" or returnValue == ""):
                    print(
                        f'--> ERROR. El método {name} no esta retornando nada. "{self.scopeActual}", linea: {ctx.start.line}, columna: {ctx.start.column}')
                    # exit()
                # una vez guardados parametros y variables, ahora guardamos la nueva entrada del diccionario
            self.tablaSimbolos.AddNewMethod_DictMethod(
                tipo, name, parametrosToAdd, methodReturnsThings, self.scopeAnterior)
        else:
            print(
                f'--> Error, el método {name} ya fue declarado anteriormente. Linea: {line} columna: {column} ')
            # exit()
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
            if("if" in self.scopeActual or "while" in self.scopeActual):
                methodTypeFromTable = self.tablaSimbolos.getTypeMethodDictMethods(
                    self.scopeAnterior)
            else:
                methodTypeFromTable = self.tablaSimbolos.getTypeMethodDictMethods(
                    self.scopeActual)
            if(methodTypeFromTable == "void"):
                print(
                    f'--> ERROR. Un método tipo VOID no puede devolver algo. "{self.scopeActual}", linea: {ctx.start.line}, columna: {ctx.start.column}')
                # exit()
            else:
                value = ctx.expr().getText()
                arrayVars = []
                if((value == "true" or value == "false") and methodTypeFromTable != "boolean"):
                    print(
                        f'--> ERROR. Variable boolean retornada en un método NO booleano "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                    # exit()
                elif(self.functions.checkIfIsInt(value) and methodTypeFromTable != "int"):
                    print(
                        f'--> ERROR. Variable int retornada en un método NO INT "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                    # exit()
                elif(self.functions.checkGeneraltype(value, "string") and methodTypeFromTable != "string"):
                    print(
                        f'--> ERROR. Variable string retornada en un método NO STRING "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                    # exit()

                if(self.functions.checkIfIsInt(value) == False and value != "false" and value != "true" and self.functions.checkGeneraltype(value, "string") == False):
                    if("." in value):
                        indice = value.index(".")
                        variableEstructura = value[0:indice]
                        variableDentroEstructura = value[indice+1:len(value)]
                        # si la variable que hicimos split o partimos tiene corchete obtenemos solo el nombre
                        if("[" in variableEstructura or "]" in variableEstructura):
                            indexCorchete = variableEstructura.index("[")
                            variableEstructura = variableEstructura[0: indexCorchete]
                        if("[" in variableDentroEstructura or "]" in variableDentroEstructura):
                            indexCorchete = variableDentroEstructura.index("[")
                            variableDentroEstructura = variableDentroEstructura[0: indexCorchete]
                        # mandamos ambos parametros
                        structExists = self.tablaSimbolos.varExistsRecursivo(
                            variableEstructura, self.scopeActual, False)
                        if(structExists):
                            informacionStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                variableEstructura, self.scopeActual, False, [])
                            innerVarExists = self.tablaSimbolos.checkVarInVarSymbolTableV2(
                                variableDentroEstructura, informacionStruct[1])
                            if(innerVarExists):
                                informacionInnerVarStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                    variableDentroEstructura, informacionStruct[1], False, [])
                                if(informacionInnerVarStruct[1] != methodTypeFromTable):
                                    print(
                                        f'--> ERROR. Variable "{variableDentroEstructura}" no es del tipo requerido de retorno de {self.scopeActual} "{informacionStruct[1]}".  "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                else:
                                    pass
                            else:
                                print(
                                    f'--> ERROR. Variable "{variableDentroEstructura}" no existe DENTRO de la estructura "{informacionStruct[1]}".  "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                        else:
                            print(
                                f'--> ERROR. Variable {variableEstructura} de tipo Estructura NO existe "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                    # exit()
                    else:
                        scope = self.scopeActual
                        if("+" in value or "-" in value or "/" in value or "*" in value or "%" in value):
                            splitHijos = self.functions.removeOperations(value)
                            for x in splitHijos:
                                # o variable, o numero u operador
                                hijo = x
                                if(hijo != ""):
                                    if(self.functions.checkIfIsInt(hijo) == False):
                                        # si no es int verificamos que NO sea variable
                                        varExists = self.tablaSimbolos.varExistsRecursivo(
                                            hijo, scope, False)
                                        if(varExists):
                                            informationHijo = self.tablaSimbolos.getVarInformationRecursivo(
                                                hijo, scope, False, [])
                                            if(informationHijo[1] != "int"):
                                                print(
                                                    f'--> ERROR_RETURN. La variable o valor "{hijo}" NO es del tipo INT. linea: {ctx.start.line} , columna: {ctx.start.column}')
                                                # exit()
                                        else:
                                            # si no es var, miramos si no es método en el return
                                            # obtenemos el tipo de método
                                            tipoMetodo = self.tablaSimbolos.getTypeMethodDictMethods(
                                                hijo)
                                            if(tipoMetodo != "int"):
                                                print(
                                                    f'--> ERROR_RETURN. La variable o método "{hijo}" NO es del tipo INT y se intenta usar en una operación aritimética de return. linea: {ctx.start.line} , columna: {ctx.start.column}')
                        else:
                            for i in range(len(value)):
                                varExistsReturn = self.tablaSimbolos.varExistsRecursivo(
                                    value[i], self.scopeActual, False)
                                if(varExistsReturn == False):
                                    print(
                                        f'--> ERROR. La variable retornada NO existe  "{self.scopeActual}", linea: {ctx.start.line}')
                                    # exit()
                                varinformation = self.tablaSimbolos.getVarInformationRecursivo(
                                    value[i], self.scopeActual, False, [])
                                if isinstance(varinformation[1], str) and len(varinformation[1]) > 0:
                                    arrayVars.append(varinformation[1])
                                if not len(set(arrayVars)) <= 1:
                                    print(
                                        f'--> ERROR. Hay un error en el valor de retorno en el scope "{self.scopeActual}", linea: {ctx.start.line}')
                                    # exit()
                            e = ""
                            if(len(arrayVars) > 0):
                                e = next(iter(arrayVars))
                            # obtenemos el tipo de método
                            if(methodTypeFromTable != e):
                                print(
                                    f'--> ERROR. El tipo de retorno de un método SIEMPRE debe ser igual al declarado "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                # exit()

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
                tipoGuardado = ""
                metodoAsignado = ctx.expr().method_call().method_call_inter().method_name().getText()
                # verificamos si deberia poder retornar algo
                scope = self.scopeActual
                methodTypeFromTableV2 = self.tablaSimbolos.getTypeMethodDictMethods(
                    metodoAsignado)
                # verificamos si es una estructura
                if("." in name):  # es una estructura
                    indice = name.index(".")
                    variableEstructura = name[0:indice]
                    variableDentroEstructura = name[indice+1:len(name)]
                    # si la variable que hicimos split o partimos tiene corchete obtenemos solo el nombre
                    if("[" in variableEstructura or "]" in variableEstructura):
                        indexCorchete = variableEstructura.index("[")
                        variableEstructura = variableEstructura[0: indexCorchete]
                    if("[" in variableDentroEstructura or "]" in variableDentroEstructura):
                        indexCorchete = variableDentroEstructura.index("[")
                        variableDentroEstructura = variableDentroEstructura[0: indexCorchete]
                    structExists = self.tablaSimbolos.varExistsRecursivo(
                        variableEstructura, self.scopeActual, False)
                    if(structExists):  # si la estructura existe
                        # obtenemos infromacion de la estructura y d ela variable que estamos apuntando
                        informacionStruct = self.tablaSimbolos.getVarInformationRecursivo(
                            variableEstructura, self.scopeActual, False, [])
                        if("." in variableDentroEstructura):  # si por casualidad tenemos OTRO nivel
                            indice2 = variableDentroEstructura.index(".")
                            # c
                            variableEstructura2 = variableDentroEstructura[0:indice2]
                            # a
                            variableDentroEstructura2 = variableDentroEstructura[indice2+1:len(
                                variableDentroEstructura)]
                            structExists2 = self.tablaSimbolos.varExistsRecursivo(
                                variableEstructura2, informacionStruct[1], False)
                            if(structExists2):  # si la estructura existe
                                # obtenemos infromacion de la estructura y d ela variable que estamos apuntando
                                informacionStruct2 = self.tablaSimbolos.getVarInformationRecursivo(
                                    variableEstructura2, informacionStruct[1], False, [])
                                innerVarExists2 = self.tablaSimbolos.checkVarInVarSymbolTableV2(
                                    variableDentroEstructura2, informacionStruct2[1])
                                if(innerVarExists2):
                                    # obtenemos la información de la variable DENTRO de la estructura
                                    informacionInnerVarStruct2 = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableDentroEstructura2, informacionStruct2[1], False, [])
                                    # obtenemos el tipo de dato
                                    tipoDatoInnerVariable2 = informacionInnerVarStruct2[1]
                                    tipoGuardado = tipoDatoInnerVariable2  # lo asignamos a la variable
                                else:
                                    print(
                                        f'--> ERROR33333. Variable anidada "{variableDentroEstructura2}" no existe DENTRO de la estructura "{informacionStruct[1]}".  "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                            else:
                                print(
                                    f'--> ERROR. Variable anidada {variableEstructura2} de tipo Estructura NO existe "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                        else:
                            innerVarExists = self.tablaSimbolos.checkVarInVarSymbolTableV2(
                                variableDentroEstructura, informacionStruct[1])
                            if(innerVarExists):
                                # obtenemos la información de la variable DENTRO de la estructura
                                informacionInnerVarStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                    variableDentroEstructura, informacionStruct[1], False, [])
                                # obtenemos el tipo de dato
                                tipoDatoInnerVariable = informacionInnerVarStruct[1]
                                tipoGuardado = tipoDatoInnerVariable  # lo asignamos a la variable
                            else:
                                print(
                                    f'--> ERROR33333. Variable "{variableDentroEstructura}" no existe DENTRO de la estructura "{informacionStruct[1]}".  "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                    else:  # si no existe
                        print(
                            f'--> ERROR. Variable {variableEstructura} de tipo Estructura NO existe "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')

                else:  # es una variable NORMAL
                    # obtenemos la informacion
                    # obtenemos infromacion de la estructura y d ela variable que estamos apuntando
                    informationVariable = self.tablaSimbolos.getVarInformationRecursivo(
                        name, scope, False, [])
                    tipoGuardado = informationVariable[1]

                if(methodTypeFromTableV2 == "void"):
                    print(
                        f'--> ERROR. Un metodo VOID no puede asignarse a una variable. linea: {ctx.start.line} , columna: {ctx.start.column}')
                    # exit()
                if(methodTypeFromTableV2 == ""):
                    print(
                        f'--> ERROR. El método "{metodoAsignado}" NO existe y esta siendo asignado a la variable local "{name}". linea: {ctx.start.line} , columna: {ctx.start.column}')
                    # exit()
                elif(tipoGuardado != methodTypeFromTableV2):
                    print(
                        f'--> ERROR. El método "{metodoAsignado}" tiene un tipo de retorno "{methodTypeFromTableV2}" y la variable local "{name}" es del tipo "{tipoGuardado}" NO CONCUERDAN . linea: {ctx.start.line} , columna: {ctx.start.column}')
                    # exit()
                # ahora verificamos que si necesita parámetros
                parametrosMetodo = []
                tipoParametroEnviado = ""
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
                        if(canTryAgain):  # por si es metodo
                            try:
                                interTry = parametrosEnviados[x].method_call(
                                ).getText()
                                tipoParametroEnviado = "metodo"
                                canTryAgain = False
                            except:
                                pass
                        if(canTryAgain):  # por si es estructura
                            try:
                                interTry = parametrosEnviados[x].location(
                                ).array_id().getText()
                                tipoParametroEnviado = "array"
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
                        elif(tipoParametroEnviado == "metodo"):
                            nombreParametro = parametrosEnviados[x].method_call(
                            ).getText()
                            if("(" in nombreParametro):
                                nombreParametro = nombreParametro.replace(
                                    "(", "")
                            if(")" in nombreParametro):
                                nombreParametro = nombreParametro.replace(
                                    ")", "")
                            # obtenemos el tipo de método
                            tipoMetodo = self.tablaSimbolos.getTypeMethodDictMethods(
                                nombreParametro)
                            tipoParametrosEnviar.append(tipoMetodo)
                            tipoParametrosEnviarGlobal.append(tipoMetodo)
                        elif(tipoParametroEnviado == "array"):
                            nombreArray = parametrosEnviados[x].location(
                            ).array_id().getText()
                            if("." in nombreArray):  # es una estructura
                                indice = nombreArray.index(".")
                                variableEstructura = nombreArray[0:indice]
                                variableDentroEstructura = nombreArray[indice + 1:len(
                                    nombreArray)]
                                # si la variable que hicimos split o partimos tiene corchete obtenemos solo el nombre
                                if("[" in variableEstructura or "]" in variableEstructura):
                                    indexCorchete = variableEstructura.index(
                                        "[")
                                    variableEstructura = variableEstructura[0: indexCorchete]
                                if("[" in variableDentroEstructura or "]" in variableDentroEstructura):
                                    indexCorchete = variableDentroEstructura.index(
                                        "[")
                                    variableDentroEstructura = variableDentroEstructura[0: indexCorchete]
                                # si tenemos otro nivel
                                if("." in variableDentroEstructura):
                                    print("anidado")
                                    # obtenemos infromacion de la estructura y d ela variable que estamos apuntando
                                    informacionStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableEstructura, self.scopeActual, False, [])
                                    indice2 = variableDentroEstructura.index(
                                        ".")
                                    variableEstructura2 = variableDentroEstructura[0:indice2]
                                    variableDentroEstructura2 = variableDentroEstructura[indice2 + 1:len(
                                        variableDentroEstructura)]
                                    # obtenemos infromacion de la estructura y d ela variable que estamos apuntando
                                    informacionStruct2 = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableEstructura2, informacionStruct[1], False, [])
                                    informacionInnerVarStruct2 = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableDentroEstructura2, informacionStruct2[1], False, [])
                                    tipoDatoInnerVariable2 = informacionInnerVarStruct2[1]
                                    tipoParametrosEnviar.append(
                                        tipoDatoInnerVariable2)
                                    tipoParametrosEnviarGlobal.append(
                                        tipoDatoInnerVariable2)
                                else:
                                    # probamos si existe la struct
                                    structExists = self.tablaSimbolos.varExistsRecursivo(
                                        variableEstructura, self.scopeActual, False)
                                    if(structExists):
                                        # obtenemos infromacion de la estructura y d ela variable que estamos apuntando
                                        informacionStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                            variableEstructura, self.scopeActual, False, [])
                                        innerVarExists = self.tablaSimbolos.checkVarInVarSymbolTableV2(
                                            variableDentroEstructura, informacionStruct[1])
                                        if(innerVarExists):
                                            informacionInnerVarStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                                variableDentroEstructura, informacionStruct[1], False, [])
                                            tipoDatoInnerVariable = informacionInnerVarStruct[1]
                                            tipoParametrosEnviar.append(
                                                tipoDatoInnerVariable)
                                            tipoParametrosEnviarGlobal.append(
                                                tipoDatoInnerVariable)
                                        else:
                                            print(
                                                f'--> ERROR. La estructura o un valor interno de parámetro enviado no existe "{variableEstructura}" .linea: {ctx.start.line} , columna: {ctx.start.column}')
                                    else:
                                        print(
                                            f'--> ERROR. La estructura de parámetro enviado no existe "{variableEstructura}" .linea: {ctx.start.line} , columna: {ctx.start.column}')
                    # print("TIPOS DAODS ", tipoParametrosEnviar)
                    if(len(parametrosMetodo) != len(tipoParametrosEnviar)):
                        print(
                            f'--> ERROR. El método "{metodoAsignado}" pide un total de {len(parametrosMetodo)} parámetros, pero se están enviando {len(tipoParametrosEnviar)}.linea: {ctx.start.line} , columna: {ctx.start.column}')
                        # exit()
                    for y in range(0, len(parametrosMetodo)):
                        if(tipoParametrosEnviar[y] != ""):
                            if(parametrosMetodo[y] != tipoParametrosEnviar[y]):
                                print(
                                    f'--> ERROR. Un parámetro enviado al método "{metodoAsignado}" no es del mismo tipo REQUERIDO .linea: {ctx.start.line} , columna: {ctx.start.column}')
                                # exit()
                        else:
                            print(
                                f'--> ERROR. Un parámetro enviado al método "{metodoAsignado}" NO ha sido DECLARADO.linea: {ctx.start.line} , columna: {ctx.start.column}')
                            # exit()
                    # revisamos globalmente
                    for y in range(0, len(parametrosMetodo)):
                        if(tipoParametrosEnviarGlobal[y] != ""):
                            if(parametrosMetodo[y] != tipoParametrosEnviarGlobal[y]):
                                print(
                                    f'--> ERROR2. Un parámetro enviado al método "{metodoAsignado}" no es del mismo tipo REQUERIDO .linea: {ctx.start.line} , columna: {ctx.start.column}')
                                # exit()
            # este if es para ver si la llamada a un metodo es sin asignacion, solo normalmente
            elif(mehtodCallNormal != None and mehtodCallNormal != ""):
                metodoAsignado = ctx.method_call().method_call_inter().method_name().getText()
                # verificamos si deberia poder retornar algo
                scope = self.scopeActual
                methodTypeFromTableV2 = self.tablaSimbolos.getTypeMethodDictMethods(
                    metodoAsignado)
                if(methodTypeFromTableV2 == ""):
                    print(
                        f'--> ERRORA2. El método "{metodoAsignado}" NO existe "{name}". linea: {ctx.start.line} , columna: {ctx.start.column}')
                    # exit()
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
                            if(canTryAgain):  # por si es metodo
                                try:
                                    interTry = parametrosEnviados[x].method_call(
                                    ).getText()
                                    tipoParametroEnviado = "metodo"
                                    canTryAgain = False
                                except:
                                    pass
                            if(canTryAgain):  # por si es estructura
                                try:
                                    interTry = parametrosEnviados[x].location(
                                    ).array_id().getText()
                                    tipoParametroEnviado = "array"
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
                            elif(tipoParametroEnviado == "metodo"):
                                nombreParametro = parametrosEnviados[x].method_call(
                                ).getText()
                                if("(" in nombreParametro):
                                    nombreParametro = nombreParametro.replace(
                                        "(", "")
                                if(")" in nombreParametro):
                                    nombreParametro = nombreParametro.replace(
                                        ")", "")
                                # obtenemos el tipo de método
                                tipoMetodo = self.tablaSimbolos.getTypeMethodDictMethods(
                                    nombreParametro)
                                tipoParametrosEnviar.append(tipoMetodo)
                                tipoParametrosEnviarGlobal.append(tipoMetodo)
                            elif(tipoParametroEnviado == "array"):
                                nombreArray = parametrosEnviados[x].location(
                                ).array_id().getText()
                                if("." in nombreArray):  # es una estructura
                                    indice = nombreArray.index(".")
                                    variableEstructura = nombreArray[0:indice]
                                    variableDentroEstructura = nombreArray[indice + 1:len(
                                        nombreArray)]
                                    # si la variable que hicimos split o partimos tiene corchete obtenemos solo el nombre
                                    if("[" in variableEstructura or "]" in variableEstructura):
                                        indexCorchete = variableEstructura.index(
                                            "[")
                                        variableEstructura = variableEstructura[0: indexCorchete]
                                    if("[" in variableDentroEstructura or "]" in variableDentroEstructura):
                                        indexCorchete = variableDentroEstructura.index(
                                            "[")
                                        variableDentroEstructura = variableDentroEstructura[0: indexCorchete]
                                    # si tenemos otro nivel
                                    if("." in variableDentroEstructura):
                                        # obtenemos infromacion de la estructura y d ela variable que estamos apuntando
                                        informacionStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                            variableEstructura, self.scopeActual, False, [])
                                        indice2 = variableDentroEstructura.index(
                                            ".")
                                        variableEstructura2 = variableDentroEstructura[0:indice2]
                                        variableDentroEstructura2 = variableDentroEstructura[indice2 + 1:len(
                                            variableDentroEstructura)]
                                        # obtenemos infromacion de la estructura y d ela variable que estamos apuntando
                                        informacionStruct2 = self.tablaSimbolos.getVarInformationRecursivo(
                                            variableEstructura2, informacionStruct[1], False, [])
                                        informacionInnerVarStruct2 = self.tablaSimbolos.getVarInformationRecursivo(
                                            variableDentroEstructura2, informacionStruct2[1], False, [])
                                        tipoDatoInnerVariable2 = informacionInnerVarStruct2[1]
                                        tipoParametrosEnviar.append(
                                            tipoDatoInnerVariable2)
                                        tipoParametrosEnviarGlobal.append(
                                            tipoDatoInnerVariable2)
                                    else:
                                        # probamos si existe la struct
                                        structExists = self.tablaSimbolos.varExistsRecursivo(
                                            variableEstructura, self.scopeActual, False)
                                        if(structExists):
                                            # obtenemos infromacion de la estructura y d ela variable que estamos apuntando
                                            informacionStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                                variableEstructura, self.scopeActual, False, [])
                                            innerVarExists = self.tablaSimbolos.checkVarInVarSymbolTableV2(
                                                variableDentroEstructura, informacionStruct[1])
                                            if(innerVarExists):
                                                informacionInnerVarStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                                    variableDentroEstructura, informacionStruct[1], False, [])
                                                tipoDatoInnerVariable = informacionInnerVarStruct[1]
                                                tipoParametrosEnviar.append(
                                                    tipoDatoInnerVariable)
                                                tipoParametrosEnviarGlobal.append(
                                                    tipoDatoInnerVariable)
                                            else:
                                                print(
                                                    f'--> ERROR. La estructura o un valor interno de parámetro enviado no existe "{variableEstructura}" .linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        else:
                                            print(
                                                f'--> ERROR. La estructura de parámetro enviado no existe "{variableEstructura}" .linea: {ctx.start.line} , columna: {ctx.start.column}')
                    # print("TIPOS DAODS ", tipoParametrosEnviar)
                    if(len(parametrosMetodo) != len(tipoParametrosEnviar)):
                        print(
                            f'--> ERROR22. El método "{metodoAsignado}" pide un total de {len(parametrosMetodo)} parámetros, pero se están enviando {len(tipoParametrosEnviar)}.linea: {ctx.start.line} , columna: {ctx.start.column}')
                        # exit()
                    # Reviosamos localmente
                    for y in range(0, len(parametrosMetodo)):
                        if(tipoParametrosEnviar[y] != ""):
                            if(parametrosMetodo[y] != tipoParametrosEnviar[y]):
                                print(
                                    f'--> ERROR1. Un parámetro enviado al método "{metodoAsignado}" no es del mismo tipo REQUERIDO .linea: {ctx.start.line} , columna: {ctx.start.column}')
                                # exit()
                    # revisamos globalmente
                    for y in range(0, len(parametrosMetodo)):
                        if(tipoParametrosEnviarGlobal[y] != ""):
                            if(parametrosMetodo[y] != tipoParametrosEnviarGlobal[y]):
                                print(
                                    f'--> ERROR2. Un parámetro enviado al método "{metodoAsignado}" no es del mismo tipo REQUERIDO .linea: {ctx.start.line} , columna: {ctx.start.column}')
                                # exit()

            else:
                if(ctx.IF() or ctx.WHILE()):
                    self.conteoIfs += 1
                    scopeNuevo = ""
                    if(ctx.IF()):
                        scopeNuevo = 'if'+str(self.conteoIfs)
                    elif(ctx.WHILE()):
                        scopeNuevo = 'while'+str(self.conteoIfs)
                    self.scopeAnterior = self.scopeActual
                    self.scopeActual = scopeNuevo
                    # print("scope antes LUEGO  IF o WHILE", self.scopeActual)
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
                            f'--> ERROR. En una condicion, deben darse valores booleanos "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                        # exit()
                    # agregamos el nuevo if como metodo
                    self.tablaSimbolos.AddNewMethod_DictMethod(
                        "", scopeNuevo, [], False, self.scopeAnterior)
                    # variables de EQ_OPS
                    arraySplitEqOps = []
                    # variables de cond OPS
                    arraySplitCondOps = []
                    # variable para RelOPS
                    arraySplitRelOps = []
                    if((tipoVariableEqOps == "==" or tipoVariableEqOps == "!=")
                            and tipoVariablecondOps == "" and tipoVariableRelOps == ""):
                        # hacemos split de cada valor y vamos a buscarlo
                        arraySplitEqOps = ctx.expr().getText().split(tipoVariableEqOps)
                        valor1 = arraySplitEqOps[0]
                        valor2 = arraySplitEqOps[1]
                        # si lo que tenemos tiene un valor de estructura
                        variableEstructura1 = ""
                        variableDentroEstructura1 = ""
                        variableEstructura2 = ""
                        variableDentroEstructura2 = ""
                        if("." in valor1):
                            indice = valor1.index(".")
                            variableEstructura1 = valor1[0:indice]
                            variableDentroEstructura1 = valor1[indice +
                                                               1:len(valor1)]
                        if("." in valor2):
                            indice = valor2.index(".")
                            variableEstructura2 = valor2[0:indice]
                            variableDentroEstructura2 = valor2[indice +
                                                               1:len(valor2)]
                        # si la variable que hicimos split o partimos tiene corchete obtenemos solo el nombre
                        if("[" in variableEstructura1 or "]" in variableEstructura1):
                            indexCorchete = variableEstructura1.index("[")
                            variableEstructura1 = variableEstructura1[0: indexCorchete]
                        if("[" in variableDentroEstructura1 or "]" in variableDentroEstructura1):
                            indexCorchete = variableDentroEstructura1.index(
                                "[")
                            variableDentroEstructura1 = variableDentroEstructura1[0: indexCorchete]
                        if("[" in variableEstructura2 or "]" in variableEstructura2):
                            indexCorchete = variableEstructura2.index("[")
                            variableEstructura2 = variableEstructura2[0: indexCorchete]
                        if("[" in variableDentroEstructura2 or "]" in variableDentroEstructura2):
                            indexCorchete = variableDentroEstructura2.index(
                                "[")
                            variableDentroEstructura2 = variableDentroEstructura2[0: indexCorchete]

                        varExists3 = ""
                        varExists4 = ""
                        varInformation = []
                        for x in arraySplitEqOps:
                            if((valor2 == "true" or valor2 == "false") and (valor1 != "true" and valor1 != "false")):
                                if("." in valor1):
                                    # obtenemos infromacion de la estructura y de la variable que estamos apuntando
                                    informacionStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableEstructura1, self.scopeActual, False, [])
                                    # obtenemos la información de la variable DENTRO de la estructura
                                    informacionInnerVarStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableDentroEstructura1, informacionStruct[1], False, [])
                                    # obtenemos el tipo de dato
                                    varTypeInterno = informacionInnerVarStruct[1]
                                    if(varTypeInterno != "boolean"):
                                        print(
                                            f'--> ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                else:
                                    varExists3 = self.tablaSimbolos.varExistsRecursivo(
                                        valor1, self.scopeActual, False)
                                    if(varExists3 == False):
                                        print(
                                            f'--> ERROR. La variable {valor1} NO ha sido declarada o no es valida "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
                                    else:
                                        varInformation = self.tablaSimbolos.getVarInformationRecursivo(
                                            valor1, self.scopeActual, False, [])
                                        # el tipo de variable
                                        varTypeInterno = varInformation[1]
                                        if(varTypeInterno != "boolean"):
                                            print(
                                                f'--> ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()
                            elif((valor1 == "true" or valor1 == "false") and (valor2 != "true" and valor2 != "false")):
                                if("." in valor2):
                                    # obtenemos infromacion de la estructura y de la variable que estamos apuntando
                                    informacionStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableEstructura2, self.scopeActual, False, [])
                                    # obtenemos la información de la variable DENTRO de la estructura
                                    informacionInnerVarStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableDentroEstructura2, informacionStruct[1], False, [])
                                    # obtenemos el tipo de dato
                                    varTypeInterno = informacionInnerVarStruct[1]
                                    if(varTypeInterno != "boolean"):
                                        print(
                                            f'--> ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                else:
                                    varExists3 = self.tablaSimbolos.varExistsRecursivo(
                                        valor2, self.scopeActual, False)
                                    if(varExists3 == False):
                                        print(
                                            f'--> ERROR. La variable {valor2} NO ha sido declarada o no es valida "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
                                    else:
                                        varInformation = self.tablaSimbolos.getVarInformationRecursivo(
                                            valor2, self.scopeActual, False, [])
                                        # el tipo de variable
                                        varTypeInterno = varInformation[1]
                                        if(varTypeInterno != "boolean"):
                                            print(
                                                f'--> ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()
                            elif(self.functions.checkIfIsInt(valor1) and self.functions.checkIfIsInt(valor2) == False):
                                if("." in valor2):
                                    # obtenemos infromacion de la estructura y de la variable que estamos apuntando
                                    informacionStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableEstructura2, self.scopeActual, False, [])
                                    # obtenemos la información de la variable DENTRO de la estructura
                                    informacionInnerVarStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableDentroEstructura2, informacionStruct[1], False, [])
                                    # obtenemos el tipo de dato
                                    varTypeInterno = informacionInnerVarStruct[1]
                                    if(varTypeInterno != "int"):
                                        print(
                                            f'--> ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                else:
                                    varExists3 = self.tablaSimbolos.varExistsRecursivo(
                                        valor2, self.scopeActual, False)
                                    if(varExists3 == False):
                                        print(
                                            f'--> ERROR. La variable {valor2} NO ha sido declarada o no es valida "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
                                    else:
                                        varInformation = self.tablaSimbolos.getVarInformationRecursivo(
                                            valor2, self.scopeActual, False, [])
                                        # el tipo de variable
                                        varTypeInterno = varInformation[1]
                                        if(varTypeInterno != "int"):
                                            print(
                                                f'--> ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()
                            elif(self.functions.checkIfIsInt(valor2) and (self.functions.checkIfIsInt(valor1) == False)):
                                if("." in valor1):
                                    # obtenemos infromacion de la estructura y de la variable que estamos apuntando
                                    informacionStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableEstructura1, self.scopeActual, False, [])
                                    # obtenemos la información de la variable DENTRO de la estructura
                                    informacionInnerVarStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableDentroEstructura1, informacionStruct[1], False, [])
                                    # obtenemos el tipo de dato
                                    varTypeInterno = informacionInnerVarStruct[1]
                                    if(varTypeInterno != "int"):
                                        print(
                                            f'--> ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                else:
                                    varExists3 = self.tablaSimbolos.varExistsRecursivo(
                                        valor1, self.scopeActual, False)
                                    if(varExists3 == False):
                                        print(
                                            f'--> ERROR33. La variable {valor1} NO ha sido declarada o no es valida "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
                                    else:
                                        varInformation = self.tablaSimbolos.getVarInformationRecursivo(
                                            valor1, self.scopeActual, False, [])
                                        # el tipo de variable
                                        varTypeInterno = varInformation[1]
                                        if(varTypeInterno != "int"):
                                            print(
                                                f'--> ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()
                            elif(self.functions.checkGeneraltype(valor1, "string") and self.functions.checkGeneraltype(valor2, "string") == False):
                                if("." in valor2):
                                    # obtenemos infromacion de la estructura y de la variable que estamos apuntando
                                    informacionStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableEstructura2, self.scopeActual, False, [])
                                    # obtenemos la información de la variable DENTRO de la estructura
                                    informacionInnerVarStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableDentroEstructura2, informacionStruct[1], False, [])
                                    # obtenemos el tipo de dato
                                    varTypeInterno = informacionInnerVarStruct[1]
                                    if(varTypeInterno != "string"):
                                        print(
                                            f'--> ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                else:
                                    varExists3 = self.tablaSimbolos.varExistsRecursivo(
                                        valor2, self.scopeActual, False)
                                    if(varExists3 == False):
                                        print(
                                            f'--> ERROR. La variable {valor2} NO ha sido declarada o no es valida "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
                                    else:
                                        varInformation = self.tablaSimbolos.getVarInformationRecursivo(
                                            valor2, self.scopeActual, False, [])
                                        # el tipo de variable
                                        varTypeInterno = varInformation[1]
                                        if(varTypeInterno != "string"):
                                            print(
                                                f'--> ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()
                            elif(self.functions.checkGeneraltype(valor2, "string") and self.functions.checkGeneraltype(valor1, "string") == False):
                                if("." in valor1):
                                    # obtenemos infromacion de la estructura y de la variable que estamos apuntando
                                    informacionStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableEstructura1, self.scopeActual, False, [])
                                    # obtenemos la información de la variable DENTRO de la estructura
                                    informacionInnerVarStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableDentroEstructura1, informacionStruct[1], False, [])
                                    # obtenemos el tipo de dato
                                    varTypeInterno = informacionInnerVarStruct[1]
                                    if(varTypeInterno != "string"):
                                        print(
                                            f'--> ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                else:
                                    varExists3 = self.tablaSimbolos.varExistsRecursivo(
                                        valor1, self.scopeActual, False)
                                    if(varExists3 == False):
                                        print(
                                            f'--> ERROR. La variable {valor1} NO ha sido declarada o no es valida "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
                                    else:
                                        varInformation = self.tablaSimbolos.getVarInformationRecursivo(
                                            valor1, self.scopeActual, False, [])
                                        # el tipo de variable
                                        varTypeInterno = varInformation[1]
                                        if(varTypeInterno != "string"):
                                            print(
                                                f'--> ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()
                            # condicion por si ambas son dle mismo valor, hacemos PASS
                            elif((valor2 == "true" or valor2 == "false") and (valor1 == "true" or valor1 == "false")):
                                pass
                            elif(self.functions.checkIfIsInt(valor2) and self.functions.checkIfIsInt(valor1)):
                                pass
                            elif(self.functions.checkGeneraltype(valor2, "string") and self.functions.checkGeneraltype(valor1, "string")):
                                pass
                            else:
                                varTypeInterno1 = ""
                                varTypeInterno2 = ""
                                if("." in valor1):
                                    # obtenemos infromacion de la estructura y de la variable que estamos apuntando
                                    informacionStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableEstructura1, self.scopeActual, False, [])
                                    # obtenemos la información de la variable DENTRO de la estructura
                                    informacionInnerVarStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableDentroEstructura1, informacionStruct[1], False, [])
                                    # obtenemos el tipo de dato
                                    varTypeInterno1 = informacionInnerVarStruct[1]
                                    # verificamos la otra variable
                                    varExists3 = self.tablaSimbolos.varExistsRecursivo(
                                        valor1, self.scopeActual, False)
                                    if(varExists3 == False):
                                        print(
                                            f'--> ERROR. Una variable no ha sido declarada en una condicion "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
                                    else:
                                        varInformation2 = self.tablaSimbolos.getVarInformationRecursivo(
                                            valor2, self.scopeActual, False, [])
                                        varTypeInterno2 = varInformation2[1]
                                        if(varTypeInterno1 != varTypeInterno2):
                                            print(
                                                f'--> ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()
                                elif("." in valor2):
                                    # obtenemos infromacion de la estructura y de la variable que estamos apuntando
                                    informacionStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableEstructura2, self.scopeActual, False, [])
                                    # obtenemos la información de la variable DENTRO de la estructura
                                    informacionInnerVarStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableDentroEstructura2, informacionStruct[1], False, [])
                                    # obtenemos el tipo de dato
                                    varTypeInterno2 = informacionInnerVarStruct[1]
                                    # verificamos la otra variable
                                    varExists3 = self.tablaSimbolos.varExistsRecursivo(
                                        valor2, self.scopeActual, False)
                                    if(varExists3 == False):
                                        print(
                                            f'--> ERROR. Una variable no ha sido declarada en una condicion "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
                                    else:
                                        varInformation1 = self.tablaSimbolos.getVarInformationRecursivo(
                                            valor1, self.scopeActual, False, [])
                                        varTypeInterno1 = varInformation1[1]
                                        if(varTypeInterno1 != varTypeInterno2):
                                            print(
                                                f'--> ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()
                                else:
                                    # verificamos ambas variables
                                    varExists3 = self.tablaSimbolos.varExistsRecursivo(
                                        valor1, self.scopeActual, False)
                                    varExists4 = self.tablaSimbolos.varExistsRecursivo(
                                        valor2, self.scopeActual, False)
                                    if(varExists3 == True and varExists4 == False):
                                        print(
                                            f'--> ERROR. Una variable no ha sido declarada en una condicion "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
                                    elif(varExists3 == False and varExists4 == True):
                                        print(
                                            f'--> ERROR. Una variable no ha sido declarada en una condicion "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
                                    elif(varExists3 == False and varExists4 == False):
                                        print(
                                            f'--> ERROR. Una variable no ha sido declarada en una condicion "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
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
                                                f'--> ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()
                                # variables de  cond_OPS
                    if((tipoVariablecondOps == "&&" or tipoVariablecondOps == "||")
                            and tipoVariableEqOps == "" and tipoVariableRelOps == ""):
                        print("variable condOps")
                        # hacemos split de cada valor y vamos a buscarlo
                        arraySplitCondOps = ctx.expr().getText().split(tipoVariablecondOps)
                        valor1 = arraySplitCondOps[0]
                        valor2 = arraySplitCondOps[1]
                        # si lo que tenemos tiene un valor de estructura
                        variableEstructura1 = ""
                        variableDentroEstructura1 = ""
                        variableEstructura2 = ""
                        variableDentroEstructura2 = ""
                        if("." in valor1):
                            indice = valor1.index(".")
                            variableEstructura1 = valor1[0:indice]
                            variableDentroEstructura1 = valor1[indice +
                                                               1:len(valor1)]
                        if("." in valor2):
                            indice = valor2.index(".")
                            variableEstructura2 = valor2[0:indice]
                            variableDentroEstructura2 = valor2[indice +
                                                               1:len(valor2)]
                        # si la variable que hicimos split o partimos tiene corchete obtenemos solo el nombre
                        if("[" in variableEstructura1 or "]" in variableEstructura1):
                            indexCorchete = variableEstructura1.index("[")
                            variableEstructura1 = variableEstructura1[0: indexCorchete]
                        if("[" in variableDentroEstructura1 or "]" in variableDentroEstructura1):
                            indexCorchete = variableDentroEstructura1.index(
                                "[")
                            variableDentroEstructura1 = variableDentroEstructura1[0: indexCorchete]
                        if("[" in variableEstructura2 or "]" in variableEstructura2):
                            indexCorchete = variableEstructura2.index("[")
                            variableEstructura2 = variableEstructura2[0: indexCorchete]
                        if("[" in variableDentroEstructura2 or "]" in variableDentroEstructura2):
                            indexCorchete = variableDentroEstructura2.index(
                                "[")
                            variableDentroEstructura2 = variableDentroEstructura2[0: indexCorchete]

                        varExistsValor1 = ""
                        varExistsValor2 = ""
                        for x in arraySplitCondOps:
                            if((valor2 == "true" or valor2 == "false") and (valor1 != "true" and valor1 != "false")):
                                if("." in valor1):
                                    # obtenemos infromacion de la estructura y de la variable que estamos apuntando
                                    informacionStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableEstructura1, self.scopeActual, False, [])
                                    # obtenemos la información de la variable DENTRO de la estructura
                                    informacionInnerVarStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableDentroEstructura1, informacionStruct[1], False, [])
                                    # obtenemos el tipo de dato
                                    varTypeInterno = informacionInnerVarStruct[1]
                                    if(varTypeInterno != "boolean"):
                                        print(
                                            f'--> ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                else:
                                    varExistsValor1 = self.tablaSimbolos.varExistsRecursivo(
                                        valor1, self.scopeActual, False)
                                    if(varExistsValor1 == False):
                                        print(
                                            f'--> ERROR. La variable {valor1} NO ha sido declarada o no es valida "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
                                    else:
                                        varInformation = self.tablaSimbolos.getVarInformationRecursivo(
                                            valor1, self.scopeActual, False, [])
                                        # el tipo de variable
                                        varTypeInterno = varInformation[1]
                                        if(varTypeInterno != "boolean"):
                                            print(
                                                f'--> ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()
                            elif((valor1 == "true" or valor1 == "false") and (valor2 != "true" and valor2 != "false")):
                                if("." in valor2):
                                    # obtenemos infromacion de la estructura y de la variable que estamos apuntando
                                    informacionStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableEstructura2, self.scopeActual, False, [])
                                    # obtenemos la información de la variable DENTRO de la estructura
                                    informacionInnerVarStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableDentroEstructura2, informacionStruct[1], False, [])
                                    # obtenemos el tipo de dato
                                    varTypeInterno = informacionInnerVarStruct[1]
                                    if(varTypeInterno != "boolean"):
                                        print(
                                            f'--> ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                else:
                                    varExistsValor1 = self.tablaSimbolos.varExistsRecursivo(
                                        valor2, self.scopeActual, False)
                                    if(varExistsValor1 == False):
                                        print(
                                            f'--> ERROR. La variable {valor2} NO ha sido declarada o no es valida "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
                                    else:
                                        varInformation = self.tablaSimbolos.getVarInformationRecursivo(
                                            valor2, self.scopeActual, False, [])
                                        # el tipo de variable
                                        varTypeInterno = varInformation[1]
                                        if(varTypeInterno != "boolean"):
                                            print(
                                                f'--> ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()
                            elif(self.functions.checkIfIsInt(valor1)):
                                print(
                                    f'--> ERROR. La variable "{valor1}" es INT pero debe ser del tipo "BOOLEAN" "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                # exit()
                            elif(self.functions.checkIfIsInt(valor2)):
                                print(
                                    f'--> ERROR. La variable "{valor2}" es INT pero debe ser del tipo "BOOLEAN" "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                # exit()
                            elif(self.functions.checkGeneraltype(valor1, "string")):
                                print(
                                    f'--> ERROR. La variable "{valor1}" es STRING pero debe ser del tipo "BOOLEAN" "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                # exit()
                            elif(self.functions.checkGeneraltype(valor2, "string")):
                                print(
                                    f'--> ERROR. La variable "{valor2}" es STRING pero debe ser del tipo "BOOLEAN" "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                # exit()
                            # condicion por si ambas son dle mismo valor, hacemos PASS
                            elif((valor2 == "true" or valor2 == "false") and (valor1 == "true" or valor1 == "false")):
                                pass
                            elif(self.functions.checkIfIsInt(valor2) and self.functions.checkIfIsInt(valor1)):
                                pass
                            elif(self.functions.checkGeneraltype(valor2, "string") and self.functions.checkGeneraltype(valor1, "string")):
                                pass
                            else:
                                varTypeInterno1 = ""
                                varTypeInterno2 = ""
                                if("." in valor1):
                                    # obtenemos infromacion de la estructura y de la variable que estamos apuntando
                                    informacionStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableEstructura1, self.scopeActual, False, [])
                                    # obtenemos la información de la variable DENTRO de la estructura
                                    informacionInnerVarStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableDentroEstructura1, informacionStruct[1], False, [])
                                    # obtenemos el tipo de dato
                                    varTypeInterno1 = informacionInnerVarStruct[1]
                                    # verificamos la otra variable
                                    varExists3 = self.tablaSimbolos.varExistsRecursivo(
                                        valor2, self.scopeActual, False)
                                    if(varExists3 == False):
                                        print(
                                            f'--> ERROR. Una variable no ha sido declarada en una condicion "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
                                    else:
                                        varInformation2 = self.tablaSimbolos.getVarInformationRecursivo(
                                            valor2, self.scopeActual, False, [])
                                        varTypeInterno2 = varInformation2[1]

                                        if(varTypeInterno1 != "boolean" or varTypeInterno2 != "boolean"):
                                            print(
                                                f'--> ERROR. En una condicion, ambas variables deben ser del tipo BOOLEAN "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()
                                        elif(varTypeInterno1 == "boolean" and varTypeInterno2 == "boolean"):
                                            pass
                                        else:
                                            print(
                                                f'--> ERROR. En una condicion, ambas variables deben ser del tipo BOOLEAN "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()
                                elif("." in valor2):
                                    # obtenemos infromacion de la estructura y de la variable que estamos apuntando
                                    informacionStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableEstructura2, self.scopeActual, False, [])
                                    # obtenemos la información de la variable DENTRO de la estructura
                                    informacionInnerVarStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableDentroEstructura2, informacionStruct[1], False, [])
                                    # obtenemos el tipo de dato
                                    varTypeInterno2 = informacionInnerVarStruct[1]
                                    # verificamos la otra variable
                                    varExists3 = self.tablaSimbolos.varExistsRecursivo(
                                        valor2, self.scopeActual, False)
                                    if(varExists3 == False):
                                        print(
                                            f'--> ERROR. Una variable no ha sido declarada en una condicion "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
                                    else:
                                        varInformation1 = self.tablaSimbolos.getVarInformationRecursivo(
                                            valor1, self.scopeActual, False, [])
                                        varTypeInterno1 = varInformation1[1]
                                        if(varTypeInterno1 != "boolean" or varTypeInterno2 != "boolean"):
                                            print(
                                                f'--> ERROR. En una condicion, ambas variables deben ser del tipo BOOLEAN "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()
                                        elif(varTypeInterno1 == "boolean" and varTypeInterno2 == "boolean"):
                                            pass
                                        else:
                                            print(
                                                f'--> ERROR. En una condicion, ambas variables deben ser del tipo BOOLEAN "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()
                                else:
                                    # verificamos ambas variables
                                    varExistsValor1 = self.tablaSimbolos.varExistsRecursivo(
                                        valor1, self.scopeActual, False)
                                    varExistsValor2 = self.tablaSimbolos.varExistsRecursivo(
                                        valor2, self.scopeActual, False)
                                    if(varExistsValor1 == True and varExistsValor2 == False):
                                        print(
                                            f'--> ERROR. Una variable no ha sido declarada en una condicion "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
                                    elif(varExistsValor1 == False and varExistsValor2 == True):
                                        print(
                                            f'--> ERROR. Una variable no ha sido declarada en una condicion "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
                                    elif(varExistsValor1 == False and varExistsValor2 == False):
                                        print(
                                            f'--> ERROR. Una variable no ha sido declarada en una condicion "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
                                    elif(varExistsValor1 == True and varExistsValor2 == True):
                                        varInformation1 = self.tablaSimbolos.getVarInformationRecursivo(
                                            valor1, self.scopeActual, False, [])
                                        varInformation2 = self.tablaSimbolos.getVarInformationRecursivo(
                                            valor2, self.scopeActual, False, [])
                                        # el tipo de variable
                                        varTypeInterno1 = varInformation1[1]
                                        varTypeInterno2 = varInformation2[1]
                                        if(varTypeInterno1 != "boolean" or varTypeInterno2 != "boolean"):
                                            print(
                                                f'--> ERROR. En una condicion, ambas variables deben ser del tipo BOOLEAN "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()
                                        elif(varTypeInterno1 == "boolean" and varTypeInterno2 == "boolean"):
                                            pass
                                        else:
                                            print(
                                                f'--> ERROR. En una condicion, ambas variables deben ser del tipo BOOLEAN "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()

                    # variables de REL_OPS
                    elif((tipoVariableRelOps == "<" or tipoVariableRelOps == "<=" or
                          tipoVariableRelOps == ">" or tipoVariableRelOps == ">=")
                            and tipoVariableEqOps == "" and tipoVariablecondOps == ""):
                        arraySplitRelOps = ctx.expr().getText().split(tipoVariableRelOps)
                        valor1 = arraySplitRelOps[0]
                        valor2 = arraySplitRelOps[1]
                        # si lo que tenemos tiene un valor de estructura
                        variableEstructura1 = ""
                        variableDentroEstructura1 = ""
                        variableEstructura2 = ""
                        variableDentroEstructura2 = ""
                        if("." in valor1):
                            indice = valor1.index(".")
                            variableEstructura1 = valor1[0:indice]
                            variableDentroEstructura1 = valor1[indice +
                                                               1:len(valor1)]
                        if("." in valor2):
                            indice = valor2.index(".")
                            variableEstructura2 = valor2[0:indice]
                            variableDentroEstructura2 = valor2[indice +
                                                               1:len(valor1)]
                        # si la variable que hicimos split o partimos tiene corchete obtenemos solo el nombre
                        if("[" in variableEstructura1 or "]" in variableEstructura1):
                            indexCorchete = variableEstructura1.index("[")
                            variableEstructura1 = variableEstructura1[0: indexCorchete]
                        if("[" in variableDentroEstructura1 or "]" in variableDentroEstructura1):
                            indexCorchete = variableDentroEstructura1.index(
                                "[")
                            variableDentroEstructura1 = variableDentroEstructura1[0: indexCorchete]
                        if("[" in variableEstructura2 or "]" in variableEstructura2):
                            indexCorchete = variableEstructura2.index("[")
                            variableEstructura2 = variableEstructura2[0: indexCorchete]
                        if("[" in variableDentroEstructura2 or "]" in variableDentroEstructura2):
                            indexCorchete = variableDentroEstructura2.index(
                                "[")
                            variableDentroEstructura2 = variableDentroEstructura2[0: indexCorchete]

                        varExistsValor1 = ""
                        varExistsValor2 = ""
                        for x in arraySplitRelOps:
                            if(self.functions.checkIfIsInt(valor1) and self.functions.checkIfIsInt(valor2) == False):
                                if("." in valor2):
                                    # obtenemos infromacion de la estructura y de la variable que estamos apuntando
                                    informacionStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableEstructura2, self.scopeActual, False, [])
                                    # obtenemos la información de la variable DENTRO de la estructura
                                    informacionInnerVarStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableDentroEstructura2, informacionStruct[1], False, [])
                                    # obtenemos el tipo de dato
                                    varTypeInterno = informacionInnerVarStruct[1]
                                    if(varTypeInterno != "int"):
                                        print(
                                            f'--> ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                else:
                                    varExists3 = self.tablaSimbolos.varExistsRecursivo(
                                        valor2, self.scopeActual, False)
                                    if(varExists3 == False):
                                        print(
                                            f'--> ERROR. La variable {valor2} NO ha sido declarada o no es valida "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
                                    else:
                                        varInformation = self.tablaSimbolos.getVarInformationRecursivo(
                                            valor2, self.scopeActual, False, [])
                                        # el tipo de variable
                                        varTypeInterno = varInformation[1]
                                        if(varTypeInterno != "int"):
                                            print(
                                                f'--> ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()
                            elif(self.functions.checkIfIsInt(valor2) and (self.functions.checkIfIsInt(valor1) == False)):
                                if("." in valor1):
                                    # obtenemos infromacion de la estructura y de la variable que estamos apuntando
                                    informacionStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableEstructura1, self.scopeActual, False, [])
                                    # obtenemos la información de la variable DENTRO de la estructura
                                    informacionInnerVarStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableDentroEstructura1, informacionStruct[1], False, [])
                                    # obtenemos el tipo de dato
                                    varTypeInterno = informacionInnerVarStruct[1]
                                    if(varTypeInterno != "int"):
                                        print(
                                            f'--> ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                else:
                                    varExists3 = self.tablaSimbolos.varExistsRecursivo(
                                        valor1, self.scopeActual, False)
                                    if(varExists3 == False):
                                        print(
                                            f'--> ERROR. La variable {valor1} NO ha sido declarada o no es valida "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
                                    else:
                                        varInformation = self.tablaSimbolos.getVarInformationRecursivo(
                                            valor1, self.scopeActual, False, [])
                                        # el tipo de variable
                                        varTypeInterno = varInformation[1]
                                        if(varTypeInterno != "int"):
                                            print(
                                                f'--> ERROR. En una condicion, ambas variables deben ser del mismo tipo "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()
                            elif(valor2 == "true" or valor2 == "false"):
                                print(
                                    f'--> ERROR. La variable "{valor2}" es BOOLEAN pero debe ser del tipo "INT" "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                # exit()
                            elif(valor1 == "true" or valor1 == "false"):
                                print(
                                    f'--> ERROR. La variable "{valor1}" es BOOLEAN pero debe ser del tipo "INT" "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                # exit()
                            elif(self.functions.checkGeneraltype(valor1, "string")):
                                print(
                                    f'--> ERROR. La variable "{valor1}" es STRING pero debe ser del tipo "INT" "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                # exit()
                            elif(self.functions.checkGeneraltype(valor2, "string")):
                                print(
                                    f'--> ERROR. La variable "{valor2}" es STRING pero debe ser del tipo "INT" "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                # exit()
                            # condicion por si ambas son dle mismo valor, hacemos PASS
                            elif(self.functions.checkIfIsInt(valor2) and self.functions.checkIfIsInt(valor1)):
                                pass
                            else:
                                varTypeInterno1 = ""
                                varTypeInterno2 = ""
                                if("." in valor1):
                                    # obtenemos infromacion de la estructura y de la variable que estamos apuntando
                                    informacionStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableEstructura1, self.scopeActual, False, [])
                                    # obtenemos la información de la variable DENTRO de la estructura
                                    informacionInnerVarStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableDentroEstructura1, informacionStruct[1], False, [])
                                    # obtenemos el tipo de dato
                                    varTypeInterno1 = informacionInnerVarStruct[1]
                                    # verificamos la otra variable
                                    varExists3 = self.tablaSimbolos.varExistsRecursivo(
                                        valor2, self.scopeActual, False)
                                    if(varExists3 == False):
                                        print(
                                            f'--> ERROR. Una variable no ha sido declarada en una condicion "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
                                    else:
                                        varInformation2 = self.tablaSimbolos.getVarInformationRecursivo(
                                            valor2, self.scopeActual, False, [])
                                        varTypeInterno2 = varInformation2[1]

                                        if(varTypeInterno1 != "int" or varTypeInterno2 != "int"):
                                            print(
                                                f'--> ERROR. En una condicion de relación, ambas variables deben ser del tipo int "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()
                                        elif(varTypeInterno1 == "int" and varTypeInterno2 == "int"):
                                            pass
                                        else:
                                            print(
                                                f'--> ERROR. En una condicion de relación, ambas variables deben ser del tipo int "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()
                                elif("." in valor2):
                                    # obtenemos infromacion de la estructura y de la variable que estamos apuntando
                                    informacionStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableEstructura2, self.scopeActual, False, [])
                                    # obtenemos la información de la variable DENTRO de la estructura
                                    informacionInnerVarStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableDentroEstructura2, informacionStruct[1], False, [])
                                    # obtenemos el tipo de dato
                                    varTypeInterno2 = informacionInnerVarStruct[1]
                                    # verificamos la otra variable
                                    varExists3 = self.tablaSimbolos.varExistsRecursivo(
                                        valor2, self.scopeActual, False)
                                    if(varExists3 == False):
                                        print(
                                            f'--> ERROR. Una variable no ha sido declarada en una condicion "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
                                    else:
                                        varInformation1 = self.tablaSimbolos.getVarInformationRecursivo(
                                            valor1, self.scopeActual, False, [])
                                        varTypeInterno1 = varInformation1[1]
                                        if(varTypeInterno1 != "int" or varTypeInterno2 != "int"):
                                            print(
                                                f'--> ERROR. En una condicion de relación, ambas variables deben ser del tipo int "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()
                                        elif(varTypeInterno1 == "int" and varTypeInterno2 == "int"):
                                            pass
                                        else:
                                            print(
                                                f'--> ERROR. En una condicion de relación, ambas variables deben ser del tipo int "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()
                                else:
                                    # verificamos ambas variables
                                    varExistsValor1 = self.tablaSimbolos.varExistsRecursivo(
                                        valor1, self.scopeActual, False)
                                    varExistsValor2 = self.tablaSimbolos.varExistsRecursivo(
                                        valor2, self.scopeActual, False)
                                    if(varExistsValor1 == True and varExistsValor2 == False):
                                        print(
                                            f'--> ERROR. Una variable no ha sido declarada en una condicion "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
                                    elif(varExistsValor1 == False and varExistsValor2 == True):
                                        print(
                                            f'--> ERROR. Una variable no ha sido declarada en una condicion "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
                                    elif(varExistsValor1 == False and varExistsValor2 == False):
                                        print(
                                            f'--> ERROR. Una variable no ha sido declarada en una condicion "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
                                    elif(varExistsValor1 == True and varExistsValor2 == True):
                                        varInformation1 = self.tablaSimbolos.getVarInformationRecursivo(
                                            valor1, self.scopeActual, False, [])
                                        varInformation2 = self.tablaSimbolos.getVarInformationRecursivo(
                                            valor2, self.scopeActual, False, [])
                                        # el tipo de variable
                                        varTypeInterno1 = varInformation1[1]
                                        varTypeInterno2 = varInformation2[1]
                                        if(varTypeInterno1 != "int" or varTypeInterno2 != "int"):
                                            print(
                                                f'--> ERROR. En una condicion de relación, ambas variables deben ser del tipo int "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()
                                        elif(varTypeInterno1 == "int" and varTypeInterno2 == "int"):
                                            pass
                                        else:
                                            print(
                                                f'--> ERROR. En una condicion de relación, ambas variables deben ser del tipo INT "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()

                elif(ctx.assign_op().EQUAL_OP()):  # logica cuando asignamos del lado derecho
                    valorAsignado = ctx.expr().getText()
                    expresionEntera = ctx.expr().getText()
                    splitHijos = []
                    splitHijos = self.functions.removeOperations(
                        expresionEntera)
                    scope = self.scopeActual
                    if("+" in valorAsignado or "-" in valorAsignado or "/" in valorAsignado or "*" in valorAsignado or "%" in valorAsignado):
                        # sabiendoq ue hay operaciones del lado derecho
                        for x in splitHijos:
                            # o variable, o numero u operador
                            hijo = x
                            # verificamos si es int
                            if(not "+" in hijo and not "-" in hijo and not "/" in hijo and not "*" in hijo and not "%" in hijo):
                                if(self.functions.checkIfIsInt(hijo) == False):
                                    varExists = self.tablaSimbolos.varExistsRecursivo(
                                        hijo, scope, False)
                                    if(varExists):
                                        informationHijo = self.tablaSimbolos.getVarInformationRecursivo(
                                            hijo, scope, False, [])
                                        if(informationHijo[1] != "int"):
                                            print(
                                                f'--> ERROR_DECLARACION. La variable o valor "{hijo}" NO es del tipo INT. linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            # exit()
                                    else:
                                        print(
                                            f'--> ERROR_DECLARACION. La variable o valor "{hijo}" NO existe o es no puede ser usado en una operacion aritmética. linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        # exit()
                    nameVariableV2 = ""
                    try:
                        nameVariableV2 = ctx.location().getText()  # el nombre de la variable
                    except:
                        pass
                    line = ctx.start.line
                    column = ctx.start.column
                    scope = self.scopeActual
                    arrayinformation = []
                    hasAnotherSon = False
                    try:
                        innerLocation = ctx.location().location()
                        if(innerLocation != None):
                            hasAnotherSon = True
                    except:
                        pass
                    if("+" in valorAsignado or "-" in valorAsignado or "/" in valorAsignado or "*" in valorAsignado or "%" in valorAsignado):
                        pass
                    else:
                        if(hasAnotherSon):
                            print("LOGICA para 2 hijos ")
                        elif(hasAnotherSon == False):  # lógica para un valor del lado derecho UNICO
                            if("." not in nameVariableV2):  # si no es una structura del lado izquierdo
                                # verificamos si la variable o valor existe pero una variable no estructura
                                variableAsignadaExiste = self.tablaSimbolos.varExistsRecursivo(
                                    nameVariableV2, scope, False)
                                if(variableAsignadaExiste == True):
                                    tipoVariableAsignada = self.tablaSimbolos.getVarInformationRecursivo(
                                        nameVariableV2, scope, False, [])[1]
                                    if(self.functions.checkIfIsInt(valorAsignado)):
                                        # si del lado derecho es int, miramos al lado izquierdo
                                        if(tipoVariableAsignada != "int"):
                                            print(
                                                f'--> ERROR. El valor asignado del lado derecho es INT y no corresponde con el del izquierdo "{nameVariableV2}". linea: {ctx.start.line} , columna: {ctx.start.column}')
                                    elif(self.functions.checkGeneraltype(valorAsignado, "string")):
                                        # si del lado derecho es string, miramos al lado izquierdo
                                        if(tipoVariableAsignada != "string"):
                                            print(
                                                f'--> ERROR. El valor asignado del lado derecho es STRING y no corresponde con el del izquierdo "{nameVariableV2}". linea: {ctx.start.line} , columna: {ctx.start.column}')
                                    elif(valorAsignado == "true" or valorAsignado == "false"):
                                        # si del lado derecho es boolean, miramos al lado izquierdo
                                        if(tipoVariableAsignada != "boolean"):
                                            print(
                                                f'--> ERROR. El valor asignado del lado derecho es BOOLEAN y no corresponde con el del izquierdo "{nameVariableV2}". linea: {ctx.start.line} , columna: {ctx.start.column}')
                                    else:
                                        # verificamos la variable o valor
                                        varExistsValor1 = self.tablaSimbolos.varExistsRecursivo(
                                            valorAsignado, self.scopeActual, False)
                                        if(varExistsValor1 == False):
                                            print(
                                                f'--> ERROR. La  variable "{valorAsignado}" no ha sido "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        else:
                                            varInformation1 = self.tablaSimbolos.getVarInformationRecursivo(
                                                valorAsignado, self.scopeActual, False, [])
                                            # el tipo de variable
                                            varTypeInterno1 = varInformation1[1]
                                            # si del lado derecho la var no tiene el mismo tipo
                                            if(varTypeInterno1 != tipoVariableAsignada):
                                                print(
                                                    f'--> ERROR. El valor asignado del lado derecho es no tiene el mismo tipo que el izquierdo y no corresponde con el del izquierdo. linea: {ctx.start.line} , columna: {ctx.start.column}')
                                else:
                                    print(
                                        f'--> ERROR_TESTEO. La variable o valor "{nameVariableV2}" NO existe. linea: {ctx.start.line} , columna: {ctx.start.column}')
                            else:  # es una estructura a la izquierda
                                indice = nameVariableV2.index(".")
                                variableEstructura = nameVariableV2[0:indice]
                                variableDentroEstructura = nameVariableV2[indice+1:len(
                                    nameVariableV2)]
                                # si la variable que hicimos split o partimos tiene corchete obtenemos solo el nombre
                                if("[" in variableEstructura or "]" in variableEstructura):
                                    indexCorchete = variableEstructura.index(
                                        "[")
                                    variableEstructura = variableEstructura[0: indexCorchete]
                                if("[" in variableDentroEstructura or "]" in variableDentroEstructura):
                                    indexCorchete = variableDentroEstructura.index(
                                        "[")
                                    variableDentroEstructura = variableDentroEstructura[0: indexCorchete]
                                # mandamos ambos parametros
                                structExists = self.tablaSimbolos.varExistsRecursivo(
                                    variableEstructura, self.scopeActual, False)
                                if(structExists):  # si la estructura existe
                                    # obtenemos infromacion de la estructura y d ela variable que estamos apuntando
                                    informacionStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                        variableEstructura, self.scopeActual, False, [])
                                    innerVarExists = self.tablaSimbolos.checkVarInVarSymbolTableV2(
                                        variableDentroEstructura, informacionStruct[1])
                                    if(innerVarExists):
                                        informacionInnerVarStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                            variableDentroEstructura, informacionStruct[1], False, [])
                                        tipoDatoInnerVariable = informacionInnerVarStruct[1]
                                        if(self.functions.checkIfIsInt(valorAsignado)):
                                            # si del lado derecho es int, miramos al lado izquierdo
                                            if(tipoDatoInnerVariable != "int"):
                                                print(
                                                    f'--> ERROR. El valor asignado del lado derecho es INT y no corresponde con el del izquierdo "{nameVariableV2}". linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        elif(self.functions.checkGeneraltype(valorAsignado, "string")):
                                            # si del lado derecho es string, miramos al lado izquierdo
                                            if(tipoDatoInnerVariable != "string"):
                                                print(
                                                    f'--> ERROR. El valor asignado del lado derecho es STRING y no corresponde con el del izquierdo "{nameVariableV2}". linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        elif(valorAsignado == "true" or valorAsignado == "false"):
                                            # si del lado derecho es boolean, miramos al lado izquierdo
                                            if(tipoDatoInnerVariable != "boolean"):
                                                print(
                                                    f'--> ERROR. El valor asignado del lado derecho es BOOLEAN y no corresponde con el del izquierdo "{nameVariableV2}". linea: {ctx.start.line} , columna: {ctx.start.column}')
                                        else:
                                            # si lo del lado derecho es una estructura
                                            if("." in valorAsignado):
                                                indice = valorAsignado.index(
                                                    ".")
                                                variableEstructuraAsignado = valorAsignado[0:indice]
                                                variableDentroEstructuraAsignado = valorAsignado[indice+1:len(
                                                    valorAsignado)]
                                                # obtenemos infromacion de la estructura y d ela variable que estamos apuntando
                                                informacionStruct2 = self.tablaSimbolos.getVarInformationRecursivo(
                                                    variableEstructura, self.scopeActual, False, [])
                                                informacionInnerVarStruct = self.tablaSimbolos.getVarInformationRecursivo(
                                                    variableDentroEstructura, informacionStruct2[1], False, [])
                                                tipoDatoInnerVariable2 = informacionInnerVarStruct[1]
                                                # si del lado derecho la var no tiene el mismo tipo
                                                if(tipoDatoInnerVariable2 != tipoDatoInnerVariable):
                                                    print(
                                                        f'--> ERROR. El valor asignado del lado derecho es no tiene el mismo tipo que el izquierdo y no corresponde con el del izquierdo. linea: {ctx.start.line} , columna: {ctx.start.column}')
                                            else:
                                                # verificamos la variable o valor
                                                varExistsValor1 = self.tablaSimbolos.varExistsRecursivo(
                                                    valorAsignado, self.scopeActual, False)
                                                if(varExistsValor1 == False):
                                                    print(
                                                        f'--> ERROR. La  variable "{valorAsignado}" no ha sido "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                                else:
                                                    varInformation1 = self.tablaSimbolos.getVarInformationRecursivo(
                                                        valorAsignado, self.scopeActual, False, [])
                                                    # el tipo de variable
                                                    varTypeInterno1 = varInformation1[1]
                                                    # si del lado derecho la var no tiene el mismo tipo
                                                    if(varTypeInterno1 != tipoDatoInnerVariable):
                                                        print(
                                                            f'--> ERROR. El valor asignado del lado derecho es no tiene el mismo tipo que el izquierdo y no corresponde con el del izquierdo. linea: {ctx.start.line} , columna: {ctx.start.column}')
                                    else:
                                        print(
                                            f'--> ERROR. Variable "{variableDentroEstructura}" no existe DENTRO de la estructura "{informacionStruct[1]}".  "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')
                                else:
                                    print(
                                        f'--> ERROR. Variable {variableEstructura} de tipo Estructura NO existe "{self.scopeActual}", linea: {ctx.start.line} , columna: {ctx.start.column}')

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
                indexCorchete = name.index("[")
                name = name[0: indexCorchete]
                arrayValue = ctx.field_var()[x].array_id().expr().getText()

                if(self.functions.checkIfIsInt(arrayValue)):
                    # valor declarado dentro del array
                    arrayValue = int(arrayValue)
                    claseError = Errores(name, column, line, "")
                    hasError, errorValue = claseError.checkArrayError(
                        arrayValue, False)
                    if(hasError):
                        print(errorValue)
                        # exit()
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
                            # exit()
                    else:
                        print(
                            f'--> ERROR. La variable o valor "{oldArrayValue}" no ha sido declarada e intenta usarse en un array en la linea:{line} columna:{column} ')
                        # exit()

                # we add the array to the struct table
                self.tablaSimbolos.AddNewStruct_DictStruct(
                    name, tipo, self.scopeAnterior)

            varExists = self.tablaSimbolos.checkVarInVarSymbolTableV2(
                name, self.scopeActual)
            if(varExists == False):
                if("struct" in tipo):
                    tipo = tipo.replace("struct", "")
                self.tablaSimbolos.AddNewVar_DictVar(name, tipo, scope, 0, 0)
            elif(varExists == True):
                print(
                    f'--> Error_VarDeclaration2, la variable {name} ya fue declarada en el scope {scope}. Linea: {line} columna: {column} ')
                # exit()
            # ya tenemos las variables actuales
            # print(name, " ", column, " ", line, " ", tipo, " scope: ", scope)

    def enterArray_id(self, ctx: decafAlejandroParser.Array_idContext):
        name = ctx.ID().getText()  # el nombre del array
        column = ctx.start.column
        line = ctx.start.line
        # verificamos si lo que viene es un numero o letra
        arrayValue = ctx.expr().getText()
        if(self.functions.checkIfIsInt(arrayValue)):
            # valor declarado dentro del array
            arrayValue = int(arrayValue)
            # verificamos si lo que es es una estructura o variable
            # si no es int verificamos que no sea una variable de una estructura o global
            varExists = self.tablaSimbolos.varExistsRecursivo(
                name, self.scopeActual, False)
            varExistsStruct = False
            estructuras = self.tablaSimbolos.getDictStruct()
            for tupla, valorTupla in estructuras.items():
                varExistsArray2 = self.tablaSimbolos.varExistsRecursivo(
                    name, valorTupla[0], False)
                if(varExistsArray2):
                    varExistsStruct = True
            if(varExists == True or varExistsStruct == True):
                pass
            elif(varExists == False or varExistsStruct == False):
                claseError = Errores(name, column, line, "")
                hasError, errorValue = claseError.checkArrayError(
                    arrayValue, False)
                if(hasError):
                    print(errorValue)
                # exit()
        elif(self.functions.checkIfIsInt(arrayValue) == False):
            # si no es int verificamos que no sea una variable
            varExistsArray = self.tablaSimbolos.varExistsRecursivo(
                arrayValue, self.scopeActual, False)
            if(varExistsArray):
                pass
            else:
                print(
                    f'-->  ERROR . El valor DENTRO de un corchete de array debe ser INT. La variable o valor "{arrayValue}" no lo es o no. Linea: {line} columna: {column} ')
            # exit()
        else:
            varExists = self.tablaSimbolos.checkStructInStructSymbolTableV2(
                arrayValue)
            if(varExists == False):
                print(
                    f'--> ERROR_ARRAY. La variable {arrayValue} no es un array . linea: {ctx.start.line} , columna: {ctx.start.column}')
                # exit()


def main(nombreFile=""):
    """
    método main principal
    """
    streamNameFile = 'Python3/programs/' + nombreFile
    data = ""
    lexer = ""
    try:
        data = open(streamNameFile).read()
        # hacemos el open de la data del archivo de prueba
        # invocamos al lexer
        lexer = decafAlejandroLexer(InputStream(data))
    except:
        print('Error, introduce UN NOMBRE DE ARCHIVO VALIDO')
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


def pedirNumeroEntero():
    """
        Pide un numero en consola y retorna el numero
    """
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num


salir = False
opcion = 0

while not salir:
    """
    Menú principal
    """
    print("")
    print("------------------------> MENU <-----------------------")
    pprint("1. Opcion 1: cargar archivo de pruebas y ejecutar")
    pprint("2. Opcion 2: SALIR")

    pprint("Elige una opcion")

    opcion = pedirNumeroEntero()

    if opcion == 1:
        nombreFile = str(input("Introduce el nombre del .decaf : "))
        main(nombreFile)
    elif opcion == 2:
        salir = True
    else:
        print("Introduce un numero entre 1 y 2")

print("Fin. ADIOS")
