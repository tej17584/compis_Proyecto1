"""
Nombre: Alejandro Tejada
Curso: Diseño Compiladores
Fecha: agosto 2021
Programa: ErrorClass.py
Propósito: este programa maneja los errores que podemos chequear
           y los imprime en consola
V 1.0
"""


class Errores():
    """
    Esta clase se encarga de los errores que puedan surgir y que podamos
    manejar a nivel lógico sin necesidad de tabla de símbolos
    """

    def __init__(self, nombre="", columna="", linea="", tipo="") -> None:
        self.nombre = nombre
        self.columna = columna
        self.linea = linea
        self.tipo = tipo
        self.arrayErrores = []

    def checkArrayError(self, numero, isLetter):
        """
        Método general de chequeado de errores para arrays
        *@param numero: es el numero declarado en el array
        *@param isLetter: indica si estamos tanteando una letra
        """
        # Chequeo de regla semántica: num en la
        # declaración de un arreglo debe de ser mayor a 0.
        if(numero <= 0 and (isLetter == False)):
            return True, f'Error de declaración del array con nombre:{self.nombre}. En linea: {self.linea}, columna:{self.columna}. El valor declarado es de : -> {numero} <- y se espera uno mayor a 0'
        elif(numero <= 0 and (isLetter == True)):
            return True, f'Error de declaración del array con nombre:{self.nombre}. En linea: {self.linea}, columna:{self.columna}. La variable usada DENTRO del array tiene un valor de: -> {numero} <- y se espera uno mayor a 0'
        return False, ""

    def addNewError(self, error):
        """
        Método para agregar un nuevo error al stack
        *@param error: el nuevo error
        """
        self.arrayErrores.append("--> ", error)

    def getAllErrors(self):
        """
        REtorna todos los errores
        """
        return self.arrayErrores


class SemanticError():
    def __init__(self):
        self.errores = []
        self.IDENTIFICADOR_DECLARADO_MUCHAS_VECES = 'Identificador no puede estar declarado más de una vez en el mismo ámbito.'
        self.MAIN_PARAMETERLESS = 'No existe un método llamado main sin parámetros.'
        self.NUMERO_PARAMETROS_METODO = 'El número de argumentos en la llamada al método no coincide.'
        self.TIPO_PARAMETROS_METODO = 'El typeValue de dato en los argumentos en la llamada al método no coincide.'
        self.EQ_OPS = 'El typeValue de dato de operandos no es el mismo para los operadores "==" y "!=".'
        self.ARITH_OP = 'El typeValue de dato de operando debe ser INT para operadores aritméticos.'
        self.REL_OP = 'El typeValue de dato de operando debe ser INT para operadores de relación.'
        self.COND_OP = 'El typeValue de dato en operación condicional debe ser boolean.'
        self.IF_BOOLEAN = 'El typeValue de dato dentro de condición de IF debe ser boolean.'
        self.WHILE_BOOLEAN = 'El typeValue de dato dentro de condición de WHILE debe ser boolean.'
        self.ASIGNACION = 'La asignación de dos valores deben ser del mismo typeValue.'
        self.RETURN_TYPE = 'El valor de retorno debe de ser del mismo typeValue con que fue declarado el método.'
        self.RETURN_VOID = 'Un método declarado VOID no puede retornar ningún valor.'
        self.MUST_STRUCT = 'El typeValue de dato de la variable debe ser STRUCT.'
        self.METHOD_NOT_DECLARED = 'El método no existe o no hay definición del método previamente a ser invocado.'
        self.SHADOW_PARAMETER = 'No es posible declarar una variable con el nombre de un parámetro.'

    def AddEntryToTable(self, line, col, msg):
        self.errores.append({
            'Line': line,
            'Col': col,
            'Msg': msg
        })

    def ToString(self):
        for error in self.errores:
            print(' => Line ' + str(error['Line']) +
                  ':' + str(error['Col']) + ' ' + error['Msg'])

    def GetErrores(self):
        errors = []
        for error in self.errores:
            errors.append(
                ' => Line ' + str(error['Line']) + ':' + str(error['Col']) + ' ' + error['Msg'])
        return errors